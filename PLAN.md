# Astra Maths: a Year 2 maths academy for Finn (6) and Dad

**Status:** build-ready plan. Written 11 Oct 2026, the first half of Finn's Year 2 autumn term.
**Builder:** Opus 5.5 as orchestrator, Haiku 5.5 subagents for parallel content, puzzle banks, patches and QA. See section 10.
**Source material:** `research/01-synthesis-method.md` (what Synthesis Tutor does, from the screenshots and sources), `research/02-curriculum-year1.md` and `research/03-curriculum-year2.md` (the England National Curriculum statements, verbatim, with IDs), `research/04-coverage-map.md` (every statement mapped to a mission). Where this plan and a research file disagree, the research file wins.
**Sister app:** Astra Finn, the space academy in `C:\1 Astra Nova - Finn`, live at https://philhandley.github.io/astra-finn/. Astra Maths reuses its engine, style, tooling and deployment route. Same tablet, same crew.

---

## 1. The brief in one paragraph

A tablet web app that Finn and Dad use together for 15 to 25 minutes at a time. It teaches maths the Synthesis Tutor way: a tutor who speaks in short lines on the left, a manipulative on the right that Finn operates with his fingers (blast rows of dots to make arrays, drag counters into tens and ones, smash a square into quarters, snap dots into groups), warm praise that names exactly what he just did, quick-fire flashcards with a number pad, a fluency map, and arcade games that unlock as he goes. On top sits the Astra Nova layer from the space app: guess before you count, a few Big Questions with no single right answer, "I changed my mind" stars, a debrief and a patch at the end of every mission. The content is the England National Curriculum for Year 2 in full, plus every Year 1 statement as a "Launch Pad" so nothing is missed. It installs on the Samsung tablet from a GitHub Pages link as a home-screen app and works offline.

Hard constraints of this PC are the same as the space app: no Node.js, so no build step; plain HTML, CSS and ES-module JavaScript; Python 3.12 with Pillow for tooling; git with Git Credential Manager; no `gh`.

---

## 2. Teaching method: Synthesis on the screen, Astra Nova in the room, mastery maths underneath

### 2a. What Synthesis Tutor does that we copy (details and screenshots in `research/01-synthesis-method.md`)

1. **Two panels.** Tutor words left (one to three short lines, each read aloud, with a repeat button). One manipulative right. The words describe what the child is doing in the widget: "You made 10 dots by blasting 5 times. Each blast made a new row of dots."
2. **The child operates the maths.** Nothing is watched; everything is dragged, tapped, blasted, smashed or glued.
3. **Ask before you tell.** "Have you done this at school?" with two buttons. "Yes, I know a bit" skips to a quick check; "Not yet" starts at the first small step.
4. **One picture per idea.** Arrays for multiplication, groups for division, equal parts for fractions, columns of dots for place value, a cloud of a hundred dots so a hundred *looks* big.
5. **Fluency on the side.** Flashcards with a number pad, a grid that fills in as facts become solid, arcade games that reward progress.
6. **Mistakes are expected.** No red cross. A wrong answer brings the manipulative back with the same numbers and a smaller step.

### 2b. What we change for a six-year-old in England with Dad beside him

- **Dad is the tutor's voice when it matters.** The app reads its own lines aloud, but there is no microphone, no chatbot and no speech recognition. Dad asks "why?" and "how do you know?". This removes every complaint reviewers had about the Synthesis voice and speech input.
- **England's curriculum, England's words.** Maths, number bonds, part-whole, tens frame, place-value counters, base-10 blocks, pounds and pence, analogue clocks, anticlockwise. Year 1 fundamentals are a proper section, not a remedial mode.
- **Practice never runs out.** Every exercise is generated from a small parameter set. Reviewers' biggest complaint about Synthesis is that able children finish the content in weeks.
- **Re-teach, don't march on.** Reviewers found Synthesis linear. Here a wrong answer always goes *down* a step (smaller numbers, the manipulative shown again), never forward.
- **Astra Nova on top, lightly.** As in the space app, most steps are informative and playful. Only some missions have a Big Question. There are no scores between the two players.
- **One space theme.** The Blaster is already a space game; the rest of the app joins it. Finn's rocket, asteroids and a launch tower reappear.

### 2c. Mastery underneath (the way Finn's school almost certainly teaches)

English primary schools teach "maths mastery": concrete first (counters, cubes), then pictorial (tens frames, part-whole diagrams, number lines, bar models, arrays), then abstract (digits and signs), with the three kept side by side. The DfE's 2020 guidance names the representations to use for each idea and gives "language focus" sentences such as "Seven is made of three and four". The app uses exactly those representations and those sentence stems, so school and home sound the same. The IDs in the research files (for example Y2-AS-3, 2NPV–1) are the statutory statements and the DfE "ready-to-progress" criteria; every mission lists the IDs it covers and `research/04-coverage-map.md` proves nothing is missed.

### 2d. The mission rhythm (so Finn knows the ritual by the second mission)

| Beat | What happens | Why |
|---|---|---|
| **0. Quick Fire** (1 minute, optional) | Ten flashcards from the facts that are due today. Number pad. "Ten in a row!" | Spaced practice, every session. |
| **1. Look** (30 seconds) | One picture or short animation and one question. "Five astronauts. How many boots?" | Problem first. |
| **2. Ask** | "Have you done this at school?" Two buttons. | Finn's own sense of where he is. No test. |
| **3. Commander's Guess** | Estimate before counting: "About how many dots?" with three picture choices, or a slider. Dad guesses second. | Predict before reveal. Being wrong is fine. |
| **4. Try it** (the heart, 3 to 6 small steps) | The manipulative with the tutor narrating Finn's own actions. Each step has one tiny goal ("Blast three more times"). | Synthesis. Concrete, then pictorial, then abstract. |
| **5. Practise** (5 to 8 items) | Generated questions with the manipulative one tap away. Wrong answer: "Not yet. Let's make it with counters." and a smaller number. | Infinite, adaptive, kind. |
| **6. Big Question** (some missions only) | Which One Doesn't Belong, or Would You Rather. Both crew members vote, say why, hear the other, may change their mind. The reveal never crowns a winner. | Astra Nova. |
| **7. Engineer's Error** (some missions) | The Engineer "worked it out" on screen and got it wrong. Finn finds the slip and says what went wrong. | Checking, the inverse, constructive disagreement. |
| **8. Debrief and patch** | "What was your favourite part?" plus one mission question. The patch lands on the wall. | Reflection. The only reward. |

Any step can be skipped with Next. A mission is 6 to 12 minutes.

Crew roles as in the space app: **Finn is Commander** (touches the screen, guesses first, makes the calls), **Dad is Flight Engineer** (reads when the voice is off, asks why, types one line into the Crew Log, plays the Engineer's Error). Dad's three rules on the crew screen: Finn guesses first; ask "how do you know?" more than you explain; changed minds get a cheer.

### 2e. The tutor's voice (rules for every line of script)

- One to three lines per card, under twelve words each, read aloud with a UK voice. A repeat button on every card.
- Say what Finn did, in maths words: "You put 4 tens and 7 ones. That's 47."
- Praise the action, not the child: "Three rows of five. That's a proper array."
- Ask before telling. Offer the sentence stem and let Finn finish it: "Seven is made of three and..."
- Never "wrong", "incorrect" or a red cross. Use "Not yet", then show, then retry smaller.
- One number idea per card. Numbers in digits (47), never spelled out, except in the Numbers in Words missions.
- Use the DfE language-focus sentences where they exist (see the research files).

---

## 3. App map

**Mission Control** (home): starfield, crew names, patch wall, Changed-Mind stars, and the **Star Chart**: eight sectors as tiles with a picture each and a progress ring. Nothing is locked except the Arcade games, which unlock one per sector. An **Engineer's notes** button opens Dad's crib sheet (section 8).

A first-run **Cadet Check** (five minutes, feels like a mission, no score shown) samples Year 1 skills (count on from 37; one more than 19; 7 + ? = 10; half of 8; name a cube; half past 3; count in 5s) and suggests where to start: "Let's begin at the Launch Pad" or "You're ready for the Number Station". Dad can re-run it any time.

### Sector 0: Launch Pad (Year 1 fundamentals, 11 missions, Cadet patches)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| L1 | Count the Stars | A 100 square that lights up as Finn counts forward and back from any number; "what comes before 40?" | Y1-NPV-1, Y1-NPV-3, 1NPV–1 |
| L2 | Numbers in Words to 20 | Tens frames with the numeral and the word; match and build | Y1-NPV-4, Y1-NPV-5, 1NPV–2 |
| L3 | Skip-count Rockets | Number line hops in 2s, 5s and 10s; first go at Asteroid Sort | Y1-NPV-2, 1NF–2 |
| L4 | Bonds to 10 | Tens frame and part-whole model; every pair; "7 is made of 3 and 4" | Y1-AS-2, 1AS–1, 1NF–1 |
| L5 | Bonds to 20 and doubles | Two tens frames; doubles to 10 + 10; near doubles | Y1-AS-2 |
| L6 | Add and subtract within 20 | Counting on, make 10 then add the rest, take away on a number line | Y1-AS-1, Y1-AS-3, 1AS–2 |
| L7 | The Equals Sign | Balance scales; missing numbers such as 7 = ? − 9 | Y1-AS-1, Y1-AS-4 |
| L8 | Halves and Quarters | Smash and Glue: a square, a pizza, a set of 8 dots | Y1-F-1, Y1-F-2 |
| L9 | Shape Spotter | Name 2-D and 3-D shapes in any orientation; compose shapes from smaller ones; quarter and half turns | Y1-G-1, Y1-PD-1, 1G–1, 1G–2 |
| L10 | Clocks, Coins and Days | O'clock and half past; coin and note values; days of the week; before, after, yesterday, tomorrow | Y1-M-3, Y1-M-4, Y1-M-5, Y1-M-6 |
| L11 | Longer, Heavier, Fuller | Compare and measure lengths, mass, capacity and time with non-standard then standard units | Y1-M-1, Y1-M-2 |

Y1-MD-1 (groups and arrays with support) is mission A1 in the Array Blaster sector, which starts at a Year 1 level.

### Sector 1: Number Station (Year 2 place value, 6 missions)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| N1 | Tens and Ones | Place-value columns with base-10 blocks; drag ten ones together and they fuse into a ten; 47 = 40 + 7 | Y2-NPV-2, 2NPV–1 |
| N2 | Count in 2s, 3s, 5s and 10s | Number line hops from any start; the 100 square patterns | Y2-NPV-1 |
| N3 | Number Line Landing | Land the rocket where 67 belongs on 0 to 100; previous and next multiple of 10; estimate on an empty line | Y2-NPV-3, 2NPV–2 |
| N4 | Compare and Order | The hungry crocodile for <, > and =; order five numbers | Y2-NPV-4 |
| N5 | Numbers in Words to 100 | Build "sixty-four" from "sixty" and "four" tiles | Y2-NPV-5 |
| N6 | Partition Lab | Flexible partitioning: 47 = 30 + 17 = 20 + 27; use it to solve a problem | Y2-NPV-6, 2NPV–1 |

### Sector 2: Bonds Bay (Year 2 addition and subtraction, 7 missions)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| B1 | Fact Families | Part-whole model; 3 + 4 = 7 gives four facts; 30 + 40 = 70 by the same picture | Y2-AS-2, 2NF–1, 2AS–3 |
| B2 | Across the Ten | 8 + 5 on two tens frames: fill the ten, then add the rest; 13 − 5 back through 10 | 2AS–1 |
| B3 | Ones and Tens | 47 + 5 and 47 + 30 with blocks and the number line | Y2-AS-3, 2AS–3 |
| B4 | Two-Digit Add and Take | 34 + 28 and 52 − 27 with blocks that exchange; the column layout shown as a picture beside them | Y2-AS-3, 2AS–4 |
| B5 | Three Numbers | 6 + 7 + 4: find the bond to 10 first | Y2-AS-3 |
| B6 | Any Order? | Commutativity and the inverse; check a sum by subtracting; missing numbers; the Engineer's Error | Y2-AS-4, Y2-AS-5 |
| B7 | How Many More? | Bar models for difference; problems with lengths and money | Y2-AS-1, 2AS–2 |

### Sector 3: Array Blaster (Year 2 multiplication and division, 7 missions)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| A1 | Equal Groups | The Blaster: set blast size, fire, watch rows stack; 5 + 5 + 5 = 15; 3 × 5 = 15 | Y1-MD-1, Y2-MD-4, 2MD–1 |
| A2 | Any Order? | Flip the array: 3 rows of 5 becomes 5 rows of 3 | Y2-MD-3 |
| A3 | The 2s | Doubles, pairs of boots, even numbers | Y2-MD-1 |
| A4 | The 10s and the 5s | Tens as fingers, fives as a clock face | Y2-MD-1 |
| A5 | Odd and Even | Pair up the dots; the one left over | Y2-MD-1 |
| A6 | Sharing and Grouping | Snap dots into groups of 4 (24 ÷ 4) and share 24 into 4 bowls | Y2-MD-2, 2MD–2 |
| A7 | Missions with × ÷ = | Problems in context; missing factor; write the statement | Y2-MD-2, Y2-MD-4, 2MD–2 |

### Sector 4: Fraction Forge (Year 2 fractions, 5 missions)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| F1 | Equal Parts | Smash and Glue; equal or not equal; halves of shapes, lengths and sets | Y1-F-1, Y2-F-1 |
| F2 | Quarters | Quarters, 2/4 = 1/2, three quarters | Y2-F-1, Y2-F-2 |
| F3 | Thirds | Hammer 3; link to counting in 3s | Y2-F-1 |
| F4 | Fractions of Amounts | 1/2 of 6 = 3, 1/4 of 12 by sharing dots into bowls | Y2-F-2 |
| F5 | Counting in Fractions | A number line in halves and quarters past 1 (non-statutory) | Y2-F-1 |

### Sector 5: Measure Lab (Year 2 measurement, 7 missions)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| M1 | Length | Drag a ruler along a rocket part; cm and m; estimate then measure; order with <, > | Y2-M-1, Y2-M-2 |
| M2 | Mass | Balance scales with g and kg weights | Y2-M-1, Y2-M-2 |
| M3 | Capacity and Temperature | Fill a jug in ml and l; read a thermometer in °C | Y2-M-1, Y2-M-2 |
| M4 | Coins and Notes | UK coins and notes into a purse; £ and p; make 50p three ways | Y2-M-3, Y2-M-4 |
| M5 | The Shop | Buy supplies, add, take away, give change | Y2-M-5 |
| M6 | Clock Tower | Drag the hands: quarter past, quarter to, five minutes | Y2-M-7 |
| M7 | Time Flies | 60 minutes in an hour, 24 hours in a day; order and compare intervals | Y2-M-6, Y2-M-8 |

### Sector 6: Shape Dock (Year 2 geometry, 5 missions)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| S1 | 2-D Shapes | Tap to count sides and vertices; fold for vertical symmetry | Y2-G-1, 2G–1 |
| S2 | 3-D Shapes | Spin a cube, cuboid, pyramid, cylinder, cone, sphere; tap faces, edges, vertices | Y2-G-2, 2G–1 |
| S3 | Shapes on Shapes | Which 2-D shape is on this face? Sort shapes and everyday objects | Y2-G-3, Y2-G-4 |
| S4 | Patterns | Continue and make repeating patterns of shapes and colours | Y2-PD-1 |
| S5 | Rover Drive | Drive a rover on a grid: forward, quarter turn clockwise, half turn, right angles | Y2-PD-2 |

### Sector 7: Data Deck (Year 2 statistics, 3 missions)

| # | Mission | Manipulative | Covers |
|---|---|---|---|
| D1 | Tally and Table | Tally the asteroids by colour; fill a table | Y2-S-1, Y2-S-2 |
| D2 | Pictograms | Build a pictogram where one symbol is 2, 5 or 10; total and compare | Y2-S-1, Y2-S-3 |
| D3 | Block Diagrams | Build and read a block diagram; ask your own question | Y2-S-1, Y2-S-2, Y2-S-3 |

51 missions in all, roughly seven hours of guided content, plus unlimited practice and the Arcade.

### The Arcade (unlocks one game per sector finished)

| Game | Synthesis original | What it is | Facts it drills |
|---|---|---|---|
| **Quick Fire** | Flashcards | A deck, a number pad, a three-colour progress bar, "ten in a row" | Bonds to 20, 2s, 5s, 10s, related facts to 100 |
| **Fact Map** | Times-table grid | A 10 × 10 grid showing only the 2, 5 and 10 rows plus a bonds-to-20 grid; cells go grey, amber, green as facts become solid; no times shown to Finn | Y2-MD-1, Y2-AS-2 |
| **Asteroid Sort** | Space shooter | Rocket at the bottom; asteroids carry numbers; shoot the ones that fit the rule ("multiples of 5", "makes 10 with 3", "even") | Y2-NPV-1, Y2-MD-1, Y2-AS-2 |
| **Tile Dock** | Tile sums puzzle | 2 × 2 and 3 × 3 grids with row and column totals within 20; drag tiles into the gaps | Y1-AS-4, Y2-AS-5 |
| **Rocket Landing** | (ours) | Land on the number line at the right spot; harder lines have fewer marks | Y2-NPV-3 |
| **Shop Run** | (ours) | Make the exact amount with the fewest coins before the countdown; rule change halfway: "the 20p slot is broken" | Y2-M-3, Y2-M-4 |

### Playground

Every manipulative with no goal and no tutor: blast arrays, build numbers, smash fractions, set the clock, drive the rover. Synthesis has this and children use it.

---

## 4. The Astra Nova layer: Big Questions for maths

Formats, not answers, borrowed from four well-known classroom traditions (we write our own puzzles): **Which One Doesn't Belong** (four pictures, every one can be the odd one out, Christopher Danielson, https://wodb.ca), **Would You Rather Maths** (two choices with a real trade-off, John Stevens, https://www.wouldyourathermath.com), **Estimation 180** (estimate from a photo, Andrew Stadel, https://estimation180.com) and NRICH's low-threshold, high-ceiling tasks for Key Stage 1 (University of Cambridge, https://nrich.maths.org). All four are free teaching formats used in UK classrooms.

Each sector has two or three Big Questions. Each has three or four picture-sized options, no right answer, a reveal that shows how different people argued, and the follow-up "What would change your mind?". Examples the writers should match in tone:

- **Number Station:** Which one doesn't belong: 25, 52, 50, 15? (Only 52 is not in the 5s; only 50 has no ones; only 15 is under 20; only 25 is a square, which nobody needs to know.) Would you rather have 6 tens or 58 ones?
- **Bonds Bay:** Would you rather work out 9 + 7 or 10 + 6? Which doesn't belong: 7 + 8, 15 − 0, 9 + 6, 8 + 8?
- **Array Blaster:** Would you rather have 3 bags of 5 sweets or 5 bags of 3? Share 7 biscuits between 2 astronauts: what do you do with the extra one?
- **Fraction Forge:** Would you rather have half of a small pizza or a quarter of a giant one? Is a half always the same size?
- **Measure Lab:** Would you rather have 5 coins or 2 coins? (It depends which.) Pack the pod: spend exactly £1 with three coins, more than one way.
- **Shape Dock:** Which doesn't belong: square, rectangle, triangle, circle? (Every answer works.)
- **Data Deck:** One symbol for 2 or one symbol for 10: which pictogram tells the story better?

The **Engineer's Error** cards are the other Astra Nova move: the Engineer's working appears with a plausible slip (forgot to exchange, counted the start number, read the clock hands the wrong way round). Finn finds it. "What would you tell the Engineer?"

---

## 5. Fluency and adaptivity (simple, on the device)

- **Item bank:** every fact (bond, double, 2s, 5s, 10s, related facts to 100) is one item with a Leitner box 0 to 4 in `localStorage`. Correct moves it up a box; a slip moves it down one. Boxes are due after 0, 1, 3, 7 and 14 days.
- **Quick Fire** draws ten due items, newest boxes first, and mixes in two solid ones so every round has early wins.
- **Fact Map** colours each cell by box: grey (not met), amber (box 0 to 1), green (box 2 to 4). It never shows times or percentages to Finn. Dad's notes show counts.
- **Mission check:** the "Ask" step and a three-item check decide whether to run all Try-it steps or go straight to Practise.
- **Practise:** generators take a difficulty level per strand (for example bonds: totals to 5, to 10, to 20; add: no exchange, exchange). Three in a row right raises the level for the session; one slip drops it and shows the manipulative. Levels persist per strand.
- **No timers Finn can see.** Quick Fire's bar fills with cards, not seconds. Asteroid Sort has a soft pace with no game over.

---

## 6. Look and feel

- **Same family as Astra Finn:** near-black navy, faint starfield, ivory text, gold for actions, cyan for data. Space Grotesk headings, Inter body, body text no smaller than 20 px, buttons at least 56 px, drag targets at least 64 px. Landscape tablet at about 1280 by 800.
- **The manipulative panel is a lighter slate console** so counters stay crisp. Counter colours are fixed app-wide so the same colour always means the same thing: ones cyan, tens gold, hundreds magenta; blast dots blue on the Tron grid as in the Synthesis Blaster; fraction fills from a set of eight.
- **Numbers are huge.** The equation caption above a widget ("4 × 3 = 12") is at least 40 px.
- **Every card has Read aloud.** The voice reads automatically unless switched off (a toggle on Mission Control, as in Astra Finn).
- **Sound:** optional, off by default. A blaster "pew", a soft click for a counter landing, a chime for a patch.
- **Feedback animation, never a cross:** a wrong tap makes the manipulative gently rebuild the question. A right answer makes the caption glow gold.

---

## 7. Technical architecture (zero build step, forked from Astra Finn)

Copy from `C:\1 Astra Nova - Finn`: `index.html`, `manifest.webmanifest`, `css/app.css` (tokens and components), `js/core/` (store, speak, patch, icons), `tools/` (build_sw.py, sw.template.js, shot.sh, make_artifact.py), `dev/harness.html`. Change the app name, the storage key (`astramaths.v1`) and the icons. Three.js stays in the import map only for Shape Dock's 3-D shapes (Phase 2); everything else is SVG and canvas.

```
/index.html                      shell, import map, service-worker registration
/manifest.webmanifest            "Astra Maths", standalone, landscape
/sw.js                           generated by tools/build_sw.py
/css/app.css                     tokens, layout, components, manipulative console
/js/app.js                       router (#/sector/mission), Mission Control, Star Chart, crew, patches, Crew Log, Cadet Check
/js/core/store.js                localStorage state: crew, patches, stars, log, fluency boxes, strand levels
/js/core/speak.js                read aloud, UK voice (from Astra Finn)
/js/core/fluency.js              Leitner boxes, due items, Fact Map data
/js/core/steps.js                the mission runner: step types, tutor panel, Next and Back, re-teach rule
/js/widgets/tensframe.js         one or two tens frames, draggable counters
/js/widgets/partwhole.js         part-whole (cherry) model with counters and digits
/js/widgets/numberline.js        0 to 20 and 0 to 100 lines, hops, landing, empty lines
/js/widgets/placevalue.js        tens and ones columns, base-10 blocks, fuse ten ones into a ten, exchange
/js/widgets/hundred.js           100 square with highlighting
/js/widgets/blaster.js           Array Blaster (canvas): blast size, rows, captions, flip, groups view
/js/widgets/groups.js            drag dots into groups; share into bowls
/js/widgets/fractions.js         Smash and Glue: shapes, lengths, sets; hammer 2, 3, 4; glue; fill
/js/widgets/bar.js               bar models for difference
/js/widgets/balance.js           balance scales for = and missing numbers
/js/widgets/numpad.js            number pad with tick and clear (shared by many)
/js/widgets/clock.js             analogue clock with draggable hands, five-minute snap, digital readout
/js/widgets/coins.js             UK coins and notes, purse, totals, change
/js/widgets/measure.js           ruler, balance with weights, jug, thermometer
/js/widgets/shapes2d.js          2-D shapes, tap sides and vertices, symmetry fold
/js/widgets/shapes3d.js          Three.js cube, cuboid, pyramid, cylinder, cone, sphere; tap faces, edges, vertices (Phase 2)
/js/widgets/pattern.js           repeating patterns and sequences
/js/widgets/rover.js             grid rover: forward, turns, clockwise, right angles
/js/widgets/charts.js            tally, table, pictogram, block diagram builders
/js/gen/*.js                     exercise generators per strand with difficulty levels
/js/arcade/quickfire.js          flashcards
/js/arcade/factmap.js            fluency grid
/js/arcade/asteroids.js          Asteroid Sort (canvas)
/js/arcade/tiledock.js           tile sums puzzle
/js/arcade/landing.js            Rocket Landing
/js/arcade/shoprun.js            Shop Run
/content/sectors.json            sector list, order, patches, unlock rules
/content/<sector>/<mission>.json all copy, step lists, generator params, Big Questions, debrief, sources
/content/bigquestions/*.json     Which One Doesn't Belong and Would You Rather banks per sector
/assets/img/                     CC and public-domain pictures (rockets, astronauts), resized to 1600 px and 300 KB
/assets/patches/                 SVG patches: 11 Cadet, 40 Year 2
/assets/icons/                   PWA icons from Pillow
/research/                       the four briefs
```

Key choices:
- **Widgets are SVG with pointer events** (drag with `setPointerCapture`), except the Blaster and Asteroid Sort, which are canvas for animation. Every widget exposes the same tiny interface: `mount(el, props)`, `on('change', fn)`, `getState()`, `setState()`, `destroy()`. The mission runner and the generators talk to widgets only through that.
- **Scripts refer to widget state** with placeholders: `"You put {tens} tens and {ones} ones. That's {value}."` The runner fills them from `getState()` so the tutor always describes what Finn actually did.
- **Generators are code**, content JSON only names them: `{"gen":"addTwoDigit","level":2,"items":6}`. A generator returns `{prompt, answer, widget, widgetProps, reteach}` where `reteach` is a smaller item for the "Not yet" path.
- **Read aloud** and **state** come from Astra Finn's `speak.js` and `store.js` unchanged, with a new `fluency.js` beside them.
- **Offline:** the service worker precaches everything (shell, CSS, JS, content, images, icons, fonts fall back to system). There are no videos in this app, so it is fully offline after one visit.
- **Local testing:** `python -m http.server 8100` and `tools/shot.sh` as in Astra Finn; `dev/harness.html?widget=blaster` mounts one widget alone with its debug params.

---

## 8. Dad's side: Engineer's notes

Behind one button on Mission Control:
- **This term at school.** Most English primaries follow the White Rose Maths order. Year 2, typical: Autumn: place value, addition and subtraction, shape, money. Spring: multiplication and division, length and height, mass, capacity and temperature. Summer: fractions, time, statistics, position and direction. (Unverified for Finn's school. Ask the teacher for the yearly overview and tick the sector that matches each week.)
- **Coverage checklist:** every Y1 and Y2 ID with the missions that cover it and a tick when the mission's debrief is done (from `research/04-coverage-map.md`).
- **Fact Map with counts:** how many facts are grey, amber and green per family, and the ten shakiest facts.
- **Sentence stems** from the DfE guidance to say out loud: "Seven is made of three and four", "Forty-seven is four tens and seven ones", "How many more is 9 than 6?", "Three groups of five is fifteen".
- **The Crew Log** with export as a text file.

Nothing in Engineer's notes is shown to Finn as a score.

---

## 9. Content format (so content can be written in parallel)

Each `content/<sector>/<mission>.json`:

```json
{
  "id": "arrays-equal-groups",
  "sector": "blaster",
  "title": "Equal Groups",
  "tagline": "Blast rows of dots and count them the fast way",
  "covers": ["Y1-MD-1", "Y2-MD-4", "2MD-1"],
  "hero": { "img": "assets/img/astronaut-boots.jpg", "credit": "NASA, public domain" },
  "steps": [
    { "type": "quickfire", "items": 10 },
    { "type": "look", "text": "Five astronauts in a row.", "question": "How many boots?" },
    { "type": "ask", "text": "Have you made equal groups at school?" },
    { "type": "guess", "prompt": "About how many dots will 3 blasts of 5 make?", "options": ["About 8", "About 15", "About 30"], "reveal": "15. Three rows of five.", "source": "https://www.gov.uk/government/publications/national-curriculum-in-england-mathematics-programmes-of-study" },
    { "type": "try", "widget": "blaster", "props": { "size": 5, "maxRows": 4 },
      "script": [
        { "goal": { "rows": 1 }, "say": "Set the blaster to 5. Blast once." },
        { "goal": { "rows": 3 }, "say": "Blast two more times.", "then": "You made {rows} rows of {size}. That's {total} dots." },
        { "goal": { "caption": true }, "say": "Say it the fast way: 3 times 5 is 15.", "caption": "3 × 5 = 15" }
      ] },
    { "type": "practise", "gen": "equalGroups", "level": 1, "items": 6, "widget": "blaster" },
    { "type": "question", "ref": "bigquestions/blaster.json#bags" },
    { "type": "athome", "text": "Put the shoes by the door in rows of 2. How many shoes? Count in 2s." },
    { "type": "finish", "debrief": ["What was your favourite part?", "When would counting in 5s be faster than counting in 1s?"], "patch": "assets/patches/a1.svg" }
  ]
}
```

Copy rules for the writers: one to three lines per card, under twelve words a line, words a six-year-old can follow when read aloud. Say what Finn did using placeholders. Never "wrong". Every `covers` ID must exist in the research files. Every number fact in a reveal carries a `source` URL (gov.uk for curriculum facts; a coin or clock fact needs no source). Big Questions must be written so a crew could split either way and the reveal never says which option was right. No scenarios with people in danger; a rocket part that "doesn't fit" is fine.

---

## 10. Build plan: Opus 5.5 orchestrating, Haiku 5.5 in parallel

Start a fresh session in `C:\1. Astra Nova Synthesis  - Maths Tutor` with Opus 5.5 and the prompt: *"Read CLAUDE.md, PLAN.md and research/, then build Astra Maths as specified. Fork the engine from C:\1 Astra Nova - Finn. Use Haiku 5.5 subagents for the parallel tasks in PLAN.md section 10."*

**Opus does the integrated, hard parts itself:** the fork and rename, the mission runner and step types, the widget interface and every widget, the generators and the re-teach rule, fluency and the Fact Map, the Blaster and Asteroid Sort, Quick Fire, the Cadet Check, the PWA plumbing, deployment.

**Haiku subagents run in parallel.** Each prompt is self-contained and each agent writes only its own files:
1. `content/launchpad/*.json` (L1 to L11) from `research/02-curriculum-year1.md`.
2. `content/number/*.json` and `content/bonds/*.json` (N1 to N6, B1 to B7) from `research/03-curriculum-year2.md`.
3. `content/blaster/*.json` and `content/fractions/*.json` (A1 to A7, F1 to F5).
4. `content/measure/*.json`, `content/shape/*.json`, `content/data/*.json` (M1 to M7, S1 to S5, D1 to D3).
5. `content/bigquestions/*.json`: three Which One Doesn't Belong sets and two Would You Rather questions per sector, with the "how people argued" reveals, in the tone of section 4.
6. Patches and icons: 51 SVG patches in the navy, ivory and gold style, PWA icons with Pillow, a handful of CC or public-domain hero images with `CREDITS.md`.
7. QA after the first integrated build: tap through every Phase 1 mission at 1280 by 800, record console errors, text under 20 px, targets under 56 px, scripts whose placeholders did not fill, and generators that produced an impossible item.

**Phases with acceptance checks:**
- **Phase 1, the first session:** Mission Control and the Star Chart, crew, the runner, Quick Fire and Fact Map, Launch Pad L1, L4, L5, L6, Number Station N1 to N4, Bonds Bay B1 to B4, Array Blaster A1 to A4, patches, PWA, deployed, installed. Check: install from the link on the tablet; finish L4 and A1 end to end with no console errors; works with Wi-Fi off after one visit.
- **Phase 2:** the rest of Launch Pad, Number Station, Bonds Bay and Array Blaster; Fraction Forge; Measure Lab; Shape Dock (SVG first, Three.js later); Data Deck; Asteroid Sort, Tile Dock, Rocket Landing, Shop Run; Engineer's notes with the coverage checklist. Check: every ID in `research/04-coverage-map.md` has at least one finished mission; the Cadet Check routes correctly.
- **Phase 3:** Playground, the full Big Question banks, Engineer's Error cards everywhere, 3-D shapes in Three.js, sound, Crew Log export, polish.

If time is tight, cut in this order: Three.js shapes, Shop Run, Rocket Landing, Playground, Data Deck's block diagrams. Never cut the Blaster, the tens frame, the place-value columns, Quick Fire or the re-teach rule.

---

## 11. The first session with Finn (25 minutes)

1. **Crew setup and Cadet Check, 6 minutes.** Same names and avatars as the space app. The check feels like a warm-up. Dad reads the three rules.
2. **Launch Pad L4, Bonds to 10, 6 minutes.** Tens frame, part-whole, "7 is made of 3 and 4". Patch.
3. **Array Blaster A1, Equal Groups, 10 minutes.** Set the blaster to 5, blast three times, say it the fast way, flip the array, Big Question "3 bags of 5 or 5 bags of 3?". Patch.
4. **Quick Fire, 2 minutes.** Ten cards. "Ten in a row" if it happens.
5. **Debrief, 1 minute.** "What was your favourite part?" Dad writes one line in the Crew Log.

---

## 12. Deployment and the tablet

Live since 11 Oct 2026 at `https://philhandley.github.io/astra-finn/maths/`, published as a folder of the Astra Finn Pages site, because a separate `astra-maths` repository has to be created on github.com first (`DEPLOY.md` has the steps to move it). Relative paths everywhere. Commit with the GitHub no-reply address used for Astra Finn. Run `python tools/build_sw.py` before every push. On the tablet: open the link in Samsung Internet or Chrome, Add to Home screen or Install, open once online, then it works offline. The Claude Artifact route is the fallback for an instant link.

---

## 13. Decisions made by assumption

- Finn is in Year 2 for 2026 to 2027 and his school follows a mastery scheme in roughly the White Rose order. Dad should confirm the scheme with the teacher; the sectors work in any order.
- Separate app and repository from Astra Finn, with its own storage key, rather than a tab inside the space app, so each stays small and installs separately. Crew names are typed again once.
- The Synthesis layout, manipulatives and tone are copied as classroom-standard mechanics in our own words and art; no Synthesis names, art or text are used.
- Dad voices the tutor where judgement is needed; the app never listens to the microphone.
- No Three.js in Phase 1 so the app loads instantly; 3-D shapes come later.
- Big Questions are few and simple, matching the age-first decision taken for the space app.
- Square numbers, column addition with carrying and numbers beyond 100 appear only as easter eggs in the Playground, since they are beyond Year 2.
