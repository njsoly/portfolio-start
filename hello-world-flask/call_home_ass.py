import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load secrets from a file outside the repo (chmod 600).
# Falls back to a local .env (gitignored) if the user-level one isn't there.
SECRETS_PATH = Path.home() / ".config" / "home-ass.env"
if SECRETS_PATH.is_file():
    load_dotenv(SECRETS_PATH)
else:
    load_dotenv()  # looks for ./.env

try:
    TOKEN = os.environ["HA_LLAT"]
except KeyError as e:
    raise SystemExit(
        f"Missing env var {e.args[0]}. "
        f"Set it in {SECRETS_PATH} or a local .env file."
    )

BASE_URL = os.environ.get("HA_BASE_URL", "http://njsoly-raz5-ha:8123")

url = f"{BASE_URL}/api/"
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

print(response.text)
