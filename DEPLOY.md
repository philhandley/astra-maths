# Getting Astra Maths onto the tablet

## Where it lives

Astra Maths is published inside the Astra Finn GitHub Pages site, in its own folder, so it has its own address, its own home-screen icon and its own offline copy:

**https://philhandley.github.io/astra-finn/maths/**

The source of truth is this folder (`C:\1. Astra Nova Synthesis  - Maths Tutor`, its own git repository). Publishing copies the app files into `C:\1 Astra Nova - Finn\maths\` and pushes that repository.

## Updating it after a change

From this folder:

```bash
python tools/build_sw.py
```

```bash
python tools/publish.py "C:/1 Astra Nova - Finn/maths"
```

Then in `C:\1 Astra Nova - Finn`:

```bash
git add maths && git commit -m "Update Astra Maths" && git push
```

GitHub Pages redeploys in about two minutes.

## Moving it to its own address later (optional)

If you would rather have `https://philhandley.github.io/astra-maths/`:

1. On github.com, create a new **public** repository called `astra-maths` with every "Initialize" box unticked.
2. In this folder run:

```bash
git remote add origin https://github.com/philhandley/astra-maths.git
```

```bash
git push -u origin main
```

3. On GitHub: Settings, Pages, Source "Deploy from a branch", branch `main`, folder `/ (root)`, Save.

Progress is stored per address in the tablet's browser, so moving address starts the patches afresh.

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
