import os, json, requests
from dotenv import load_dotenv


load_dotenv()

# Fetching Scrip lists
COMPANY_URL = os.environ.get("COMPANY_URL")
try:
    response = requests.get(COMPANY_URL)
    details = response.json()
except:
    with open("companies.json") as f:
        data = f.read()
        details = json.loads(data)

details = sorted(details, key=lambda d: d['Stock Symbol'])
scrips = [(i["Stock Symbol"], i["Stock Symbol"]) for i in details]
company_scrip = {i["Stock Name"]:i["Stock Symbol"] for i in details}

# Getting Share details
NEPSE_URL = os.environ.get("NEPSE_URL")
share_data = {}
try:
    response = requests.get(NEPSE_URL)
    data = response.json()
    for item in data:
        share_data[company_scrip.get(item.get("Traded Companies"))] = item
except:
    share_data = {}