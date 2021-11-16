import os, json, requests
from types import resolve_bases
from dotenv import load_dotenv
from django.contrib.auth.models import User


load_dotenv()

# Fetching Scrip lists
COMPANY_URL = os.environ.get("COMPANY_URL")
try:
    response = requests.get(COMPANY_URL)
    details = response.json()
except:
    details = {}

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

# Getting IPO companies
IPO_URL = os.environ.get("IPO_URL")
try:
    response = requests.get(IPO_URL)
    data = response.json()
    companies = [(item.get("name"), item.get("name")) for item in data.get("body")]
    companies_id = {item.get("name"):item.get("id") for item in data.get("body")}
except:
    companies = []
    companies_id = {}

# Getting IPO result
def get_ipo_result(request, company):
    IPO_RES_URL = os.environ.get("IPO_RES_URL")
    result = {}
    
    boids = [int(demat.boid) for demat in request.user.demat_set.all()]
    for boid in boids:
        values = {
            "companyShareId": companies_id.get(company),
            "boid": boid
            }
        response = requests.post(
            IPO_RES_URL,
            json=values
        )
        data = response.json()
        result[boid] = data.get("message")
    return result
