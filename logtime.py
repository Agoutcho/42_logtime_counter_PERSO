#! /bin/python3
import json
import requests
import datetime
from dateutil import parser

def get_access_token(config):
    url = "https://api.intra.42.fr/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": config["client_id"],
        "client_secret": config["client_secret"]
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        # Update the config file with the new access_token
        config["access_token"] = access_token
        with open('config.json', 'w') as f:
            json.dump(config, f)
        return access_token
    else:
        print("Error: ", response.json())
        return None

def get_location_stats(config, access_token):
    url = f"https://api.intra.42.fr/v2/users/{config['username']}/locations_stats"
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Use current month if begin_at and end_at are not provided
    if "begin_at" not in config or "end_at" not in config:
        now = datetime.now()
        config["begin_at"] = now.strftime("%Y-%m-01")
        config["end_at"] = now.strftime("%Y-%m-%d")

    params = {
        "begin_at": config["begin_at"],
        "end_at": config["end_at"]
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: ", response.json())
        return None

def calculate_total_time(data):
    hours_per_day = {}
    min_per_day = {}
    for date, time in data.items():
        if time != "24:00:00":
            hours = datetime.datetime.strptime(time, "%H:%M:%S.%f").hour
            min = datetime.datetime.strptime(time, "%H:%M:%S.%f").minute
        else:
            hours = 24
            min = 0
        hours_per_day[date] = hours
        min_per_day[date] = min
        print(f"Date : {date} | {hours} | {min}")
    total_hours = sum(hours_per_day.values()) + (sum(min_per_day.values()) / 60)
    return total_hours

print("LOGTIME counter")

with open('config.json') as f:
    config = json.load(f)

access_token = config.get('access_token', None)
if access_token is None:
    access_token = get_access_token(config)
    print("Access token : ", access_token)
if access_token is None:
    print("Change your API ID")
else:
    location_stats = get_location_stats(config, access_token)
    total_time = calculate_total_time(location_stats)
    print("Total time spent connected: ", total_time)

