# Getting Astra Maths onto the tablet

## Where it lives

**https://philhandley.github.io/astra-maths/**

This folder is the GitHub repository `philhandley/astra-maths`, published by GitHub Pages from `main`. It has its own address outside Astra Finn, so the tablet installs it as its own app. (It used to live at `/astra-finn/maths/`, which now redirects here. Progress is kept: all the apps share the same site storage.)

## Updating it after a change

```bash
python tools/build_sw.py
```

```bash
git add -A && git commit -m "Update Astra Maths" && git push
```

GitHub Pages redeploys in about two minutes.

## Installing on the Samsung tablet

**Samsung Internet:** open the address, tap the menu (three lines, bottom right), then **Add page to**, then **Home screen**. If an **Install** icon appears in the address bar, tap that instead.

**Chrome:** open the address, tap the three-dot menu, then **Add to Home screen**, then **Install**.

Then:
- Open it once on Wi-Fi and tap into a mission, so everything is saved for offline use. After that it works with Wi-Fi off.
- Turn the tablet sideways. It is designed for landscape.
- Turn the volume up: Nova reads every line aloud. The speaker button in a mission's top bar switches automatic reading off.
- Sounds (blaster pews, chimes) are off by default. The music-note button in a mission's top bar turns them on.

## First session

1. Type the crew names (Finn and Dad).
2. Do the **Cadet Check** (about five minutes). It finds which Year 1 fundamentals are already solid and suggests where to start.
3. Fly the suggested mission, then one **Quick Fire** round.
4. Look at the **Fact Map** together and the patch on the wall.
