import streamlit as st
import requests

# Streamlit app title
st.title("Stock Price Checker")

# User input for stock symbol
symbol = st.text_input("Enter Stock Symbol:")

# API key input (you can hardcode this if preferred)
api_key = st.text_input("Enter Alpha Vantage API Key:")

# Check if symbol and API key are provided
if symbol and api_key:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "Global Quote" in data:
            try:
                price = float(data["Global Quote"]["05. price"])
                yest_price = float(data["Global Quote"]["08. previous close"])

                st.write(f"The price of this stock is {price} dollars.")

                diff = price - yest_price
                diff_better = f"{diff:.2f}"

                if diff > 0:
                    st.write(f"The stock price has increased by {diff_better} dollars since yesterday.")
                elif diff < 0:
                    st.write(f"The stock price has decreased by {diff_better} dollars since yesterday.")
                else:
                    st.write("The stock price has remained the same since yesterday.")
