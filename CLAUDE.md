# Astra Maths: build instructions

Read `PLAN.md` first. It is the specification. The four briefs in `research/` are the source of truth for every curriculum statement, ID and link; the plan defers to them.

## Who this is for
A six-year-old in Year 2 (Finn, the Commander) and his dad (the Flight Engineer) using a Samsung tablet together, 15 to 25 minutes at a time. Ship Phase 1 of `PLAN.md` section 10 before anything else.

## Where things come from
- Fork the engine from the sister app in `C:\1 Astra Nova - Finn`: `index.html`, `manifest.webmanifest`, `css/app.css`, `js/core/`, `tools/`, `dev/harness.html`. Rename the app, change the storage key to `astramaths.v1`, regenerate icons. Do not edit the sister app.
- The Synthesis Tutor screenshots are in `Screenshots/` and are described widget by widget in `research/01-synthesis-method.md`. Copy the mechanics and layout, not the names, art or text.

## Hard constraints of this machine
- No Node.js and no npm. Do not add a build step, a bundler or a framework that needs one.
- Python 3.12 with Pillow and PyMuPDF is installed. Use it for image resizing, PWA icon generation and `python -m http.server 8100` for local testing.
- git is installed with Git Credential Manager. `gh` is not.
- Chrome and Edge are installed. Use the built-in browser pane to test at 1280 by 800.

## Technical rules
- Plain HTML, CSS and ES-module JavaScript. Libraries only from a CDN, pinned to an exact version at least two weeks old, loaded through an import map, and precached by the service worker. Three.js only for Shape Dock, and only from Phase 2.
- Relative paths everywhere, so the site works under a GitHub Pages sub-path.
- `localStorage` only. No backend, accounts, analytics, microphone or third-party scripts beyond Three.js and Google Fonts.
- Widgets are SVG with pointer events (canvas for the Blaster and Asteroid Sort) and share one interface: `mount(el, props)`, `on('change', fn)`, `getState()`, `setState()`, `destroy()`. The runner and generators use nothing else.
- Generators are code; content JSON only names them with a level and a count. Every generator returns a smaller `reteach` item.
- Tap targets at least 56 px, drag targets at least 64 px, body text at least 20 px, equation captions at least 40 px.
- Images: public domain or Creative Commons only, credited in `assets/img/CREDITS.md`, resized to 1600 px and 300 KB max.

## Content rules (age first, Synthesis voice, Astra Nova flavour)
- One to three lines per card, under twelve words a line, read aloud with a UK voice, a repeat button on every card.
- The tutor says what Finn did, with placeholders filled from widget state: "You put {tens} tens and {ones} ones."
- Never "wrong", "incorrect" or a red cross. "Not yet", then the manipulative with the same numbers, then a smaller item.
- Use the DfE representations and sentence stems in the research files: tens frames, part-whole, number lines, base-10 blocks, bar models, arrays, "Seven is made of three and four".
- Only some missions have a Big Question (Which One Doesn't Belong, Would You Rather). Three or four picture-sized options, no right answer, a reveal that never says which was correct. Write them so a crew could split either way.
- Every mission ends with a debrief ("What was your favourite part?" plus one question) and a patch.
- Every mission lists the curriculum IDs it covers in `covers`; every ID must exist in `research/02` or `research/03`, and `research/04-coverage-map.md` must stay true.
- No scores between the two players. No timers Finn can see. Patches, the Crew Log, Changed-Mind stars and the colour-only Fact Map are the only rewards.
- No scenarios with people in danger.

## Delegation
Use Haiku 5.5 subagents in parallel for the seven tasks listed in `PLAN.md` section 10. Each prompt must be self-contained and each agent writes only its own files. Build the runner, the widgets, the generators, fluency, the Blaster, Quick Fire, the Cadet Check and the PWA plumbing yourself.

## Testing
- `tools/shot.sh <name> "<path-and-hash>" [WxH] [ms]` takes a headless Chrome screenshot of the local server (port 8100) and prints console lines. Add `?devcrew` to skip crew setup.
- `dev/harness.html?widget=<name>&props=<json>` mounts one widget on its own; `dev/gen.html?gen=<strand>&all=1` checks every generator; `dev/smoke.html` checks every mission against the real widgets and generators; `python tools/check_content.py` validates mission JSON and curriculum coverage.
- `?devcrew&devmission=zz-test#/m/zz-test/1/0` runs the dev test mission (every step type).
- Run `python tools/build_sw.py` after any change, before committing. Test offline caching with headless Edge and `dev/test-sw.html` (headless Chrome fails service-worker cache writes on this PC).

## Done means
Installed from the public link on the tablet, Launch Pad L4 and Array Blaster A1 finished end to end with no console errors, Quick Fire and the Fact Map working, and the app still opens with Wi-Fi off after one online visit.
