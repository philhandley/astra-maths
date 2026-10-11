"""Validate every mission JSON against ENGINE.md.

Run from the project root:  python tools/check_content.py [mission-id ...]
Prints ERROR and WARN lines and a summary. Exit code 1 if there are errors.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEP_TYPES = {'look', 'ask', 'guess', 'try', 'practise', 'question', 'error', 'athome', 'finish'}
SUB_KEYS = {'say', 'goal', 'input', 'answer', 'options', 'set', 'caption', 'then', 'hint', 'hintProps', 'explain', 'unit', 'prefix'}
INPUTS = {'numpad', 'choice'}

errors, warns = [], []


def err(mid, msg):
    errors.append(f'ERROR {mid}: {msg}')


def warn(mid, msg):
    warns.append(f'WARN  {mid}: {msg}')


def gen_levels(spec):
    """Return the 'levels' number for 'strand.name' or None if missing."""
    if not isinstance(spec, str) or '.' not in spec:
        return None
    strand, name = spec.split('.', 1)
    f = ROOT / 'js' / 'gen' / f'{strand}.js'
    if not f.exists():
        return None
    src = f.read_text(encoding='utf-8')
    m = re.search(r'export\s+const\s+' + re.escape(name) + r'\s*=\s*\{', src)
    if not m:
        return None
    window = src[m.end(): m.end() + 1500]
    lv = re.search(r'\blevels\s*:\s*(\d+)', window)
    return int(lv.group(1)) if lv else 0


def widget_exists(name):
    return isinstance(name, str) and (ROOT / 'js' / 'widgets' / f'{name}.js').exists()


def check_lines(mid, where, lines, max_lines=3):
    if lines is None:
        return
    if isinstance(lines, str):
        lines = [lines]
    if not isinstance(lines, list):
        err(mid, f'{where}: lines must be a list of strings')
        return
    if len(lines) > max_lines:
        warn(mid, f'{where}: {len(lines)} lines (aim for 1 to {max_lines})')
    for ln in lines:
        if not isinstance(ln, str) or not ln.strip():
            err(mid, f'{where}: empty or non-string line')
            continue
        words = len(ln.split())
        if words > 14:
            warn(mid, f'{where}: long line ({words} words): "{ln}"')
        low = ln.lower()
        if re.search(r'\b(wrong|incorrect)\b', low):
            warn(mid, f'{where}: avoid "wrong"/"incorrect": "{ln}"')


def check_mission(path, curriculum, sector_ids):
    mid = path.stem
    try:
        m = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        err(mid, f'invalid JSON: {e}')
        return
    for k in ('id', 'sector', 'title', 'tagline', 'covers', 'steps'):
        if k not in m:
            err(mid, f'missing "{k}"')
    if m.get('id') != mid:
        err(mid, f'id "{m.get("id")}" does not match file name')
    if m.get('sector') not in sector_ids:
        err(mid, f'unknown sector "{m.get("sector")}"')
    for c in m.get('covers', []):
        if c not in curriculum:
            err(mid, f'covers ID "{c}" not in content/curriculum.json (DfE codes use an en dash, e.g. 2MD–1)')
    w = m.get('warmup')
    if w is not None:
        if not isinstance(w, dict) or gen_levels(w.get('gen')) in (None, 0):
            err(mid, f'warmup generator "{(w or {}).get("gen")}" not found')
        elif w.get('level', 1) > gen_levels(w.get('gen')):
            err(mid, 'warmup level above generator max')
        if isinstance(w, dict) and w.get('mission') and not (ROOT / 'content' / 'missions' / f"{w['mission']}.json").exists():
            err(mid, f'warmup mission "{w["mission"]}" not found')
    steps = m.get('steps', [])
    if not isinstance(steps, list) or not steps:
        err(mid, 'steps must be a non-empty list')
        return
    if steps[-1].get('type') != 'finish':
        err(mid, 'last step must be "finish"')
    types = [s.get('type') for s in steps]
    if 'practise' not in types:
        warn(mid, 'no practise step')
    for i, s in enumerate(steps):
        t = s.get('type')
        where = f'step {i} ({t})'
        if t not in STEP_TYPES:
            err(mid, f'{where}: unknown type')
            continue
        tiers = s.get('tiers')
        if tiers is not None and (not isinstance(tiers, list) or not all(x in (1, 2, 3) for x in tiers)):
            err(mid, f'{where}: tiers must be a list drawn from 1, 2, 3')
        if t == 'look':
            check_lines(mid, where, s.get('lines'))
            if not s.get('lines'):
                err(mid, f'{where}: needs lines')
            if s.get('widget') and not widget_exists(s['widget']):
                err(mid, f'{where}: widget "{s["widget"]}" not found')
            q = (s.get('question') or '').strip()
            opts = s.get('options')
            if opts is not None:
                if not (isinstance(opts, list) and len(opts) >= 2):
                    err(mid, f'{where}: options needs 2+ entries')
                a = s.get('answer')
                if a is not None and not (isinstance(a, int) and 0 <= a < len(opts or [])):
                    err(mid, f'{where}: answer must be an option index')
                if not s.get('reveal'):
                    err(mid, f'{where}: options need reveal lines')
            elif s.get('show') is not None:
                sh = s['show']
                if not isinstance(sh, dict) or not (sh.get('lines') or sh.get('props') or sh.get('big')):
                    err(mid, f'{where}: show needs lines, props or big')
                check_lines(mid, where + ' show', sh.get('lines') if isinstance(sh, dict) else None)
            elif q.endswith('?'):
                err(mid, f'{where}: asks "{q}" but gives no way to answer (add options + answer + reveal, or show)')
        elif t == 'ask':
            if not s.get('text'):
                err(mid, f'{where}: needs text')
        elif t == 'guess':
            opts = s.get('options') or []
            if len(opts) < 2:
                err(mid, f'{where}: needs 2+ options')
            a = s.get('answer')
            if a is not None and not (isinstance(a, int) and 0 <= a < len(opts)):
                err(mid, f'{where}: answer must be an option index')
            check_lines(mid, where + ' reveal', s.get('reveal'))
            if s.get('widget') and not widget_exists(s['widget']):
                err(mid, f'{where}: widget "{s["widget"]}" not found')
        elif t == 'try':
            if not widget_exists(s.get('widget')):
                err(mid, f'{where}: widget "{s.get("widget")}" not found')
            script = s.get('script') or []
            if not script:
                err(mid, f'{where}: empty script')
            for j, sub in enumerate(script):
                w2 = f'{where} sub {j}'
                extra = set(sub) - SUB_KEYS
                if extra:
                    warn(mid, f'{w2}: unknown keys {sorted(extra)}')
                check_lines(mid, w2 + ' say', sub.get('say'))
                if 'goal' in sub and not sub.get('hint'):
                    warn(mid, f'{w2}: goal step has no hint for the Help button')
                says = sub.get('say') or []
                if says and str(says[-1]).strip().endswith('?') and 'input' not in sub and 'goal' not in sub:
                    warn(mid, f'{w2}: asks "{says[-1]}" with no input or goal (Finn cannot answer it on screen)')
                check_lines(mid, w2 + ' then', sub.get('then'))
                if 'input' in sub:
                    if sub['input'] not in INPUTS:
                        err(mid, f'{w2}: input must be numpad or choice')
                    if 'answer' not in sub:
                        err(mid, f'{w2}: input without answer')
                    if sub['input'] == 'choice':
                        opts = [o.get('value', o.get('label')) if isinstance(o, dict) else o for o in (sub.get('options') or [])]
                        if len(opts) < 2:
                            err(mid, f'{w2}: choice needs options')
                        elif not isinstance(sub.get('answer'), str) or '{' not in str(sub.get('answer')):
                            if str(sub.get('answer')) not in [str(o) for o in opts]:
                                err(mid, f'{w2}: answer {sub.get("answer")!r} not in options')
                if 'goal' in sub and not isinstance(sub['goal'], dict):
                    err(mid, f'{w2}: goal must be an object')
        elif t == 'practise':
            gens = s.get('gen')
            gens = gens if isinstance(gens, list) else [gens]
            maxlv = None
            for g in gens:
                lv = gen_levels(g)
                if lv is None:
                    err(mid, f'{where}: generator "{g}" not found (js/gen/<strand>.js must export it)')
                elif lv == 0:
                    err(mid, f'{where}: generator "{g}" has no levels number')
                else:
                    maxlv = lv if maxlv is None else min(maxlv, lv)
            levels = s.get('levels')
            if levels is not None:
                if not (isinstance(levels, list) and len(levels) == 3 and all(isinstance(x, int) and x >= 1 for x in levels)):
                    err(mid, f'{where}: levels must be three integers >= 1')
                elif maxlv and max(levels) > maxlv:
                    err(mid, f'{where}: levels {levels} exceed generator max {maxlv}')
            elif 'level' in s and maxlv and s['level'] > maxlv:
                err(mid, f'{where}: level above generator max')
            items = s.get('items', 6)
            if isinstance(items, list):
                if len(items) != 3:
                    err(mid, f'{where}: items list must have 3 numbers')
            elif not isinstance(items, int) or items < 1:
                err(mid, f'{where}: items must be a positive integer or a list of 3')
            check_lines(mid, where + ' intro', s.get('intro'))
        elif t == 'question':
            opts = s.get('options') or []
            fmt = s.get('format')
            if fmt not in ('wodb', 'wyr'):
                err(mid, f'{where}: format must be wodb or wyr')
            if fmt == 'wodb' and len(opts) != 4:
                err(mid, f'{where}: wodb needs exactly 4 options')
            if fmt == 'wyr' and not 2 <= len(opts) <= 3:
                err(mid, f'{where}: wyr needs 2 or 3 options')
            for o in opts:
                if not isinstance(o, dict) or 'label' not in o:
                    err(mid, f'{where}: each option needs a label')
                elif o.get('widget') and not widget_exists(o['widget']):
                    err(mid, f'{where}: option widget "{o["widget"]}" not found')
            if not s.get('reveal'):
                err(mid, f'{where}: needs a reveal')
            check_lines(mid, where + ' reveal', s.get('reveal'), max_lines=4)
        elif t == 'error':
            lines = s.get('lines') or []
            w = s.get('wrong')
            if not (isinstance(w, int) and 1 <= w < len(lines)):
                err(mid, f'{where}: wrong must index a line after the first')
            if not s.get('fix'):
                err(mid, f'{where}: needs fix lines')
        elif t == 'athome':
            if not s.get('title') or not s.get('steps'):
                err(mid, f'{where}: needs title and steps')
        elif t == 'finish':
            if not s.get('debrief'):
                warn(mid, f'{where}: no debrief questions')
    if 'warmup' not in m and m.get('sector') != 'launchpad':
        warn(mid, 'no warmup (the "Not yet" path has no warm-up)')
    tier1 = [s for s in steps if not s.get('tiers') or 1 in s['tiers']]
    if len(tier1) < 4:
        warn(mid, f'only {len(tier1)} steps at tier 1')


def main():
    curriculum = {c['id'] for c in json.loads((ROOT / 'content' / 'curriculum.json').read_text(encoding='utf-8'))}
    sectors = json.loads((ROOT / 'content' / 'sectors.json').read_text(encoding='utf-8'))
    sector_ids = {s['id'] for s in sectors['sectors']}
    planned = [m['id'] for s in sectors['sectors'] for m in s['missions']]
    only = set(sys.argv[1:])
    files = sorted((ROOT / 'content' / 'missions').glob('*.json'))
    for f in files:
        if only and f.stem not in only:
            continue
        check_mission(f, curriculum, sector_ids)
    existing = {f.stem for f in files}
    missing = [p for p in planned if p not in existing]
    for p in planned:
        if p not in sectors['path']:
            warns.append(f'WARN  sectors: {p} is not on the path')
    # Coverage: every curriculum ID covered by at least one existing mission.
    covered = set()
    for f in files:
        try:
            covered |= set(json.loads(f.read_text(encoding='utf-8')).get('covers', []))
        except Exception:  # noqa: BLE001
            pass
    uncovered = sorted(curriculum - covered)
    for line in errors + warns:
        print(line)
    print(f'\n{len(files)} mission files checked, {len(errors)} errors, {len(warns)} warnings.')
    if missing:
        print(f'Not written yet ({len(missing)}): {" ".join(missing)}')
    print(f'Curriculum IDs not yet covered ({len(uncovered)}): {" ".join(uncovered) if uncovered else "none"}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
