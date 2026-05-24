# SastaSentinels

> Seven friends. One squad. Zero mercy.

Official website for **SastaSentinels** — an elite esports squad competing in Valorant, CS2, and Apex Legends.

---

## Stack

| Layer    | Technology                                      |
| -------- | ----------------------------------------------- |
| Backend  | [FastHTML](https://fastht.ml) (Python)          |
| Styling  | Custom CSS (Space Grotesk + Orbitron)           |
| Hosting  | [Vercel](https://vercel.com) (FastHTML preset)  |
| Runtime  | Python 3.12 via `uv`                            |

---

## Features

- Splash screen with animated HUD
- Particle canvas hero section with parallax
- Player roster with 3D card tilt
- Match history log
- Games arsenal (FPS + story)
- Highlights section with YouTube links
- Animated stats counter
- Sound effects toggle
- Vercel Web Analytics + Speed Insights

---

## Local Development

```bash
# Clone
git clone https://github.com/nikharmsingh/sastasentinels.git
cd sastasentinels

# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run dev server
python main.py
```

Open [http://localhost:8000](http://localhost:8000).

---

## Project Structure

```
sastasentinels/
├── main.py          # FastHTML app — all routes and components
├── static/
│   ├── style.css    # Full site styles (~1400 lines)
│   └── script.js    # Client-side interactivity
├── requirements.txt
└── vercel.json      # Vercel rewrites and security headers
```

---

## Deployment

Deployed automatically on every push to `main` via Vercel's GitHub integration.

The `vercel.json` catch-all rewrite routes all requests through the FastHTML ASGI app, which is wrapped with [Mangum](https://github.com/jordaneremieff/mangum) for serverless compatibility.

---

## Squad

| IGN           | Role                  |
| ------------- | --------------------- |
| BeastM0del    | Carry · Top Fragger   |
| WizVoltric    | Co-IGL · Rifler       |
| GreyWolf      | Head IGL · Strategist |
| KINGPIN       | Entry Fragger         |
| Sectumsempra  | AWPer · Sniper        |
| AgentTrigger  | Support · Clutch      |
| STING         | Sentinel · Anchor     |

---

© 2025 SastaSentinels · All Rights Reserved
