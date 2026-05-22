# Trove

A personal finance dashboard. Connects to bank accounts via Plaid, categorizes transactions, and surfaces spending patterns and recurring subscriptions.

## Local setup

### Prerequisites
- Python 3.12 or newer (tested on 3.14)
- Node.js 18 or newer (for the frontend)
- A Plaid developer account with Sandbox keys

### Backend setup
1. Clone the repo: `git clone <url> && cd trove-app`
2. Create a virtual env: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your Plaid keys
5. Run the server: `uvicorn main:app --reload`
6. Verify it works: `curl -X POST http://127.0.0.1:8000/api/create_link_token`

### Frontend setup
Open a new terminal in the project root, then:
1. `cd frontend`
2. `npm install`
3. `npm run dev`
4. Open http://localhost:5173 in your browser

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| POST | `/api/create_link_token` | Creates a Plaid Link token for the frontend to initialize Plaid Link |
| POST | `/api/exchange_public_token` | Exchanges a Plaid public token for an access token after the user successfully links their account |

## Project status
Work in progress. Built as a personal project to learn FastAPI, Plaid integration, and React.
