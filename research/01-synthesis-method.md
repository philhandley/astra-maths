# Synthesis Tutor: what it does and how it teaches

Written 11 Oct 2026 from the fourteen screenshots in `Screenshots/`, the Synthesis promo video, the Synthesis website and five independent reviews. This brief tells the builder what to copy, what to adapt and what to avoid. Where a claim is Synthesis marketing it is marked as such.

## 1. What it is

Synthesis Tutor is a maths app for children aged about 5 to 11 from Synthesis, the company spun out of Astra Nova (Josh Dahn and Chrisman Frank). It covers the US K-5 curriculum: counting, place value, addition, subtraction, multiplication, division, fractions and "algebraic thinking". Its pitch is "your child's personal math tutor": a scripted digital tutor talks to the child in short sentences, works a manipulative on screen alongside them, checks understanding with "micro-assessments", and says "mistakes are expected". For children under seven every line and every answer choice is read aloud by default. The company says lessons were designed with educators and neuroscientists and that "no user ever sees live/unchecked LLM output" (engineer on Hacker News, June 2023). Version 2.0 (promo video, 90 seconds, published 2025) added a home screen of topic tiles, streaks, unlockable arcade games and small talk that links the child's interests to maths.

Sources: https://www.synthesis.com/tutor ; App Store listing https://apps.apple.com/us/app/synthesis-math-tutor-for-kids/id6448335635 ; Hacker News launch thread https://news.ycombinator.com/item?id=36246550 ; promo video https://www.youtube.com/watch?v=0x1jJaIcWIo ; review with lesson walkthrough (Amanda Melrose, 15:16, chapter "Multiplication concepts" at 10:32) seen in `Screenshots/IMG_4993.PNG`.

## 2. The screen, exactly as the screenshots show it

Every lesson uses one layout:

- **Left panel, dark, narrow (about a quarter of the width):** the tutor's words. One to three very short lines, each its own paragraph ("Time to let it rip." / "Blast by clicking in the empty space." / "We call that area the blast zone."). A small "repeat" icon above the text replays the speech. Home and settings buttons top left, pause top right. The Synthesis wordmark sits at the bottom.
- **Right panel, wide, light or dark depending on the widget:** the manipulative or game. The tutor's text refers to what the child is doing in the widget, so the two halves feel like one conversation.
- **Top bar of a widget:** the current tool and its setting (ray gun with blast size 1, 2 or 3), a reset button, sometimes a caption bubble with the equation being built ("4 × 3 = 12").
- **Home screen (promo video at 0:58):** four big picture tiles, each with an "In Progress" badge: Numbers and Place Value, Addition and Subtraction, Multiplication, Fractions. A second screen lists arcade games such as "Flashcard Frenzy: Multiply" and "Factor Extractor", which unlock with progress.

The tutor's voice is a specific style worth copying:
- Short declaratives. "Exactly." "Keep going." "Pew pew!" "Well done!" "Let's work through this fraction together."
- It names what the child just did in maths words: "You made 10 dots by blasting 5 times. Each blast made a new row of dots. I've highlighted all 5 rows."
- It asks before it tells: "Have you learned about square numbers before?" with two choice buttons ("Yes, I know quite a bit about square numbers" / "No, I'm still learning about square numbers").
- It greets by name and remembers: "Welcome back, Sam! You're on fire with that 3-day streak."
- It links interests to maths: the child says they love octopuses; the tutor says each arm is "like a fraction of the whole".
- It closes a session gently: "Great work, Lily! Would you like to wrap up for today, or dive into another lesson?"

## 3. The widgets and games seen (the catalogue to build from)

| # | Screenshot | What the screen shows | What the child does | Maths it teaches | KS1 fit |
|---|---|---|---|---|---|
| A | IMG_4991, 4992, 4990, 4993, 5002 | **The Blaster.** Dark space scene with a glowing blue perspective grid. A ray gun icon with a number (blast size) and matching yellow dots in the top bar; arrows change the size. | Tap in the empty "blast zone" to fire. Each blast drops a new row of N dots; rows stack into an array. The tutor highlights the rows, then shows the caption "4 × 3 = 12". With blast size 3 and three blasts it draws a square and asks for the next square number. | Multiplication as repeated rows, arrays, commutativity (rows versus columns), square numbers. | Y1-MD-1, Y2-MD-1, Y2-MD-2, Y2-MD-3, Y2-MD-4. Square numbers are beyond Year 2 and should be an easter egg, not a lesson. |
| B | IMG_4994 | **Place-value columns.** Four tall cards: thousands (pink), hundreds (orange), tens (green), ones (blue). The digit sits above each card, dots inside it, the value below ("3,000 + 400 + 70 + 1"), and "Total: 3,471" underneath. | Drag dots into a column; the digit, the value line and the total update live. | Place value as "how many of each size", expanded form. | Y2-NPV-2, Y2-NPV-6, 2NPV–1. We use only tens and ones, with hundreds as a stretch. |
| C | IMG_5001 | **Dot clouds.** "Expanded Form 1000 + 300 + 50 + 9" with four counters (1000s, 100s, 10s, 1s) with plus and minus buttons. Beside them, clouds of real dots sized to the quantity: a thousand pink dots, three hundred-dot clouds, a ten-dot cloud, one dot. | Tap plus or minus and watch the clouds grow and shrink. | The *size* of a ten versus a one; why 10 ones make a ten. | Y2-NPV-2, Y2-NPV-3, 2NPV–1. |
| D | IMG_5003, promo 0:50 | **Division dots.** "Divide these 24 dots to match the division statement." "24 ÷ 4" top right; "24 Total" and a legend ("4 × 5", "2 × 2") top left. | Drag dots together; four snap into a red flower, two into a purple pair. The legend counts the groups. | Division as grouping (quotitive), the link to multiplication. | Y2-MD-2, Y2-MD-4, 2MD–2. |
| E | IMG_4998, promo 0:12 | **Fraction smash.** A big square. Tools on the right: hammer 2, hammer 3, hammer 5 (split a piece into equal parts), Glue (join pieces), Fill (paint a piece). Pieces are labelled 1/2, 1/4, or "1/?" when the child has to say. A trophy counter. | Smash the whole into halves, smash a half into quarters, glue two quarters back into a half, paint "three quarters". | Equal parts, naming fractions, 2/4 = 1/2, fractions bigger than a half. | Y1-F-1, Y1-F-2, Y2-F-1, Y2-F-2. |
| F | IMG_4997 | **Flashcards.** A deck of cards ("8×2"), a blue number pad with red cross and green tick, a three-colour progress bar (done, correct streak, remaining) and a music toggle. | Type the answer, tick. "10 in a row! You're on fire." | Fluency: fact recall against a gentle clock. Adaptive difficulty (App Store). | Y1-AS-2, Y2-AS-2, Y2-MD-1. |
| G | IMG_4995 | **Times-table grid** (the "Factor Extractor" arcade game). A 12 × 12 grid; each cell holds the child's last answer time (2.9 s), a lightning bolt for fast answers, a red ring for wrong ones; the current row and column glow orange. Speed slider, "24 questions left in round", number pad, Pass button. | Answer the highlighted fact; the grid fills over many rounds. | Which facts are fast, slow or shaky. A visible map of fluency. | Y2-MD-1 (use a 10 × 10 grid showing only the 2, 5 and 10 rows; no times shown to Finn, only colours). |
| H | IMG_4996 | **Tile sums puzzle.** A 4 × 4 grid of number tiles with dot patterns; row totals on the right, column totals below; three loose tiles under it. Options: grid size 2, 3, 4 (bigger locked), Hints on/off, Tile refill. | Drag loose tiles into gaps so every row and column total works. | Addition, missing-number reasoning, checking with the inverse. | Y1-AS-4, Y2-AS-2, Y2-AS-5. Use 2 × 2 and 3 × 3 with totals within 20. |
| I | IMG_5004 | **Column addition.** Three six-digit numbers in huge digits, each column its own colour, a carry row above, a Submit button. "That was the 10 carried over from the 13." | Type each column's answer; carries appear. | Formal written addition. | Year 3 and above. For Year 2 use only two-digit numbers with base-10 blocks beside the columns (Y2-AS-3, non-statutory "use columns to prepare"). |
| J | promo 0:21 | **Space shooter arcade.** A rocket at the bottom, a "Target 2" badge at the top, enemies and asteroids carrying numbers drifting down. | Shoot the ones that match the target rule (multiples, bonds). | Fast recognition of multiples and bonds. | Y1-NPV-2, Y2-NPV-1, Y2-MD-1, Y2-AS-2. |
| K | IMG_4999 | **"Master math with interactive puzzles & stories."** Pyramid and Egyptian numerals. | Story lessons on where numbers came from. | Motivation and context. | Optional story cards. |

Other product facts from the sources: a per-topic progress bar; "Playground" (free play with the widgets, no progress bar) and "Arcade" (fast games) modes; levels that unlock; choice of a background soundtrack; a 7-day free trial; voice speed control; a dyslexia-friendly font; answers can be read aloud.

## 4. What people praise and what they criticise

Praise (reviews and the HN thread): the tutor "responds to" what the child does in the widget rather than being a chatbot; the warm, patient tone eases maths anxiety; children explain ideas at dinner afterwards; it "checks for and develops understanding".

Criticism to design around:
- **Linear.** A wrong answer leads to the next scripted step, not to re-teaching (HN).
- **Slow and repetitive.** The voice "moves at a crawl"; scripts feel repetitive (unite.ai).
- **Runs out.** Able children finish the content in weeks (Trustpilot, aitoolsforkids).
- **Speech input fails.** It sometimes marks correct spoken answers wrong (aitoolsforkids).
- **Not clearly adaptive.** Reviewers could not see how mastery was judged.

Sources: https://www.unite.ai/synthesis-tutor-review/ ; https://www.aitoolsforkids.com/blog/synthesis-tutor-review-ai-math-tutor-for-kids ; https://www.trustpilot.com/review/www.synthesis.is ; https://news.ycombinator.com/item?id=36246550 .

## 5. What we keep, what we change

**Keep (it is what makes it work):**
1. The two-panel layout: tutor words on the left, one manipulative on the right, words that describe the child's own actions.
2. One idea per screen, one to three short lines, every line read aloud, a repeat button.
3. Manipulatives the child *operates* rather than watches: blast rows, drag dots into place-value columns, smash fractions, snap dots into groups.
4. The ask-before-tell move ("Have you learned about this before?") and the warm, specific praise ("You made 10 dots by blasting 5 times").
5. Arrays as the picture of multiplication, grouping as the picture of division, equal parts as the picture of fractions.
6. A fluency map (the grid) and quick flashcards with a number pad.
7. Unlockable arcade games as the reward for lesson progress.

**Change for Finn (six, England, Year 2, with Dad beside him):**
1. **The curriculum is the England National Curriculum Year 2 plus Year 1 fundamentals**, not US K-5. UK words: maths, number bonds, part-whole, tens frame, place-value counters, pounds and pence, analogue clocks, "anticlockwise".
2. **Dad is the tutor.** No AI chat, no microphone, no speech recognition. The script knows what Finn did on screen and says so; Dad asks the "why" questions. This removes every speech-input complaint.
3. **Infinite practice.** Every exercise is generated from a small parameter set, so the content never runs out.
4. **Re-teach, don't march on.** A wrong answer triggers a smaller step with the manipulative, not the next card.
5. **Astra Nova on top.** A few "Big Questions" per topic with no single right answer (Which One Doesn't Belong, Would You Rather), voted on by both crew members, with "I changed my mind" celebrated.
6. **No scores between players, no timers Finn can see.** Patches, the Crew Log and a fluency map that only shows colours.
7. **Space theme throughout.** The Blaster is already a space game; the rest of the app joins it.

## 6. Named games and features to reuse in our own words

We do not copy Synthesis's names, art or text. Ours: Blaster becomes "Array Blaster"; Factor Extractor becomes "Fact Map"; Flashcard Frenzy becomes "Quick Fire"; Fraction smash becomes "Smash and Glue"; the shooter becomes "Asteroid Sort". Mechanics and layout are generic educational interactions (arrays, place-value columns, fraction walls, flashcards, grids) used in maths classrooms everywhere.
