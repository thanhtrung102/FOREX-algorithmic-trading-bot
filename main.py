"""
FOREX Algorithmic Trading Bot - Development/Testing Entry Point

This module provides various test functions to verify components work correctly.
Uncomment the function you want to test in the main block.
"""

from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from infrastructure.collect_data import run_collection
from dateutil import parser


def test_api_connection():
    """Test OANDA API connectivity and account access."""
    api = OandaApi()
    account = api.get_account_summary()
    if account:
        print("Account Summary:")
        print(f"  Balance: {account.get('balance')}")
        print(f"  Currency: {account.get('currency')}")
        print(f"  Open Trades: {account.get('openTradeCount')}")
    else:
        print("Failed to get account summary")


def test_fetch_candles():
    """Test fetching candle data from OANDA."""
    api = OandaApi()
    candles = api.fetch_candles("EUR_USD", count=5, granularity="H1")
    if candles:
        print(f"Fetched {len(candles)} candles:")
        for c in candles[:3]:
            print(f"  {c['time']}: O={c['mid']['o']}, H={c['mid']['h']}, L={c['mid']['l']}, C={c['mid']['c']}")
    else:
        print("Failed to fetch candles")


def test_candles_dataframe():
    """Test fetching candles as a pandas DataFrame."""
    api = OandaApi()
    df = api.get_candles_df("EUR_USD", count=10, granularity="M5")
    if df is not None and len(df) > 0:
        print("Candles DataFrame:")
        print(df.head())
    else:
        print("Failed to get candles DataFrame")


def test_fetch_candles_date_range():
    """Test fetching candles for a specific date range."""
    api = OandaApi()
    date_from = parser.parse("2024-01-01T00:00:00Z")
    date_to = parser.parse("2024-01-02T00:00:00Z")

    df = api.get_candles_df("EUR_USD", granularity="H1",
                            date_f=date_from, date_t=date_to)
    if df is not None:
        print(f"Fetched {len(df)} candles from {date_from} to {date_to}")
        print(df.head())
    else:
        print("Failed to fetch candles for date range")


def test_instruments():
    """Test loading instruments from JSON file."""
    instrumentCollection.LoadInstruments("./data")
    print(f"Loaded {len(instrumentCollection.instruments_dict)} instruments:")
    for name, inst in list(instrumentCollection.instruments_dict.items())[:5]:
        print(f"  {name}: pip={inst.pipLocation}, precision={inst.displayPrecision}")


def test_technical_indicators():
    """Test technical indicators on sample data."""
    import pandas as pd
    from technicals.indicators import BollingerBands, RSI, MACD, ATR

    # Load sample data
    try:
        df = pd.read_pickle("./data/EUR_USD_H1.pkl")
        df = df.head(100).copy()

        # Apply indicators
        df = BollingerBands(df)
        df = RSI(df)
        df = MACD(df)
        df = ATR(df)

        print("Technical Indicators Test:")
        print(df[['time', 'mid_c', 'BB_MA', 'BB_UP', 'BB_LW', 'RSI_14', 'MACD']].tail())
    except FileNotFoundError:
        print("EUR_USD_H1.pkl not found in ./data directory")


def test_backtesting():
    """Test the GuruTester backtesting framework."""
    import pandas as pd
    from guru_tester_fast import GuruTesterFast, BUY, SELL, NONE
    from technicals.indicators import RSI

    try:
        df_h1 = pd.read_pickle("./data/EUR_USD_H1.pkl")
        df_m5 = pd.read_pickle("./data/EUR_USD_M5.pkl")

        # Apply RSI indicator
        df_h1 = RSI(df_h1.copy())

        # Simple RSI signal: Buy when RSI < 30, Sell when RSI > 70
        def rsi_signal(row):
            if row.RSI_14 < 30:
                return BUY
            elif row.RSI_14 > 70:
                return SELL
            return NONE

        # Run backtest
        tester = GuruTesterFast(
            df_big=df_h1.head(1000),
            apply_signal=rsi_signal,
            df_m5=df_m5,
            PROFIT_FACTOR=1.5,
            LOSS_FACTOR=-1.0,
            use_spread=True
        )
        tester.run_test()

        if len(tester.df_results) > 0:
            print("Backtesting Results:")
            print(f"  Total Trades: {len(tester.df_results)}")
            print(f"  Total Result: {tester.df_results.result.sum():.2f}")
            print(f"  Win Rate: {(tester.df_results.result > 0).mean() * 100:.1f}%")
        else:
            print("No trades were executed in the backtest period")

    except FileNotFoundError as e:
        print(f"Data file not found: {e}")


def collect_historical_data():
    """Collect historical data from OANDA (run with caution - takes time)."""
    api = OandaApi()
    instrumentCollection.LoadInstruments("./data")
    run_collection(instrumentCollection, api)


if __name__ == '__main__':
    # Uncomment the test you want to run:

    test_api_connection()
    # test_fetch_candles()
    # test_candles_dataframe()
    # test_fetch_candles_date_range()
    # test_instruments()
    # test_technical_indicators()
    # test_backtesting()

    # Warning: This downloads a lot of data
    # collect_historical_data()
