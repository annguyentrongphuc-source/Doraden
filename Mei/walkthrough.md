# Mei — Alien Giữa Loài Người: Walkthrough

## What Was Built

A complete Ren'Py visual novel project retelling your high school drama from **Mai (Mei)'s perspective**. The original Vy-centric script has been fully adapted and massively expanded.

### Project Structure
```
e:\BUILD GAME\Mei\game\
├── script.rpy          — Main entry, narrator intro, chapter routing
├── options.rpy         — Game config (1920x1080)
├── characters.rpy      — 11 characters + 3-axis choice system + flags
├── chapter1.rpy        — Mặt Nạ Hoàn Hảo (6 choices)
├── chapter2.rpy        — Sau Lớp Vỏ (5+ choices, clone exploration)
├── chapter3.rpy        — Cỗ Máy Ảnh (5 choices)
├── chapter4.rpy        — Vỡ Mộng (7 choices)
├── chapter5.rpy        — Kết Nối (6 choices)
├── chapter6.rpy        — Alien Giữa Loài Người (4 choices)
├── chapter7.rpy        — Bình Minh — 7 endings + credits
├── images/README.md    — Sprite/BG naming guide
└── audio/README.md     — Music/SFX placement guide
```

### Stats
| Metric | Count |
|--------|-------|
| Script files | 10 |
| Total lines | ~2,900 |
| Player choices | 35+ |
| Endings | 7 |
| Chapters | 7 |
| Characters | 11 |

### Choice System — 3 Hidden Axes

| Variable | Tracks | Low | High |
|----------|--------|-----|------|
| `facade` | Mask attachment | Letting go | Doubling down |
| `empathy` | Connection with others | Isolation | Opening up |
| `self_worth` | Self-acceptance | Self-hatred | Accepting flaws |

### 7 Endings

| # | Name | Condition |
|---|------|-----------|
| 1 | **Maitopia Is Here** (True) | High empathy + self_worth, low facade |
| 2 | **Alien Learns to Land** (Bittersweet) | High empathy, mid self_worth |
| 3 | **Fortress Intact** (Loner) | High facade, low empathy |
| 4 | **Cracked Mirror** (Dark) | Low self_worth + empathy |
| 5 | **Better Than You** (Rival) | High facade + self_worth |
| 6 | **Old Soul & Ordinary Girl** (Bond) | Max Vy relationship |
| 7 | **Clone #10** (Secret) | All 5 clones explored + high empathy/self_worth |

## Next Steps for You

1. **Install Ren'Py SDK** — Download from [renpy.org](https://renpy.org). Point it at `e:\BUILD GAME\Mei\` as a project.
2. **Add sprites** — See [images/README.md](file:///e:/BUILD%20GAME/Mei/game/images/README.md) for exact filenames needed
3. **Add backgrounds** — 18 BG scenes listed in the guide
4. **Add music/SFX** — See [audio/README.md](file:///e:/BUILD%20GAME/Mei/game/audio/README.md)
5. **Playtest** — Launch from Ren'Py, play all 7 endings
6. **Polish** — Adjust dialogue, add `show`/`hide` sprite commands once art is ready
