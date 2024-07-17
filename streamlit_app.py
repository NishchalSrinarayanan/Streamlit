import streamlit as st
import requests

st.title("Stock Price Checker")

symbol = st.text_input("Enter Stock Symbol:")

if symbol:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={st.secrets['api_key']}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "Global Quote" in data:
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
            except (KeyError, ValueError):
                st.write("Error parsing stock data.")
        else:
            st.write("No data found for the provided symbol.")
    else:
        st.write("Error fetching data from Alpha Vantage API.")
else:
    st.write("Please enter the stock symbol.")
