# Astra Maths engine contract

This file is the contract between the core (router, mission runner, fluency, Mission Control) and the parts built in parallel (widgets, generators, mission content, arcade games). Read it fully before writing code. If something you need is missing, do the simplest thing that fits this contract and say so in your report. Never edit files you do not own.

The app is plain HTML, CSS and ES-module JavaScript. No build step, no npm, no frameworks. Relative paths everywhere (the site lives under a GitHub Pages sub-path). The tablet is a Samsung Android tablet in landscape, about 1280 by 800 CSS pixels, used with fingers. Test at 1280 by 800.

Audience: Finn, six, Year 2 in England, with his dad beside him. UK spelling and UK maths words (maths, number bonds, part-whole, tens frame, ones, pence, anticlockwise, vertices).

## 1. Files and ownership

```
index.html, manifest.webmanifest, sw.js            core
css/app.css                                        core (widgets inject their own CSS, see 3.4)
js/app.js                                          core: router, views, mission runner, step types
js/core/*.js                                       core: helpers you may import (see section 2)
js/widgets/<name>.js                               one widget per file (owner named in the brief)
js/gen/<strand>.js                                 exercise generators per strand (owner named in the brief)
js/arcade/<game>.js                                arcade games
content/sectors.json                               core: sectors, mission order, the recommended path
content/missions/<id>.json                         one mission per file (owner named in the brief)
content/curriculum.json                            core: every curriculum ID with a short statement
dev/harness.html?widget=<name>&props=<json>        mounts one widget alone
dev/gen.html?gen=<strand>.<name>&level=<n>&n=<k>   prints generated items and renders them
tools/check_content.py                             validates every mission JSON (run it)
```

## 2. Core helpers you may import

All in `js/core/`. Import with relative paths, for example `import { svg, onTap } from '../core/dom.js'`.

### dom.js
- `h(html)` returns the first element of an HTML string.
- `esc(s)` escapes text for HTML.
- `S(tag, attrs = {}, children = [])` creates an SVG element (namespaced). `attrs` keys are set with `setAttribute`; `class` and `style` work. Children may be elements or strings (text nodes).
- `svgRoot(viewW, viewH, cls)` returns an `<svg>` sized 100% by 100%, `viewBox="0 0 viewW viewH"`, `preserveAspectRatio="xMidYMid meet"`, `touch-action: none`.
- `svgPoint(svgEl, evt)` converts a pointer event to viewBox coordinates.
- `onTap(el, fn)` fires `fn(evt)` on a pointer tap (pointerup within 12 px of pointerdown), never twice for one touch.
- `drag(el, { start(p, evt), move(p, evt), end(p, evt) }, svgEl?)` pointer-captured drag; `p` is in viewBox coordinates when `svgEl` is given, otherwise client coordinates. Returns an unbind function.
- `injectCSS(id, css)` adds a `<style id=id>` once. Use it for all widget CSS. Prefix every class with your widget name (`.w-clock ...`).
- `clamp(v, a, b)`, `sleep(ms)`.

### rand.js
- `makeRand(seed?)` returns `R` with `R.int(a, b)` inclusive, `R.pick(arr)`, `R.shuffle(arr)` (copy), `R.chance(p)`, `R.distinct(n, a, b)` (n different ints), `R.sample(arr, n)`. Generators always use `R`, never `Math.random`, so tests can be repeated.

### theme.js
- `COL`: `{ ones: '#5fd4ff', tens: '#f2b544', hundreds: '#e879f9', a: '#f2b544', b: '#5fd4ff', ink: '#f3efe6', ink2: '#b9c0cf', ink3: '#7d869a', line: 'rgba(255,255,255,.14)', panel: '#121b33', panel2: '#18233f', good: '#6fe3a5', warn: '#ffb36b', bad: '#ff8a6b', blast: '#4f9dff', grid: '#2a6f9a' }`. `ones/tens/hundreds` are fixed app-wide: the same colour always means the same place value. `a/b` are the two counter colours for parts (gold then cyan).
- `FRAC`: eight fill colours for fraction pieces.
- `FONT`: `{ display: "'Space Grotesk', system-ui, sans-serif", body: "'Inter', system-ui, sans-serif" }`.

### art.js
- `art(name, size = 64)` returns an SVG string of a simple space icon drawn in a 100 by 100 box: `rocket, astronaut, star, asteroid, planet, moon, sun, alien, satellite, ufo, boot, helmet, crystal, fuel, apple, cookie, robot, flag, comet, crater`. Use for counting sets, word problems and option tiles.
- `artNames` is the list.

### facts.js
- `factKey(op, a, b)` returns the fluency key for a basic fact: `op` is `'+' | '-' | 'x' | '÷'`. Examples: `factKey('+', 7, 5)` is `'+:5,7'` (addends sorted), `factKey('-', 12, 5)` is `'-:12,5'`, `factKey('x', 3, 5)` is `'x:3,5'` (sorted), `factKey('÷', 15, 5)` is `'÷:15,5'`. Put it on a generator item as `fact` whenever the item is a single basic fact (bonds, facts to 20, the 2, 5 and 10 tables, multiples of ten like 30 + 40 use `factKey('+', 30, 40)`).

### speak.js (core uses it; widgets normally don't speak)
- `sayable(text)` turns maths text into speakable English (`×` to "times", `1/2` to "a half", `£3.50`, `cm` to "centimetres" and so on). The runner already applies it to every tutor line.

### sfx.js
- `sfx(name)` plays a short synthesised sound if sound is switched on: `'pew'` (blaster), `'pop'` (counter placed), `'click'`, `'chime'` (correct), `'whoosh'`, `'clunk'`, `'tick'`. Safe to call any time.

## 3. Widgets

A widget is an interactive or display-only manipulative shown in the right-hand "console" panel. Every widget is an ES module `js/widgets/<name>.js`:

```js
export const meta = {
  title: 'Tens frame',                       // shown in the Playground
  playground: { count: 0, interactive: true }, // props for free play in the Playground
  state: ['count', 'a', 'b'],                  // the keys getState() returns (documentation)
};

export function mount(el, props = {}, ctx = {}) {
  // el: an empty <div> with a definite size (position: relative). Fill it.
  // props: plain JSON (see each widget's spec). Unknown props are ignored.
  // ctx.onChange(state): call after EVERY user action that changes state.
  // ctx.readonly: true means display only, no interaction at all (also props.readonly).
  return {
    getState() { return { /* plain JSON, numbers as numbers */ }; },
    update(newProps) { /* merge into props, redraw, keep listeners; must not call onChange */ },
    showAnswer(answer) { /* optional: animate the correct state for a re-teach */ },
    destroy() { /* remove listeners, timers, rAF, observers; empty el */ },
  };
}
```

### 3.1 Rules for every widget
- Fill `el` exactly and scale to its size. Prefer one `<svg>` from `svgRoot()` with a fixed viewBox (for example 800 by 500) and `meet` scaling, so it looks the same at any size. Canvas is fine for animation (cap devicePixelRatio at 2, stop rAF in `destroy`, pause when `document.hidden`).
- The console background is dark navy (`COL.panel`). Draw on it; do not paint an opaque full background unless the widget needs a scene (the Blaster's grid).
- Touch first. Tap targets at least 56 px on screen at 1280 by 800, drag handles at least 64 px. Use `onTap` and `drag` from dom.js. Set `touch-action: none` on interactive SVG.
- Numbers and labels in `FONT.display`, at least 22 px on screen; main numbers 32 px or more.
- No text instructions inside the widget. The tutor panel on the left does all the talking. Small labels (column headings "Tens", "Ones", unit names, axis labels) are fine.
- Never show red crosses or "wrong". Widgets have no notion of right and wrong; the runner judges.
- `getState()` must be cheap and return plain JSON (numbers, strings, booleans, arrays). The runner compares it against goals.
- `update(props)` is how the runner sets up new numbers between sub-steps and practice items. Reuse the DOM where easy; a full redraw is fine.
- Respect `props.readonly` / `ctx.readonly`: no handlers, no hover, cursor default.
- Gentle animation (150 to 300 ms). Respect `prefers-reduced-motion`.
- Must not throw on any props combination in your spec; clamp silly values.
- Export `meta` with a working `playground` props object.

### 3.2 Goals the runner checks against your state
In a mission, a "try" sub-step or a practice item may say `"goal": { "tens": 4, "ones": 7 }`. The runner calls `getState()` after every `onChange` and checks each key:
- a number, string or boolean means equality,
- `{ "gte": n }`, `{ "lte": n }`, `{ "in": [..] }`, `{ "not": v }` are also allowed, and can be combined in one object: `{ "gte": 64, "lte": 70 }` means both.
- An array value means the state array must equal it element by element (for example `"bowls": [4, 4, 4]`).
So design state keys that make natural goals: `value`, `total`, `rows`, `size`, `count`, `shaded`, `parts`, `h`, `m`, `x`, `y`, `dir`, and so on.

### 3.3 The widget list and owners
`objects` and `tensframe` are core and already exist; read them as reference implementations. The specs for the rest are in each owner's brief, and are summarised here so other owners can use them in content:

| Widget | Owner | Key props | State |
|---|---|---|---|
| objects | core | `n`, `icon` (art name or `dot`), `arrange` (`row`, `rows`, `groups`, `scatter`, `dice`, `line`), `perRow`, `groups` (array of sizes), `colours` (array of counts per colour, gold then cyan), `crossed` (cross out the last k), `tappable` | `n`, `tapped` |
| tensframe | core | `count`, `frames` (1 or 2), `colours` ([gold, cyan] counts), `twoColour` (show a brush toggle), `interactive`, `max` | `count`, `a`, `b` |
| numberline | number | `min`, `max`, `step`, `labels` (`all`, `ends`, `tens`, `fives`, `none`, or an array), `mode` (`display`, `hop`, `place`), `hopSize`, `start`, `hops` (array of `{from, to}` to draw), `marks` (values to dot), `value`, `markerArt` | `value`, `hops` (count), `pos` (last hop end), `placed` |
| hundred | number | `start` (0 or 1), `highlight` (array), `pattern` (`{every: n, from: k}`), `hide` (array of numbers shown blank), `mode` (`display`, `tap`), `rows` | `selected` (last tapped), `taps` (array) |
| placevalue | number | `tens`, `ones`, `hundreds`, `showHundreds`, `interactive`, `showDigits`, `showValue`, `showExpanded`, `max` | `hundreds`, `tens`, `ones`, `value` |
| partwhole | addsub | `whole`, `parts` ([a, b] or [a, b, c]), `hide` (`whole`, 0, 1, 2 or null), `counters` | `whole`, `parts` |
| bar | addsub | `top` (array of `{v, label}`), `bottom` (array of `{v, label}`), `unknown` (label shown as ?) | none |
| balance | addsub | `left` (string like `"3 + 4"`), `right` (string), `leftValue`, `rightValue` | none |
| blocks | addsub | `a`, `b`, `op` (`+` or `-`), `interactive` (exchange tens and ones) | `tens`, `ones`, `value`, `exchanged` |
| blaster | muldiv | `size`, `rows`, `maxRows`, `maxSize`, `lockSize`, `caption`, `flip`, `interactive` | `size`, `rows`, `total`, `flipped` |
| groups | muldiv | `total`, `mode` (`share` or `group`), `bowls`, `groupSize`, `icon`, `interactive` | `bowls` (array), `groups`, `left`, `done` |
| fractions | muldiv | `shape` (`square`, `rect`, `circle`, `bar`, `set`), `parts`, `setSize`, `tools`, `shaded`, `labels`, `unequal` | `parts`, `shaded`, `equal`, `fraction` |
| clock | measure | `h`, `m`, `interactive`, `snap` (60, 30, 15, 5), `digital` | `h`, `m`, `minutes` (h*60+m, 12-hour) |
| coins | measure | `tray` (array of coin names), `purse` (array), `showTotal`, `interactive`, `price` | `total` (pence), `count`, `items` |
| measure | measure | `tool` (`ruler`, `scales`, `jug`, `thermometer`), `value`, `unit`, `max`, `step`, `interactive`, `object` | `value` |
| shapes2d | geometry | `shape`, `rotate`, `tap` (`sides`, `vertices`, null), `fold` | `sides`, `vertices`, `symmetric`, `folded` |
| shapes3d | geometry | `shape`, `tap` (`faces`, `edges`, `vertices`, null), `autoRotate` | `faces`, `edges`, `vertices` |
| rover | geometry | `cols`, `rows`, `start` (`{x, y, dir}`), `target`, `rocks`, `controls` | `x`, `y`, `dir`, `turns`, `moves`, `atTarget` |
| charts | geometry | `kind` (`tally`, `pictogram`, `block`, `table`), `cats` (array of `{label, icon, value}`), `key`, `interactive`, `max` | `values` (array) |

### 3.4 CSS
Do not edit `css/app.css`. Put widget CSS in a string and call `injectCSS('w-<name>', css)` at mount. Prefix classes with `w-<name>`. App tokens are available as CSS variables: `--ink`, `--ink-2`, `--ink-3`, `--gold`, `--cyan`, `--green`, `--line`, `--panel`, `--font-display`, `--font-body`.

## 4. Generators

A generator makes one practice item at a difficulty level. They live in `js/gen/<strand>.js` as named exports:

```js
export const readTensOnes = {
  about: 'Read a two-digit number shown as tens and ones',
  levels: 3,                         // highest level; levels start at 1
  make(level, R, params = {}) {      // R from rand.js; params from mission JSON (optional)
    return item;
  },
};
```

Mission JSON refers to it as `"gen": "number.readTensOnes"` (file name, dot, export name).

### 4.1 Item format

```js
{
  lines: ['How many tens?', 'How many ones?'],  // tutor lines, 1 to 3, under 12 words each
  caption: '40 + 7 = ?',            // optional big text above the widget (equation, number, word)
  widget: 'placevalue',             // optional widget shown in the console
  props: { tens: 4, ones: 7, readonly: true },
  input: 'numpad',                  // 'numpad' | 'choice' | 'widget' | 'order' | 'none'
  answer: 47,                       // numpad: number (or string for words/times); choice: the option VALUE;
                                    // order: array of values in order; widget: omit (use goal)
  goal: { tens: 4, ones: 7 },       // widget input only: state the widget must reach
  options: [45, 47, 74],            // choice/order: numbers, strings, or {label, value, art?, widget?, props?}
  prefix: '£', unit: 'cm',          // numpad: shown either side of the typed number
  hint: ['Count the tens: 10, 20, 30, 40.'],     // first "Not yet": shown and spoken
  hintProps: { showValue: true },   // optional: merged into widget props on the first "Not yet"
  hintWidget: { widget: 'tensframe', props: {...} },  // optional: show this widget if the item had none
  explain: ['4 tens is 40.', '40 and 7 is 47.'], // second "Not yet": shown with the answer
  fact: '+:5,7',                    // optional fluency key from facts.js
  reteach: { ...a smaller item },   // optional: asked after explain, before moving on
}
```

If an item's `hintProps` contains `interactive: true` (or `readonly: false`), the runner remounts the item's picture as a hands-on widget for the hint. Four option tiles with mini widgets are drawn in a compact row.

How the runner mounts an item's widget: for `numpad`, `choice` and `order` items the widget is readonly unless the item's `props.interactive === true` (use that when the widget is a helper Finn may fiddle with while working the answer out). For `widget` items it is interactive.

Rules:
- Every item must be answerable from what is on screen plus the lines. Check: the answer is in `options` for choice items; numpad answers are whole numbers (or strings for times like `"3:15"`, which the numpad supports with a colon key when `answer` is a string containing `:`); widget goals are reachable from the starting props.
- Level 1 is the easiest. Each level is a clear step up (bigger numbers, fewer supports, abstract instead of pictures). Missions use tiers: tier 1 plays your lower levels, tiers 2 and 3 higher ones.
- Vary contexts with space themes: rockets, astronauts, aliens, moon rocks, fuel cans, crystals, satellites, planets. People are never in danger.
- `lines` say what to do in plain words a six-year-old understands when read aloud. Numbers as digits. One idea per line.
- Prefer `choice` with 3 options for younger levels and `numpad` for higher ones.
- Never put the answer in the lines or caption.
- Always fill `hint` and `explain`. Fill `reteach` where a smaller version helps (for example 47 + 5 reteaches as 7 + 5).

### 4.2 Fluency
If an item is one basic fact, set `fact: factKey(...)`. The core records it into Finn's fact boxes (Leitner) and colours the Fact Map.

## 5. Mission JSON

`content/missions/<id>.json`:

```json
{
  "id": "a1",
  "sector": "blaster",
  "title": "Equal Groups",
  "tagline": "Blast rows of dots and count them the fast way",
  "covers": ["Y1-MD-1", "Y2-MD-4", "2MD–1"],
  "patch": { "name": "Equal Groups", "icon": "blaster" },
  "dadNotes": ["Say 'groups of' before 'times'. Three groups of five is fifteen."],
  "steps": [ ... ]
}
```

- `patch.icon` is one of: `rocket, blocks, partwhole, blaster, fraction, clock, shapes, chart, star, coin, ruler, scales, numberline, hundred, rover, cube, tensframe, words`. If omitted the sector's icon is used.
- `covers` IDs must exist in `content/curriculum.json` (copied from `research/02` and `research/03`; DfE codes use an en dash, `2MD–1`).
- Tiers: every mission can be played at tier 1, 2 or 3 (Cadet, Pilot, Commander). Tier 1 earns the patch; tiers 2 and 3 add stars to it. Any step may have `"tiers": [2, 3]` to appear only at those tiers. Practice steps take `"levels": [l1, l2, l3]` (the generator level for each tier) and `"items": n` or `[n1, n2, n3]`.
- Placeholders in any line: `{key}` is replaced from the widget state (try steps) or item fields, `{commander}` and `{engineer}` are the crew names. Simple arithmetic on state keys works: `{rows * size}`.
- Lines: 1 to 3 per card, each under 12 words, read aloud automatically. Digits for numbers. Never "wrong" or "incorrect"; say "Not yet" (the runner already does this for practice).

### 5.1 Step types

**look**: a picture moment. Tutor lines left; a readonly widget or art on the right.
```json
{ "type": "look", "lines": ["Five astronauts in a row."], "question": "How many boots?",
  "widget": "objects", "props": { "n": 5, "icon": "astronaut", "arrange": "row" } }
```
`"art": "rocket"` instead of a widget shows one big icon; `"big": "47"` shows big text instead.

**ask**: "Have you done this at school?" Two buttons. "Yes, I know a bit" jumps to the next `practise` step; "Not yet" carries on.
```json
{ "type": "ask", "text": "Have you made equal groups at school?" }
```

**guess**: Commander guesses first, Engineer second, then Reveal. No right or wrong colouring beyond showing the answer kindly.
```json
{ "type": "guess", "prompt": "About how many dots will 3 blasts of 5 make?",
  "options": ["About 8", "About 15", "About 30"], "answer": 1,
  "reveal": ["15.", "Three rows of five."],
  "widget": "blaster", "props": { "size": 5, "rows": 0, "readonly": true } }
```

Guess steps may also have `"revealProps"`: props applied to the widget when the answer is revealed.

**try**: the heart of a mission. A widget on the right and a script of small goals on the left.
```json
{ "type": "try", "widget": "blaster", "props": { "size": 1, "rows": 0, "maxRows": 6 },
  "script": [
    { "say": ["Set the blaster to 5.", "Tap the arrows."], "goal": { "size": 5 } },
    { "say": ["Now blast 3 times."], "goal": { "rows": 3 }, "then": ["{rows} rows of {size}.", "That's {total} dots."] },
    { "say": ["How many dots altogether?"], "input": "numpad", "answer": "{total}" },
    { "say": ["Say it the fast way."], "caption": "3 × 5 = 15", "then": ["3 times 5 is 15."] },
    { "set": { "size": 2, "rows": 0 }, "say": ["New size: 2.", "Blast 4 times."], "goal": { "rows": 4 } }
  ] }
```
Sub-step keys: `say` (lines), `goal` (widget state to reach), `input` + `answer` (+ `options` for choice) to ask a question, `set` (props applied with `update()` before the sub-step), `caption` (big text above the widget), `then` (lines after success), `hint` (lines offered by the Help button). A sub-step with neither `goal` nor `input` shows a "Got it" button. `answer` may be a template string like `"{total}"`.

**practise**: generated items with the re-teach loop.
```json
{ "type": "practise", "gen": "muldiv.equalGroups", "levels": [1, 2, 3], "items": [5, 6, 8],
  "params": { "sizes": [2, 5, 10] }, "intro": ["Your turn. Blast and count."] }
```
`gen` may be an array to mix generators. The runner adapts: three right in a row moves up one level (at most one above the tier's level), a "Not yet" moves down one (at most one below). First "Not yet" shows `hint` (and `hintProps`/`hintWidget`), second shows `explain` and the answer, then `reteach` if present.

**question**: an Astra Nova Big Question with no right answer. Use in about half the missions.
```json
{ "type": "question", "format": "wodb", "title": "Which one doesn't belong?",
  "prompt": "Pick one. Then say why.",
  "options": [ { "label": "25" }, { "label": "52" }, { "label": "50" }, { "label": "15" } ],
  "reveal": ["Every one can be the odd one out!", "52 is the only one not in the 5s. 50 has no ones. 15 is the only one under 20. 25 has the same digits as 52."],
  "followUp": "Can you find a reason for every single one?" }
```
`format` is `wodb` (Which one doesn't belong: exactly four options, each one defensible) or `wyr` (Would you rather: two or three options with a real trade-off). Options may carry a mini widget: `{ "label": "6 tens", "widget": "placevalue", "props": { "tens": 6, "ones": 0, "readonly": true } }`. The reveal never says one option was right.

**error**: the Engineer's Error. The Engineer's working is shown line by line with one slip. Finn taps the line with the slip.
```json
{ "type": "error", "intro": ["{engineer} worked this out.", "Can you spot the slip?"],
  "lines": ["34 + 28", "30 + 20 = 50", "4 + 8 = 12", "50 + 12 = 52"], "wrong": 3,
  "fix": ["50 + 12 is 62.", "What would you tell {engineer}?"] }
```

**athome**: a real-world task for the kitchen table.
```json
{ "type": "athome", "title": "Shoe pairs", "need": ["All the shoes by the door"], "steps": ["Put the shoes in pairs.", "Count in 2s."], "why": "Pairs are groups of 2." }
```

**finish**: always last. Debrief and patch.
```json
{ "type": "finish", "debrief": ["What was your favourite part?", "When is counting in 5s faster than counting in 1s?"] }
```

### 5.2 A good mission
- 6 to 12 minutes at tier 1. Usually: look, ask, guess (optional), 1 or 2 try steps (3 to 6 sub-steps each), practise (5 to 8 items), question or error (most missions have one), athome (optional), finish.
- Concrete, then pictorial, then abstract: counters or blocks first, then a picture, then digits.
- Use the DfE language-focus sentences from `research/02` and `research/03` in `say` and `then` lines.
- Tier 2 and 3 steps (`"tiers": [2, 3]`) add a harder try sub-sequence or a second practise with a different generator, so replaying genuinely gets harder.

## 6. Testing you must do
- Do NOT use the built-in browser pane (several builders work at once and would fight over it). Use headless Chrome through `tools/shot.sh`, which uses a separate profile per screenshot name: always prefix your names with your owner tag (for example `num-hundred-1`). Look at the PNG with the Read tool.
- To test interaction headlessly, write throwaway pages named `dev/test-<owner>-<what>.html` (git ignores them) that mount your widget, fire pointer events with `dispatchEvent(new PointerEvent(...))` at element centres, and `console.log` the resulting `getState()`. `tools/shot.sh` prints console lines.
- Do not run git commands. The core owner commits.
- Start a server once: `python -m http.server 8100` from the project root (run it in the background; if port 8100 is already serving, reuse it).
- Widgets: open `http://127.0.0.1:8100/dev/harness.html?widget=<name>&props=<urlencoded JSON>` in the built-in browser at 1280 by 800, interact, read the console (state changes are logged), try `update()` from the harness buttons.
- Generators: `http://127.0.0.1:8100/dev/gen.html?gen=<strand>.<name>&level=<n>&n=20` lists items, checks them with the validator rules above, renders each item's widget, and logs problems to the console as `GEN PROBLEM`.
- Content: `python tools/check_content.py` from the project root validates every mission file (schema, IDs, widget and generator names, levels). It must print no errors for your missions.
- Missions in the real app: `http://127.0.0.1:8100/?devcrew#/m/<id>/1/0` (tier 1, step 0). The core runner is built in parallel with your work; if it is not there yet, rely on the harness pages and the checker. Do not edit core files; report core bugs instead.
- Headless screenshot from bash: `tools/shot.sh <name> "<path-and-query>"` saves a PNG and prints console lines.
