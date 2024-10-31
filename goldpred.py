import yfinance as yf
import pandas as pd
import streamlit as st
import datetime

st.set_page_config(layout="wide", page_title="Gold Price Fluctuations")

st.title("Gold Price Fluctuations in the US Market")

# Define the gold ticker symbol (GC=F for Gold Futures)
gold_ticker = "GC=F"

# Sidebar for date input
st.sidebar.title("Input")
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    start_date = st.date_input('Start Date', value=datetime.date(2023, 1, 1))
with col2:
    end_date = st.date_input('End Date', value=datetime.date.today())

# Fetch gold price data
try:
    gold_data = yf.download(gold_ticker, start=start_date, end=end_date)

    if gold_data.empty:
        st.error(f"No data found for {gold_ticker} within the specified date range.")
    else:
        # Display the gold price chart
        st.subheader("Gold Price (Close)")
        st.line_chart(gold_data["Close"])

        # Calculate and display daily percentage change
        st.subheader("Daily Percentage Change")
        daily_returns = gold_data["Close"].pct_change() * 100
        st.line_chart(daily_returns)

except Exception as e:
    st.error(f"An error occurred: {e}")
