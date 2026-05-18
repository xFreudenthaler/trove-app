# Trove

A personal finance dashboard. Connects to bank accounts via Plaid, categorizes transactions, and surfaces spending patterns and recurring subscriptions.

## Local setup

### Prerequisites
- Python 3.12+
- A Plaid developer account with Sandbox keys

### Setup
1. Clone the repo: `git clone <url> && cd trove-app`
2. Create a virtual env: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your Plaid keys
5. Run the server: `uvicorn main:app --reload`
6. Verify it works: `curl -X POST http://127.0.0.1:8000/api/create_link_token`

## Project status
Work in progress. Built as a personal project to learn FastAPI, Plaid integration, and React.
