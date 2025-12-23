# FOREX Algrothmic Trading Bot

A comprehensive automated forex trading system with backtesting capabilities, technical analysis, and real-time trading execution.

## 🌟 Features

- **Automated Trading Bot**: Execute trades automatically based on predefined strategies
- **Technical Analysis**: Built-in technical indicators and analysis tools
- **Backtesting Simulation**: Test trading strategies on historical data
- **Moving Average Strategies**: MA crossover detection and forecasting
- **Real-time Data Streaming**: Live market data integration
- **Database Management**: Store and retrieve historical trading data
- **API Integration**: Connect to forex trading platforms
- **Web Scraping**: Gather market data and news
- **Comprehensive Logging**: Track all bot activities and decisions

## 📁 Project Structure

```
FOREX-01/
├── api/                    # API integration modules
├── bot/                    # Core trading bot logic
├── constants/              # Configuration constants
├── data/                   # Historical and live market data
├── db/                     # Database management
├── exploration/            # Jupyter notebooks for analysis
├── infrastructure/         # Infrastructure and deployment configs
├── logs/                   # Trading logs and activity records
├── models/                 # Machine learning models
├── scraping/               # Web scraping modules
├── simulation/             # Backtesting and simulation engine
├── stream_bot/            # Real-time streaming bot
├── stream_example/        # Streaming implementation examples
├── technicals/            # Technical indicators library
├── run_bot.py             # Main bot execution script
├── main.py                # Application entry point
├── server.py              # API server
└── MA_Cross_Overforecast.ipynb  # MA crossover analysis
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Virtual environment (venv)
- Forex trading account and API credentials
- Required Python packages (see requirements.txt)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/thanhtrung102/FOREX-01.git
   cd FOREX-01
   ```

2. **Set up virtual environment**
   ```bash
   # Windows
   cd venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API credentials**
   - Create a `.env` file in the root directory
   - Add your forex trading platform API credentials
   ```
   API_KEY=your_api_key_here
   API_SECRET=your_api_secret_here
   ACCOUNT_ID=your_account_id_here
   ```

### Running the Bot

**Start the trading bot:**
```bash
python run_bot.py
```

**Run the API server:**
```bash
python server.py
```

**Execute backtesting:**
```bash
python guru_tester_fast.py
```

## 📊 Strategy Development

### Backtesting Results

The project includes simulation results for different timeframes:
- `ma_sim_M5.xlsx` - 5-minute timeframe results
- `ma_sim_H1.xlsx` - 1-hour timeframe results
- `ma_sim_H4.xlsx` - 4-hour timeframe results

### Running Experiments

Use Jupyter notebooks for strategy development and analysis:

```bash
jupyter notebook
cd exploration
```

Key notebooks:
- `MA_Cross_Overforecast.ipynb` - Moving Average crossover analysis
- `plotting_candles.ipynb` - Candlestick chart visualization

## 🛠️ Development

### Testing

Run API tests:
```bash
python api_tests.py
```

Run scraping tests:
```bash
python scraping_tests.py
```

Run general tests:
```bash
python tester.py
```

### Code Application

Apply trading strategies to historical data:
```bash
python apply_code.py
```

## 🔧 Configuration

The `constants/` directory contains configuration files for:
- Trading pairs
- Risk management parameters
- Technical indicator settings
- Bot behavior configurations

## 📈 Technical Indicators

The `technicals/` module includes implementations of:
- Moving Averages (SMA, EMA)
- Relative Strength Index (RSI)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- And more...

## 💾 Database

The `db/` module manages:
- Historical price data storage
- Trade execution records
- Performance metrics
- Strategy backtesting results

## 🔄 Real-time Streaming

The bot supports real-time market data streaming through:
- `stream_bot/` - Main streaming implementation
- `stream_example/` - Example streaming configurations

## 📝 Logging

All trading activities are logged in the `logs/` directory:
- Trade executions
- Strategy signals
- Error messages
- Performance metrics

## ⚠️ Disclaimer

**This software is for educational purposes only. Trading forex involves substantial risk of loss. Past performance is not indicative of future results. Use this bot at your own risk. The developers are not responsible for any financial losses incurred through the use of this software.**

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**thanhtrung102**
- GitHub: [@thanhtrung102](https://github.com/thanhtrung102)

## 🙏 Acknowledgments

- Thanks to all contributors and the open-source community
- Forex data providers
- Technical analysis library developers

---

**Note**: Remember to always test strategies thoroughly in a demo environment before deploying with real capital. Keep your API credentials secure and never commit them to version control.


