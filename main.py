import os, streamlit as st
import pandas as pd
from polygon import RESTClient


st.subheader("Polygon+Streamlit Demo App")
symbol = st.text_input("Enter a stock symbol", "AAPL")

with st.sidebar:
    #Get your Polygon API key from the dashboard. 
    #In a real app you want to store this as a secret in your .env
    polygon_api_key = st.text_input("Polygon API Key", type="password")

# Authenticate with the Polygon API
client = RESTClient(polygon_api_key)

col1, col2, col3 = st.columns(3)

#Stock details
if col1.button("Get Details"):
    if not polygon_api_key.strip() or not symbol.strip():
        st.error("Please add your Polygon API Key on the left <--")
    else:
        try:
            details = client.get_ticker_details(symbol)
            st.success(f"Ticker: {details.ticker}\n\n"
                f"Company Address: {details.address}\n\n"
                f"Market Cap: {details.market_cap}")
        except Exception as e:
            st.exception(f"Exception: {e}") 

#Current bid info
if col2.button("Get Quote"):
    if not polygon_api_key.strip() or not symbol.strip():
        st.error("Please add your Polygon API Key on the left <--")
    else:
        try:
            aggs = client.get_previous_close_agg(symbol)
            for agg in aggs:
                st.success(f"Ticker: {agg.ticker}\n\n"
                    f"Close: {agg.close}\n\n"
                    f"High: {agg.high}\n\n"
                    f"Low: {agg.low}\n\n"
                    f"Open: {agg.open}\n\n"
                    f"Volume: {agg.volume}")
        except Exception as e:
            st.exception(f"Exception: {e}") 

#historical data for the year
if col3.button("Get Historical"):
    if not polygon_api_key.strip() or not symbol.strip():
        st.error("Please add your Polygon API Key on the left <--")
    else:
        try:
            dataRequest = client.list_aggs(
                ticker = symbol,
                multiplier = 1,
                timespan = "day",
                from_ = "2024-01-01",
                to = "2024-04-29"
            )
            chart_data = pd.DataFrame(dataRequest)
    
            chart_data['date_formatted'] = chart_data['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000))
      
            st.line_chart(chart_data, x="date_formatted",y="close")
    
        except Exception as e:
            st.exception(f"Exception: {e}") 
 
