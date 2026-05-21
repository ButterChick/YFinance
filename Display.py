# app.py

import streamlit as st
import pandas as pd
import sqlite3
import plotly.graph_objects as go


# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Stock Dashboard",
    layout="wide"
)

st.title("Stock Market Dashboard")


# ----------------------------
# LOAD DATA
# ----------------------------

def load_data():

    conn = sqlite3.connect(
        "data/stocks.db"
    )

    # Change table name if needed
    query = "SELECT * FROM AAPL"

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df


df = load_data()


# ----------------------------
# DATA CLEANING
# ----------------------------

df["Date"] = pd.to_datetime(
    df["Date"]
)

df = df.sort_values(
    by="Date"
)


# ----------------------------
# METRICS
# ----------------------------

latest_close = df["Close"].iloc[-1]

highest_price = df["High"].max()

lowest_price = df["Low"].min()

volume = df["Volume"].iloc[-1]


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Latest Close",
    f"${latest_close:.2f}"
)

col2.metric(
    "Highest Price",
    f"${highest_price:.2f}"
)

col3.metric(
    "Lowest Price",
    f"${lowest_price:.2f}"
)

col4.metric(
    "Volume",
    f"{volume:,}"
)


# ----------------------------
# PRICE CHART
# ----------------------------

st.subheader("Closing Price")

price_fig = go.Figure()

price_fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Close"],
        mode="lines",
        name="Close Price"
    )
)

price_fig.update_layout(
    height=500,
    xaxis_title="Date",
    yaxis_title="Price"
)

st.plotly_chart(
    price_fig,
    use_container_width=True
)


# ----------------------------
# MOVING AVERAGES
# ----------------------------

st.subheader("Moving Averages")

ma_fig = go.Figure()

ma_fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Close"],
        mode="lines",
        name="Close"
    )
)

if "SMA_20" in df.columns:

    ma_fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["SMA_20"],
            mode="lines",
            name="SMA 20"
        )
    )

if "SMA_50" in df.columns:

    ma_fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["SMA_50"],
            mode="lines",
            name="SMA 50"
        )
    )

ma_fig.update_layout(
    height=500
)

st.plotly_chart(
    ma_fig,
    use_container_width=True
)


# ----------------------------
# VOLUME CHART
# ----------------------------

st.subheader("Trading Volume")

volume_fig = go.Figure()

volume_fig.add_trace(
    go.Bar(
        x=df["Date"],
        y=df["Volume"],
        name="Volume"
    )
)

volume_fig.update_layout(
    height=400
)

st.plotly_chart(
    volume_fig,
    use_container_width=True
)


# ----------------------------
# RAW DATA
# ----------------------------

with st.expander("Show Raw Data"):

    st.dataframe(df)


# ----------------------------
# DOWNLOAD CSV
# ----------------------------

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="stock_data.csv",
    mime="text/csv"
)