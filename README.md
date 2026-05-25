# Real-Time Stock Market ETL & Visualization Pipeline

A Python-based stock market data pipeline that fetches historical stock data from Yahoo Finance, processes it using Pandas, stores it in SQLite and Parquet format, and visualizes it using a Streamlit dashboard with Plotly charts.

---

# Features

- Fetches stock market data using Yahoo Finance
- Processes and transforms financial data
- Calculates:
  - 20-Day SMA
  - 50-Day SMA
  - Daily Returns
- Stores processed data in:
  - SQLite database
  - Parquet files
- Interactive Streamlit dashboard
- Dynamic stock selection
- Plotly visualizations
- CSV download support
- Logging system for monitoring pipeline activity

---

# Tech Stack

- Python
- Pandas
- SQLite
- Streamlit
- Plotly
- yFinance
- Matplotlib
- Logging

---

# Project Structure

```text
project/
│
├── main.py
├── Display.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── parquet/
│   └── stocks.db
│
└── logs/
    └── pipeline.log
```

---

# Data Pipeline Architecture

```text
Yahoo Finance API
        ↓
main.py ETL Pipeline
        ↓
SQLite / Parquet Storage
        ↓
Streamlit Dashboard
        ↓
Interactive Visualizations
```

---

# Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-name>
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Requirements

Example `requirements.txt`

```txt
pandas
yfinance
streamlit
plotly
matplotlib
pyarrow
```

---

# Running the ETL Pipeline

Run the backend data pipeline:

```bash
python main.py
```

This will:
- Fetch stock market data
- Process indicators
- Save SQLite database
- Save parquet files
- Generate logs

---

# Running the Dashboard

Start Streamlit dashboard:

```bash
streamlit run Display.py
```

---

# Dashboard Features

The dashboard includes:

- Dynamic stock selector
- Closing price visualization
- Moving average analysis
- Trading volume chart
- Raw data viewer
- CSV export functionality

Supported stocks:

- AAPL
- MSFT
- GOOGL
- AMZN
- NVDA

---

# Example Visualizations

## Closing Price Chart

Displays stock price movement over time.

## Moving Average Analysis

Shows:
- SMA 20
- SMA 50

Used for trend analysis.

## Trading Volume

Displays trading activity for selected stock.

---

# Logging

Logs are stored in:

```text
logs/pipeline.log
```

The logging system tracks:
- pipeline execution
- errors
- stock processing
- database updates

Example log:

```text
2026-05-25 10:22:11 | INFO | Processing AAPL
```

---

# Future Improvements

Possible upgrades:

- Real-time streaming
- Docker deployment
- PostgreSQL integration
- Redis caching
- Kafka streaming
- User authentication
- Portfolio tracking
- Technical indicators:
  - RSI
  - MACD
  - Bollinger Bands
- Cloud deployment
- CI/CD pipelines

---

# Learning Objectives

This project demonstrates:

- ETL pipeline design
- Data engineering fundamentals
- Financial data processing
- Streamlit dashboard development
- SQL database integration
- Logging and monitoring
- Data visualization
- Backend/frontend separation

---

# License

MIT License