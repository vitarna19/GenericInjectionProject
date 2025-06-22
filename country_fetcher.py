import requests
import json
import os

COUNTRIES = ['india', 'us', 'uk', 'china', 'russia']
BASE_URL = "https://restcountries.com/v3.1/name/"

output_folder = "country_data"
os.makedirs(output_folder, exist_ok=True)

for country in COUNTRIES:
    url = BASE_URL + country
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{output_folder}/{country}.json", "w") as f:
            json.dump(response.json(), f, indent=2)
    else:
        print(f"Failed to fetch data for {country}")
