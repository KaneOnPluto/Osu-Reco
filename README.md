# Osu! Reco

Osu! Reco is an open-source desktop application that recommends ranked osu! beatmaps based on a player's global rank and selected game mode.

Instead of relying on generic difficulty guesses, the app uses a custom, piecewise difficulty model designed to match real player progression. It then fetches relevant ranked beatmaps directly from the official osu! API and presents them in a clean, card-based interface.

---

## Features

- Rank-based difficulty recommendation using a custom piecewise model
- Supports all osu! game modes:
  - osu!
  - Taiko
  - Catch the Beat
  - osu!mania
- Live beatmap search via osu! API v2
- Clean, card-based UI with beatmap covers
- Click-to-select maps and open them in the browser
- Guardrails to prevent API abuse and UI freezes
- Fully offline-safe except for API calls
- Open-source and easily extensible

---

## Screenshots

(Add screenshots here once you upload them)

---

## Requirements

- Python 3.10 or newer
- Internet connection (for osu! API and cover images)
- Windows, macOS, or Linux

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/osu-reco.git
cd osu-reco
