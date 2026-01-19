# Osu! Reco

Osu! Reco is an open-source desktop application that recommends ranked osu! beatmaps based on a player’s global rank and selected game mode.

Instead of relying on a simple logarithmic approximation, the application uses a custom piecewise difficulty model designed to better reflect real player progression. Beatmaps are fetched directly from the official osu! API v2 and displayed in a clean, card-based interface with cover images.

---

## Features

- Rank-based difficulty recommendation using a custom piecewise model
- Supports all osu! game modes:
  - osu!
  - Taiko
  - Catch the Beat
  - osu!mania
- Live beatmap search via the official osu! API v2
- Card-based UI with beatmap covers
- Select beatmaps inside the app and open them in the browser
- Guardrails to prevent excessive API calls and UI freezes
- Custom dark theme using CustomTkinter
- Cross-platform (Windows, macOS, Linux)
- Fully open-source

---

## Requirements

- Python 3.10 or newer
- Internet connection (required for osu! API and cover images)
- Windows, macOS, or Linux

---

## Project Structure

```text
osu-reco/
├── main.py               # Main application and UI logic
├── osu_auth.py           # osu! OAuth token handling
├── osu_pink.json         # CustomTkinter theme
├── config.example.json   # Safe configuration template
├── requirements.txt      # Python dependencies
├── README.md
├── osu_reco.ico          # Application icon
└── .gitignore

Installation and Setup
Step 1: Clone the repository
git clone https://github.com/yourusername/osu-reco.git
cd osu-reco

Step 2: Create a virtual environment (recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

Step 3: Install dependencies
pip install -r requirements.txt

osu! API Setup (Required)

This application uses the official osu! API v2 and requires OAuth credentials.

Step 4: Create an osu! OAuth application

Log in to your osu! account

Go to: https://osu.ppy.sh/home/account/edit

Scroll to the OAuth Applications section

Create a new application

Set the application type to Confidential

The redirect URL is not used and can be set to any valid URL

You will receive:

Client ID

Client Secret

Step 5: Create your local config file

Copy the example configuration file:

cp config.example.json config.json


Open config.json and insert your credentials:

{
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "access_token": "",
    "token_expiry": 0
}


Important:

config.json must NOT be committed

It is ignored automatically via .gitignore

Running the Application

From the project directory, with your virtual environment activated:

python main.py


The application window should open.

How the Application Works

Enter your global osu! rank manually

Select the desired game mode

The app converts your rank into a recommended star difficulty range

Ranked beatmaps are fetched from the osu! API within that range

Results are displayed as selectable cards

Select a beatmap and click “Open Selected Map in Browser” to view it on osu!

The difficulty model is intentionally piecewise to avoid unrealistic jumps in difficulty and better match real player experience.

Security Notes

config.json is excluded from version control

OAuth access tokens are stored locally only

No user data is collected or transmitted beyond osu! API requests

Known Limitations

Rank must current
