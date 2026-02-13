"""
Elefan pin code generation (code valable a partir de la prochaine heure pleine et pour une semaine)
Requires : Un fichier .env avec les variables (disponible dans le keepass elefan)
 - IGLOO_HOME_CLIENT_ID
 - IGLOO_HOME_CLIENT_SECRET
 Fonctionnement : 
 1. `uv run python elefan.py`
 1. Récuperer le code généré et venir le renseigner ici : https://membres.lelefan.org/codes/new
"""

import base64
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

IGLOO_HOME_OAUTH2_API_URL = "https://auth.igloohome.co/oauth2/token"
client_id = os.environ.get("IGLOO_HOME_CLIENT_ID")
client_secret = os.environ.get("IGLOO_HOME_CLIENT_SECRET")
encoded_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()


# Make the request
response = requests.post(
    IGLOO_HOME_OAUTH2_API_URL,
    headers={
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data={
        "grant_type": "client_credentials",
    }
)
access_token = response.json()["access_token"]

# Find device ID
response_device_id = requests.get(
    "https://api.igloodeveloper.co/igloohome/devices",
    headers={
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json, application/xml"
    }
)

device_id = response_device_id.json()["payload"][0]["deviceId"]
today = datetime.now() + timedelta(hours=1)
next_week = today + timedelta(days=7)

# Generate pin
response_generate_pin = requests.post(
    f"https://api.igloodeveloper.co/igloohome/devices/{device_id}/algopin/hourly",
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json, application/xml"
    },
    json={
        "variance": 1,
        "startDate": today.strftime("%Y-%m-%dT%H:00:00+01:00"),
        "endDate": next_week.strftime("%Y-%m-%dT%H:00:00+01:00"),
        "accessName": "Temporary Hebdo PIN API 2"
    }
)

print(response_generate_pin.json())
