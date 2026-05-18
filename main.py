import os
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from plaid.api import plaid_api
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

load_dotenv()

# Plaid client setup
config = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        "clientId": os.getenv("PLAID_CLIENT_ID"),
        "secret": os.getenv("PLAID_SECRET"),
    },
)
plaid_client = plaid_api.PlaidApi(ApiClient(config))

app = FastAPI()

# Allow your frontend to call this server (we'll need this for Week 3)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # default Vite dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "service": "trove-app"}


@app.post("/api/create_link_token")
def create_link_token():
    request = LinkTokenCreateRequest(
        products=[Products("transactions")],
        client_name="Trove",
        country_codes=[CountryCode("US")],
        language="en",
        user=LinkTokenCreateRequestUser(
            client_user_id="user-1"  # hardcoded for now; later this is your real user id
        ),
    )
    response = plaid_client.link_token_create(request)
    return {"link_token": response["link_token"]}

# This is the endpoint that Plaid link will call with a public token after the user successfully links their account.
@app.post("/api/exchange_public_token")
def exchange_public_token(body: dict):
    public_token = body["public_token"]
    request = ItemPublicTokenExchangeRequest(public_token=public_token)
    response = plaid_client.item_public_token_exchange(request)
    return {
        "access_token": response["access_token"],
        "item_id": response["item_id"],
    }