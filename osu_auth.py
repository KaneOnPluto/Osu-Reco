# osu_auth.py
import requests
import time
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

TOKEN_URL = "https://osu.ppy.sh/oauth/token"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)


def get_access_token():
    config = load_config()

    if config.get("access_token") and time.time() < config.get("token_expiry", 0):
        return config["access_token"]

    payload = {
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
        "grant_type": "client_credentials",
        "scope": "public",
    }

    response = requests.post(TOKEN_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    config["access_token"] = data["access_token"]
    config["token_expiry"] = time.time() + data["expires_in"] - 60

    save_config(config)
    return config["access_token"]
