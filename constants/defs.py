API_KEY = "dc6b098a0c20ab9673b63f8ad72b81d7-758b1a37d2ef19d1eb3510cc195802b6"
ACCOUNT_ID = "101-001-31068424-001"
OANDA_URL = "https://api-fxpractice.oanda.com/v3"

SECURE_HEADER = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SELL = -1
BUY = 1
NONE = 0

MONGO_CONN_STR = "mongodb+srv://admin:13122003abc@cluster0.oyqmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Timeframe mappings for investing.com API (seconds)
TFS = {
    'M1': 60,
    'M5': 300,
    'M15': 900,
    'M30': 1800,
    'H1': 3600,
    'H4': 14400,
    'D': 86400,
    'W': 604800,
}

# Investing.com pair IDs for scraping
INVESTING_COM_PAIRS = {
    'EUR_USD': {'pair_id': 1},
    'GBP_USD': {'pair_id': 2},
    'USD_JPY': {'pair_id': 3},
    'USD_CHF': {'pair_id': 4},
    'AUD_USD': {'pair_id': 5},
    'USD_CAD': {'pair_id': 7},
    'NZD_USD': {'pair_id': 8},
    'EUR_GBP': {'pair_id': 6},
    'EUR_JPY': {'pair_id': 9},
    'GBP_JPY': {'pair_id': 10},
    'EUR_CHF': {'pair_id': 11},
}
