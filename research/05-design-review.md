# Design review: Astra Maths against Synthesis Tutor (11 Oct 2026)

Phil asked whether the first version looked as good as Synthesis Tutor, and if not, why. This compares the first version with the Synthesis screenshots in `Screenshots/` and records what style v2 changed.

## Verdict on the first version

Not as good visually, although it did more (full Year 1 and 2 coverage, three levels, adaptive practice). The gap was presentation, not content.

| What Synthesis does | What version 1 did | Effect on a six-year-old |
|---|---|---|
| Manipulatives on a bright **white work surface** set in black chrome | Everything on dark navy, including the manipulatives | Dim; the maths didn't pop; every screen felt the same |
| **Bold flat colour coding** that never changes: thousands pink, hundreds orange, tens green, ones blue | Gold tens, cyan ones, muted fills | Weaker colour cues for place value |
| **Big clean numerals** and crisp outlined objects (flash cards, tens frames, tiles) | Thin strokes, ivory on navy, smaller labels | Harder to read at arm's length |
| **Quiet, tactile controls**: white keys, solid bottom edge, the blue number pad | Glassy dark buttons and pills | Felt less like something to press |
| **Vivid picture tiles** on the home screen with "In progress" status | Dimmed space photographs, some unrelated to the topic (the Moon for Bonds Bay) | Less inviting, less clear what each topic is |
| Big Questions and puzzles on the same white surface | Big Questions as a separate dark full-width page | Broke the rhythm of the lesson |
| A friendly geometric sans | Space Grotesk plus Inter | Fine for adults, less suited to early readers |

## What style v2 changed

- **Two panels, Synthesis style**: a black tutor panel with large white text, and a white rounded work surface for every manipulative. The Blaster and the Asteroid Sort game keep a dark scene, as Synthesis's Blaster does.
- **Lexend** everywhere, a typeface designed to make reading easier for early readers.
- **One colour language** (`js/core/theme.js`): ones blue, tens green, hundreds orange, thousands pink; red and yellow two-colour counters like the ones used in UK classrooms; bold flat fraction colours. All mission text was updated to match ("the green rods", "the red counters").
- **Sticker-style objects**: flat fills with crisp dark outlines, including all the space icons.
- **Tactile controls**: white keys with a solid bottom edge, a blue primary button, the blue Synthesis-style number pad, and a segmented progress bar like the Synthesis flash cards.
- **Quick Fire** redrawn as an outlined flash-card deck on a contour-line background.
- **Big Questions** moved onto the white surface as large cards, with the vote, the "why" and the reveal in the tutor panel.
- **Illustrated covers** (`js/core/covers.js`) for every sector and game replace the photographs, each showing the actual maths (Dienes blocks, a part-whole model, an array, a fraction circle, a clock and ruler, shapes, a bar chart). Each sector tile has a status chip (Not started, In progress, Complete) and a progress bar.
- **Fact Map** drawn as rings like the Synthesis fluency grid.

## Where Synthesis is still ahead

- It has a live AI tutor that converses; ours is scripted, with Dad as the conversational partner (a deliberate choice: no microphone, no unchecked AI text).
- Its widgets have some richer animation (dot clouds of a thousand dots, fluid regrouping). Ours animate, but more simply.
- It is tested on many children; ours has only been tested by automated play-throughs and screenshots so far.
