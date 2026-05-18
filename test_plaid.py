import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.configuration import Configuration
from plaid.api_client import ApiClient

load_dotenv()

print("CLIENT_ID:", os.getenv("PLAID_CLIENT_ID"))
print("SECRET:", os.getenv("PLAID_SECRET"))


config = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        "clientId": os.getenv("PLAID_CLIENT_ID"),
        "secret": os.getenv("PLAID_SECRET"),
    },
)
client = plaid_api.PlaidApi(ApiClient(config))

# Just confirm credentials work by listing institutions
from plaid.model.institutions_get_request import InstitutionsGetRequest
from plaid.model.country_code import CountryCode

req = InstitutionsGetRequest(count=5, offset=0, country_codes=[CountryCode("US")])
resp = client.institutions_get(req)
for inst in resp["institutions"]:
    print(inst["name"])