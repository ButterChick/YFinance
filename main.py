import logging
from pathlib import Path
from datetime import datetime
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import sqlite3

CONFIG = {
    "tickers": ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"],
    "start_date": "2022-01-01",
    "end_date": datetime.today().strftime("%Y-%m-%d"),
    "parquet_dir": "data/parquet",
    "sqlite_path": "data/stocks.db",
    "log_file": "logs/pipeline.log",
}

#Logging

def setup_logging(log_file: str) -> logging.Logger:
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("StockPipeline")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Extract

def fetch_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame: #It will return a Data Frame and the input will be a ticker Obejct (Yfinace)
    stock = yf.Ticker(ticker)

    df = stock.history(
        start=start,
        end=end,
        auto_adjust=False # Raw market data, not removing dividents
    )

    df.reset_index(inplace=True)
    df["Ticker"] = ticker

    return df

# Transform data

def add_indicators(df: pd.DataFrame) -> pd.DataFrame: # Takes a DataFrame and returns a dataframe
    df["SMA_20"] = df["Close"].rolling(20).mean() #Simple moving Average Of 20 days
    df["SMA_50"] = df["Close"].rolling(50).mean() #Simple moving Average Of 50 days

    df["Daily_Return"] = df["Close"].pct_change() #Percentage change in a stock

    return df

# Save Parquet

def save_parquet(df: pd.DataFrame, ticker: str, parquet_dir: str):  #No return value, Takes dataframe, ticker and Parquet dir
    Path(parquet_dir).mkdir(parents=True, exist_ok=True)

    file_path = f"{parquet_dir}/{ticker}.parquet"

    df.to_parquet(file_path, index=False)


# Save to SQLite

def save_sqlite(df: pd.DataFrame, db_path: str, table_name: str):
    conn = sqlite3.connect(db_path)

    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()

# Main Pipeline

def run_pipeline():
    logger = setup_logging(CONFIG["log_file"])

    logger.info("Pipeline started")

    for ticker in CONFIG["tickers"]:
        logger.info(f"Processing {ticker}")

        try:
            # Extract
            df = fetch_stock_data(
                ticker,
                CONFIG["start_date"],
                CONFIG["end_date"]
            )

            # Transform
            df = add_indicators(df)

            # Load
            save_parquet(df, ticker, CONFIG["parquet_dir"])
            save_sqlite(df, CONFIG["sqlite_path"], ticker)

            logger.info(f"Completed {ticker}")

        except Exception as e:
            logger.error(f"Error processing {ticker}: {e}")

    logger.info("Pipeline completed")


if __name__ == "__main__":
    run_pipeline()