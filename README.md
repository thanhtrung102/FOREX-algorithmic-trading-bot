# FOREX Algorithmic Trading Bot

A comprehensive automated forex trading system built with Python, featuring backtesting capabilities, technical analysis, real-time data streaming, and automated trade execution through the OANDA API.

## 🌟 Features

### Core Functionality
- **Automated Trading Bot**: Multi-threaded bot with candle and trade workers for real-time execution
- **Backtesting Engine**: GuruTester framework for strategy validation on historical data
- **Real-time Streaming**: Asynchronous price streaming with event-driven architecture
- **Risk Management**: Configurable risk-reward ratios, stop-loss, and take-profit levels

### Technical Analysis
- **Technical Indicators**: RSI, MACD, Bollinger Bands, Keltner Channels, ATR, Moving Averages (SMA/EMA)
- **Candlestick Patterns**: Detection of Hanging Man, Shooting Star, Spinning Top, Marubozu, Engulfing, Tweezer Top/Bottom, Morning/Evening Star
- **Strategy Simulation**: MA crossover, EMA+MACD combinations with multiprocessing support

### Data Management
- **OANDA API Integration**: Real-time price feeds, account management, and trade execution
- **MongoDB Database**: Store instruments, historical data, and trading results
- **Pickle Data Storage**: Cached historical candle data for quick backtesting (M5, H1, H4 timeframes)

### Web Interface & Scraping
- **Flask REST API**: Endpoints for account info, prices, technical analysis, and headlines
- **Market News Scraping**: Bloomberg, DailyFX, Investing.com, MyFXBook integration
- **Economic Calendar**: Forex calendar data collection

### Analysis Tools
- **Jupyter Notebooks**: Strategy development and visualization
- **Performance Tracking**: Comprehensive logging and result analysis in Excel format

## 📁 Project Structure

```
FOREX-algorithmic-trading-bot/
├── api/                          # OANDA API integration
│   ├── oanda_api.py             # Main API wrapper for OANDA
│   ├── stream_prices.py         # Price streaming functionality
│   └── web_options.py           # Web API options
│
├── bot/                          # Core trading bot
│   ├── bot.py                   # Main Bot class with execution loop
│   ├── candle_manager.py        # Manages candle timing and updates
│   ├── technicals_manager.py   # Technical analysis and trade decisions
│   ├── trade_manager.py         # Trade execution and management
│   ├── trade_risk_calculator.py # Risk calculation utilities
│   └── settings.json            # Bot configuration (pairs, risk params)
│
├── stream_bot/                   # Multi-threaded streaming bot
│   ├── stream_bot.py            # Main orchestrator with threading
│   ├── price_processor.py       # Process incoming price data
│   ├── candle_worker.py         # Worker for candle management
│   ├── trade_worker.py          # Worker for trade execution
│   └── trade_settings_collection.py
│
├── simulation/                   # Backtesting frameworks
│   ├── guru_tester.py           # Core backtesting engine
│   ├── ma_cross.py              # MA crossover strategy simulator
│   ├── ema_macd.py              # EMA+MACD strategy
│   ├── ema_macd_mp.py           # Multi-processing version
│   └── ma_excel.py              # Export results to Excel
│
├── technicals/                   # Technical analysis library
│   ├── indicators.py            # RSI, MACD, Bollinger Bands, Keltner, ATR
│   └── patterns.py              # Candlestick pattern detection
│
├── models/                       # Data models
│   ├── api_price.py             # API price data structures
│   ├── trade_decision.py        # Trade decision model
│   ├── trade_settings.py        # Trading pair settings
│   ├── open_trade.py            # Open trade tracking
│   ├── instrument.py            # Instrument definitions
│   └── candle_timing.py         # Candle timing utilities
│
├── db/                           # Database layer
│   └── db.py                    # MongoDB integration (instruments, calendar)
│
├── scraping/                     # Web scraping modules
│   ├── bloomberg_com.py         # Bloomberg headlines
│   ├── dailyfx_com.py           # DailyFX data
│   ├── investing_com.py         # Investing.com technicals
│   ├── my_fx_book.py            # MyFXBook data
│   └── fx_calendar.py           # Economic calendar
│
├── infrastructure/               # Data collection & utilities
│   ├── collect_data.py          # Historical data collection
│   ├── instrument_collection.py # Instrument management
│   └── log_wrapper.py           # Logging utilities
│
├── exploration/                  # Jupyter notebooks
│   ├── Guru_1_EMA200_RSI_Over50.ipynb
│   ├── Guru_2_MACD_EMA100.ipynb
│   ├── MA_Cross_An.ipynb
│   ├── Indicators.ipynb
│   └── candle_patterns.ipynb
│
├── data/                         # Historical data (pickle files)
│   ├── instruments.json         # Trading instruments
│   └── *.pkl                    # Cached candle data (M5, H1, H4)
│
├── main.py                       # Development/testing entry point
├── run_bot.py                    # Production bot launcher
├── server.py                     # Flask REST API server
├── guru_tester_fast.py          # Fast backtesting script
├── plotting_candles.ipynb       # Candlestick visualization
└── MA_Cross_Overforecast.ipynb  # MA crossover analysis
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** (developed with Python 3.12/3.13)
- **OANDA Account**: Practice or live trading account
- **MongoDB Atlas** (optional): For database features
- **Dependencies**: pandas, requests, Flask, pymongo, python-dateutil, openpyxl

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/thanhtrung102/FOREX-algorithmic-trading-bot.git
   cd FOREX-algorithmic-trading-bot
   ```

2. **Set up virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate (Windows)
   venv\Scripts\activate

   # Activate (Linux/Mac)
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install pandas requests Flask flask-cors pymongo python-dateutil openpyxl
   ```

4. **Configure API credentials**

   Edit `constants/defs.py` with your credentials:
   ```python
   API_KEY = "your-oanda-api-key"
   ACCOUNT_ID = "your-account-id"
   OANDA_URL = "https://api-fxpractice.oanda.com/v3"  # Practice account
   MONGO_CONN_STR = "your-mongodb-connection-string"  # Optional
   ```

   **SECURITY WARNING**: The current `defs.py` contains hardcoded credentials. For production:
   - Move credentials to environment variables or a `.env` file
   - Add `.env` to `.gitignore`
   - Never commit sensitive credentials to version control

### Running the Bot

**1. Production Trading Bot (Multi-threaded Streaming)**
```bash
python run_bot.py
```
This launches the stream_bot with price processors, candle workers, and trade workers running in parallel threads.

**2. Simple Bot (Legacy)**
```bash
# Uncomment the Bot import and run() call in run_bot.py first
python run_bot.py
```

**3. Flask REST API Server**
```bash
python server.py
```
Access at `http://localhost:5000`

Available endpoints:
- `GET /api/test` - Test endpoint
- `GET /api/account` - OANDA account summary
- `GET /api/headlines` - Bloomberg headlines
- `GET /api/options` - Trading options
- `GET /api/technicals/<pair>/<timeframe>` - Technical analysis
- `GET /api/prices/<pair>/<granularity>/<count>` - Price data

**4. Run Backtesting**
```bash
python guru_tester_fast.py
```

**5. Development & Testing**
```bash
python main.py  # Various testing functions
python tester.py  # General tests
python api_tests.py  # API tests
python scraping_tests.py  # Scraping tests
```

## 📊 Strategy Development

### Bot Configuration

Edit `bot/settings.json` to configure trading pairs and parameters:
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

### Backtesting with GuruTester

The `GuruTester` class provides comprehensive backtesting:

```python
from simulation.guru_tester import GuruTester
import pandas as pd

# Load historical data
df_h1 = pd.read_pickle("data/EUR_USD_H1.pkl")
df_m5 = pd.read_pickle("data/EUR_USD_M5.pkl")

# Define signal function
def my_signal(row):
    # Return BUY (1), SELL (-1), or NONE (0)
    return 0

# Run backtest
tester = GuruTester(
    df_big=df_h1,
    apply_signal=my_signal,
    df_m5=df_m5,
    PROFIT_FACTOR=1.5,
    LOSS_FACTOR=-1.0,
    use_spread=True
)
tester.run_test()
print(tester.df_results.result.sum())
```

### Backtesting Results

Pre-computed simulation results:
- `ma_sim_M5.xlsx` - 5-minute MA crossover results
- `ma_sim_H1.xlsx` - 1-hour MA crossover results
- `ma_sim_H4.xlsx` - 4-hour MA crossover results

### Jupyter Notebook Analysis

```bash
jupyter notebook
```

Key notebooks in `exploration/`:
- `Guru_1_EMA200_RSI_Over50.ipynb` - EMA200 + RSI>50 strategy
- `Guru_2_MACD_EMA100.ipynb` - MACD + EMA100 strategy
- `MA_Cross_An.ipynb` - MA crossover analysis
- `Indicators.ipynb` - Technical indicator testing
- `candle_patterns.ipynb` - Candlestick pattern analysis
- `plotting_candles.ipynb` - Visualization tools

## 🛠️ Architecture & Components

### Multi-threaded Streaming Bot

The `stream_bot` uses a producer-consumer pattern with threading:

1. **PriceStreamer**: Fetches live prices from OANDA streaming API
2. **PriceProcessor**: Processes price updates for each pair (separate thread per pair)
3. **CandleWorker**: Manages candle formation and timing
4. **TradeWorker**: Executes trades based on signals

### Technical Indicators (technicals/indicators.py)

Available indicators:
```python
BollingerBands(df, n=20, s=2)
KeltnerChannels(df, n_ema=20, n_atr=10)
RSI(df, n=14)
MACD(df, n_slow=26, n_fast=12, n_signal=9)
ATR(df, n=14)
```

### Candlestick Patterns (technicals/patterns.py)

Pattern detection:
- Hanging Man, Shooting Star, Spinning Top
- Marubozu, Engulfing (Bullish/Bearish)
- Tweezer Top/Bottom
- Morning Star, Evening Star

### Data Collection

Collect historical data from OANDA:
```python
from infrastructure.collect_data import run_collection
from infrastructure.instrument_collection import instrumentCollection
from api.oanda_api import OandaApi

instrumentCollection.LoadInstruments("./data")
api = OandaApi()
run_collection(instrumentCollection, api)
```

## 🔧 Configuration Files

### constants/defs.py
Core configuration:
- `API_KEY`: OANDA API key
- `ACCOUNT_ID`: OANDA account ID
- `OANDA_URL`: API endpoint (practice/live)
- `MONGO_CONN_STR`: MongoDB connection string
- `BUY`, `SELL`, `NONE`: Trade direction constants

### bot/settings.json
Trading parameters per pair:
- `n_ma`: Moving average period
- `n_std`: Standard deviation multiplier
- `maxspread`: Maximum allowed spread
- `mingain`: Minimum gain threshold
- `riskreward`: Risk-reward ratio

### data/instruments.json
Available trading instruments with pip locations and display precision

## 💾 Database Integration

### MongoDB Collections (db/db.py)

The `DataDB` class manages three collections:
- `forex_instruments`: Trading instrument definitions
- `forex_calendar`: Economic calendar events
- `forex_sample`: Sample/test data

Example usage:
```python
from db.db import DataDB

db = DataDB()
db.test_connection()
instruments = db.query_distinct(DataDB.INSTRUMENTS_COLL, 'name')
db.add_one(DataDB.CALENDAR_COLL, {'event': 'NFP', 'date': '2024-01-05'})
```

## 📝 Logging

The bot uses a custom `LogWrapper` (infrastructure/log_wrapper.py) for comprehensive logging:

- **Per-pair logs**: Each trading pair gets a dedicated log file
- **Main log**: Overall bot activity
- **Error log**: Exceptions and crashes
- **Location**: `logs/` directory

All logs include timestamps and are formatted for debugging and performance analysis.

## 🌐 Web Scraping

Scraping modules for market sentiment and news:

### Bloomberg (scraping/bloomberg_com.py)
```python
from scraping.bloomberg_com import bloomberg_com
headlines = bloomberg_com()
```

### Investing.com Technical Analysis (scraping/investing_com.py)
```python
from scraping.investing_com import get_pair
technicals = get_pair("EUR_USD", "H1")
```

### Economic Calendar (scraping/fx_calendar.py)
Fetches forex economic calendar events

## 🧪 Testing

```bash
# Test API connectivity
python api_tests.py

# Test web scraping modules
python scraping_tests.py

# General functionality tests
python tester.py

# Apply strategies to data
python apply_code.py
```

## 🚨 Important Security Notes

### Current Security Issues

1. **Hardcoded Credentials**: The `constants/defs.py` file contains hardcoded API keys and MongoDB connection strings
   - **ACTION REQUIRED**: Replace with environment variables before production use
   - Add `constants/defs.py` to `.gitignore` or create a `defs_template.py`

2. **Exposed Secrets**: This repository may have committed sensitive credentials
   - **ACTION REQUIRED**: Rotate all API keys and database passwords
   - Review git history and consider using tools like `git-filter-repo` to remove secrets

### Recommended Security Practices

```python
# Use environment variables instead
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

## ⚠️ Risk Disclaimer

**IMPORTANT: READ BEFORE USE**

- This software is for **educational and research purposes only**
- Forex trading carries **substantial risk of loss** and may not be suitable for all investors
- **Past performance is not indicative of future results**
- The developers provide **no warranty** and accept **no liability** for financial losses
- **Always test strategies extensively** in a demo/practice environment before live trading
- **Never trade with money you cannot afford to lose**
- This bot executes **real trades** when connected to a live account - use with extreme caution
- Market conditions change; a profitable backtest does not guarantee future profits

## 📊 Supported Currency Pairs

The system includes historical data for:
- EUR/USD, GBP/USD, AUD/USD
- EUR/GBP, EUR/JPY, EUR/AUD, EUR/CAD, EUR/NZD
- GBP/JPY, GBP/AUD, GBP/CAD, GBP/NZD
- AUD/JPY, AUD/CAD, AUD/NZD
- CAD/JPY

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Write tests for new functionality
4. Ensure all tests pass
5. Commit with clear messages (`git commit -m 'Add: feature description'`)
6. Push to your fork (`git push origin feature/YourFeature`)
7. Open a Pull Request with a detailed description

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions and classes
- Write unit tests for new features
- Update documentation for API changes

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## 👤 Author

**thanhtrung102**
- GitHub: [@thanhtrung102](https://github.com/thanhtrung102)

## 🙏 Acknowledgments

- OANDA for providing the forex trading API
- Open-source Python community (pandas, Flask, pymongo)
- Technical analysis and algorithmic trading research community

## 📚 Additional Resources

### Learning Resources
- [OANDA API Documentation](https://developer.oanda.com/rest-live-v20/introduction/)
- [Investopedia - Technical Analysis](https://www.investopedia.com/technical-analysis-4689657)
- [QuantStart - Algorithmic Trading](https://www.quantstart.com/)

### Related Projects
- Backtrader - Python backtesting library
- TA-Lib - Technical analysis library
- Zipline - Algorithmic trading library

---

**Final Reminder**: This bot can execute real trades with real money. Always:
- Test thoroughly in a practice/demo environment first
- Start with minimal position sizes
- Monitor the bot actively during initial live runs
- Keep API credentials secure and never commit them to version control
- Use proper risk management (stop losses, position sizing)
- Understand the strategies being employed before deploying





