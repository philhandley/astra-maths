"""Copy the deployable app into a folder of another git repo (for example the Astra Finn GitHub Pages repo).

Usage (from the project root):
  python tools/build_sw.py
  python tools/publish.py "C:/1 Astra Nova - Finn/maths"

Only the files the app needs are copied: index.html, manifest.webmanifest, sw.js, .nojekyll, css/, js/, content/, assets/.
The target folder is replaced each time (stale files removed). Then commit and push in the target repo.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ['index.html', 'manifest.webmanifest', 'sw.js']
DIRS = ['css', 'js', 'content', 'assets']


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    target = Path(sys.argv[1]).resolve()
    if target == ROOT or ROOT in target.parents and target.parent == ROOT:
        sys.exit('Refusing to publish into the project itself.')
    if not (ROOT / 'sw.js').exists():
        sys.exit('Run python tools/build_sw.py first.')
    if target.exists():
        if not (target / 'index.html').exists() or not (target / 'manifest.webmanifest').exists():
            sys.exit(f'{target} exists but does not look like a previous publish; not touching it.')
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for f in FILES:
        shutil.copy2(ROOT / f, target / f)
    for d in DIRS:
        shutil.copytree(ROOT / d, target / d, ignore=shutil.ignore_patterns('*.py', 'Thumbs.db', 'desktop.ini'))
    count = sum(1 for p in target.rglob('*') if p.is_file())
    print(f'Published {count} files to {target}')


if __name__ == '__main__':
    main()
