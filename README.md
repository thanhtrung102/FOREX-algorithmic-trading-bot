# FOREX Algorithmic Trading Bot

A Python-based automated forex trading system featuring real-time price streaming, technical analysis, backtesting, and automated trade execution through the OANDA API.

## Verified Functionality Status

| Feature | Status | Notes |
|---------|--------|-------|
| OANDA API Integration | Working | Account access, candle fetching, trade execution |
| Technical Indicators | Working | RSI, MACD, Bollinger Bands, ATR, Keltner Channels |
| Candlestick Patterns | Working | 9 patterns detected (Hanging Man, Shooting Star, etc.) |
| Backtesting Engine | Working | GuruTester and GuruTesterFast frameworks |
| Historical Data Loading | Working | Pickle files with OHLC data for 60+ pairs |
| Instrument Collection | Working | JSON-based instrument definitions |
| Flask REST API | Working | Account, prices, technicals endpoints |
| Stream Bot Components | Working | Multi-threaded price processing architecture |
| MongoDB Integration | Requires Setup | Needs valid MongoDB Atlas connection |
| Web Scraping | Network Dependent | Reuters finance headlines (may be blocked) |

## Project Structure

```
FOREX-algorithmic-trading-bot/
|
|-- api/                          # OANDA API integration
|   |-- oanda_api.py              # Main API wrapper (candles, trades, account)
|   |-- stream_prices.py          # Price streaming functionality
|   +-- web_options.py            # Web API options
|
|-- bot/                          # Legacy single-threaded bot
|   |-- bot.py                    # Main Bot class
|   |-- candle_manager.py         # Candle timing management
|   |-- technicals_manager.py     # Technical analysis decisions
|   |-- trade_manager.py          # Trade execution
|   |-- trade_risk_calculator.py  # Risk calculations
|   +-- settings.json             # Trading pair configurations
|
|-- stream_bot/                   # Production multi-threaded bot
|   |-- stream_bot.py             # Main orchestrator
|   |-- price_processor.py        # Price update processing
|   |-- candle_worker.py          # Candle formation worker
|   |-- trade_worker.py           # Trade execution worker
|   +-- trade_settings_collection.py
|
|-- simulation/                   # Backtesting frameworks
|   |-- guru_tester.py            # Core backtesting engine
|   |-- ma_cross.py               # MA crossover strategy
|   |-- ema_macd.py               # EMA+MACD strategy
|   |-- ema_macd_mp.py            # Multiprocessing version
|   +-- ma_excel.py               # Excel export
|
|-- technicals/                   # Technical analysis library
|   |-- indicators.py             # RSI, MACD, BB, ATR, Keltner
|   +-- patterns.py               # Candlestick pattern detection
|
|-- models/                       # Data models
|   |-- api_price.py              # Price data structures
|   |-- trade_decision.py         # Trade decision model
|   |-- trade_settings.py         # Trading settings
|   |-- open_trade.py             # Open trade tracking
|   |-- instrument.py             # Instrument definitions
|   +-- candle_timing.py          # Candle timing utilities
|
|-- infrastructure/               # Data & utilities
|   |-- collect_data.py           # Historical data collection
|   |-- instrument_collection.py  # Instrument management
|   +-- log_wrapper.py            # Logging utilities
|
|-- scraping/                     # Web scraping (network dependent)
|   |-- bloomberg_com.py          # Reuters finance headlines
|   |-- investing_com.py          # Technical analysis data
|   |-- dailyfx_com.py            # DailyFX data
|   |-- my_fx_book.py             # MyFXBook data
|   +-- fx_calendar.py            # Economic calendar
|
|-- db/                           # Database layer
|   +-- db.py                     # MongoDB integration
|
|-- constants/
|   +-- defs.py                   # API credentials, constants
|
|-- data/                         # Historical data storage
|   |-- instruments.json          # Instrument definitions
|   +-- *.pkl                     # Cached candle data
|
|-- exploration/                  # Jupyter notebooks
|
|-- main.py                       # Development/testing entry point
|-- run_bot.py                    # Production bot launcher
|-- server.py                     # Flask REST API server
|-- guru_tester_fast.py           # Optimized backtesting
+-- requirements.txt              # Python dependencies
```

## Installation

### Prerequisites

- Python 3.8+ (tested with 3.11)
- OANDA Practice or Live trading account
- (Optional) MongoDB Atlas account for database features

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/thanhtrung102/FOREX-algorithmic-trading-bot.git
   cd FOREX-algorithmic-trading-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure credentials**

   Edit `constants/defs.py`:
   ```python
   API_KEY = "your-oanda-api-key"
   ACCOUNT_ID = "your-account-id"
   OANDA_URL = "https://api-fxpractice.oanda.com/v3"  # or api-fxtrade for live
   ```

   **Security Note**: Move credentials to environment variables for production use.

## Usage

### 1. Development Testing

```bash
python main.py
```

The `main.py` file contains test functions for each component. Uncomment the function you want to run:

```python
test_api_connection()      # Test OANDA connectivity
test_fetch_candles()       # Fetch sample candle data
test_technical_indicators() # Test indicator calculations
test_backtesting()         # Run a sample backtest
```

### 2. Production Trading Bot

```bash
python run_bot.py
```

This launches the multi-threaded streaming bot with:
- Real-time price streaming from OANDA
- Concurrent price processing per trading pair
- Automated candle formation and trade execution

### 3. Flask REST API

```bash
python server.py
```

Access at `http://localhost:5000`

**Endpoints:**
- `GET /api/test` - Health check
- `GET /api/account` - OANDA account summary
- `GET /api/prices/<pair>/<granularity>/<count>` - Price data
- `GET /api/technicals/<pair>/<timeframe>` - Technical analysis (requires network access)
- `GET /api/headlines` - Financial news (requires network access)

### 4. Backtesting

```python
import pandas as pd
from guru_tester_fast import GuruTesterFast, BUY, SELL, NONE
from technicals.indicators import RSI

# Load data
df_h1 = pd.read_pickle("./data/EUR_USD_H1.pkl")
df_m5 = pd.read_pickle("./data/EUR_USD_M5.pkl")

# Apply indicator
df_h1 = RSI(df_h1.copy())

# Define signal function
def rsi_signal(row):
    if row.RSI_14 < 30:
        return BUY
    elif row.RSI_14 > 70:
        return SELL
    return NONE

# Run backtest
tester = GuruTesterFast(
    df_big=df_h1,
    apply_signal=rsi_signal,
    df_m5=df_m5,
    PROFIT_FACTOR=1.5,
    LOSS_FACTOR=-1.0
)
tester.run_test()

print(f"Total trades: {len(tester.df_results)}")
print(f"Total result: {tester.df_results.result.sum():.2f}")
```

## Technical Indicators

All indicators are in `technicals/indicators.py`:

```python
from technicals.indicators import BollingerBands, RSI, MACD, ATR, KeltnerChannels

# Apply to DataFrame (requires mid_c, mid_h, mid_l columns)
df = BollingerBands(df, n=20, s=2)   # Adds: BB_MA, BB_UP, BB_LW
df = RSI(df, n=14)                    # Adds: RSI_14
df = MACD(df)                         # Adds: MACD, SIGNAL, HIST
df = ATR(df, n=14)                    # Adds: ATR_14
df = KeltnerChannels(df)              # Adds: EMA, KeUp, KeLo
```

## Candlestick Patterns

Available patterns in `technicals/patterns.py`:

```python
from technicals.patterns import apply_patterns

df_with_patterns = apply_patterns(df)
# Adds columns: HANGING_MAN, SHOOTING_STAR, SPINNING_TOP, MARUBOZU,
#               ENGULFING, TWEEZER_TOP, TWEEZER_BOTTOM, MORNING_STAR, EVENING_STAR
```

## Bot Configuration

Edit `bot/settings.json`:

```json
{
  "trade_risk": 10,
  "pairs": {
    "EUR_USD": {
      "n_ma": 12,
      "n_std": 2.5,
      "maxspread": 0.0004,
      "mingain": 0.0006,
      "riskreward": 1.5
    }
  }
}
```

**Parameters:**
- `trade_risk`: Risk amount per trade
- `n_ma`: Bollinger Bands period
- `n_std`: Standard deviation multiplier
- `maxspread`: Maximum allowed spread to enter trade
- `mingain`: Minimum gain threshold
- `riskreward`: Risk-reward ratio for TP/SL

## Historical Data

Pre-loaded data for 60+ currency pairs across three timeframes:
- M5 (5-minute)
- H1 (1-hour)
- H4 (4-hour)

**Available pairs include:**
EUR_USD, GBP_USD, AUD_USD, USD_JPY, EUR_GBP, EUR_JPY, GBP_JPY, AUD_JPY, and more.

To collect fresh data:
```python
from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from infrastructure.collect_data import run_collection

instrumentCollection.LoadInstruments("./data")
api = OandaApi()
run_collection(instrumentCollection, api)
```

## Architecture

### Multi-threaded Stream Bot

The production bot (`stream_bot/`) uses a producer-consumer pattern:

1. **PriceStreamer**: Connects to OANDA streaming API, pushes price updates to queues
2. **PriceProcessor** (per pair): Processes incoming prices, manages candle formation
3. **CandleWorker** (per pair): Handles candle completion events, generates signals
4. **TradeWorker**: Executes trades based on signals from all pairs

### Backtesting Framework

The `GuruTesterFast` class provides efficient backtesting:
1. Apply indicators to the larger timeframe DataFrame
2. Define a signal function returning BUY (1), SELL (-1), or NONE (0)
3. The tester merges signals with M5 data to simulate trade execution
4. Results include entry/exit times, prices, and profit/loss factors

## Known Limitations

1. **Web Scraping**: Reuters/Investing.com scraping may be blocked by firewalls or rate limiting
2. **MongoDB**: Requires a valid MongoDB Atlas connection string for database features
3. **OANDA API**: Currently configured for practice account; change URL for live trading
4. **Backtesting**: Does not account for slippage or partial fills

## Security Warning

The `constants/defs.py` file contains hardcoded credentials. For production:

```python
import os

API_KEY = os.getenv('OANDA_API_KEY')
ACCOUNT_ID = os.getenv('OANDA_ACCOUNT_ID')
MONGO_CONN_STR = os.getenv('MONGO_CONNECTION_STRING')
```

Create a `.env` file (add to `.gitignore`):
```
OANDA_API_KEY=your_key_here
OANDA_ACCOUNT_ID=your_account_id
MONGO_CONNECTION_STRING=your_mongo_uri
```

## Risk Disclaimer

**This software is for educational and research purposes only.**

- Forex trading involves substantial risk of loss
- Past performance does not guarantee future results
- The developers accept no liability for financial losses
- Always test thoroughly in a demo environment before live trading
- Never trade with money you cannot afford to lose

## Dependencies

- pandas >= 2.0.0
- numpy >= 1.24.0
- requests >= 2.28.0
- Flask >= 2.3.0
- flask-cors >= 4.0.0
- pymongo >= 4.0.0
- python-dateutil >= 2.8.0
- openpyxl >= 3.1.0
- cloudscraper >= 1.2.60
- beautifulsoup4 >= 4.12.0

## License

MIT License

## Author

**thanhtrung102** - [GitHub](https://github.com/thanhtrung102)
