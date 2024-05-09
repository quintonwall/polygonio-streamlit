import os, streamlit as st
import pandas as pd
from polygon import RESTClient
from bokeh.plotting import figure


st.subheader("Polygon+Streamlit Demo App")
symbol = st.text_input("Enter a stock symbol", "AAPL")

with st.sidebar:
    #Get your Polygon API key from the dashboard. 
    #In a real app you want to store this as a secret in your .env
    polygon_api_key = st.text_input("Polygon API Key", type="password")

# Authenticate with the Polygon API
client = RESTClient(polygon_api_key)

col1, col2, col3, col4 = st.columns(4)



#historical data for the year
if col1.button("Line Chart"):
    if not polygon_api_key.strip() or not symbol.strip():
        st.error("Please add your Polygon API Key on the left")
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

#historical data for the year
if col2.button("Bar Chart"):
    if not polygon_api_key.strip() or not symbol.strip():
        st.error("Please add your Polygon API Key on the left")
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
      
            st.bar_chart(chart_data, x="date_formatted",y="close")
    
        except Exception as e:
            st.exception(f"Exception: {e}")

#historical data for the year
if col3.button("Area Chart"):
    if not polygon_api_key.strip() or not symbol.strip():
        st.error("Please add your Polygon API Key on the left")
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
      
            st.area_chart(chart_data, x="date_formatted",y="close")
    
        except Exception as e:
            st.exception(f"Exception: {e}")
 

 #Bokeh
if col4.button("Bokeh Chart"):
    if not polygon_api_key.strip() or not symbol.strip():
        st.error("Please add your Polygon API Key on the left")
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
            
            p = figure(
            title='bokeh chart example',
            x_axis_label='Date',
            y_axis_label='Close')
        
            p.line(chart_data["date_formatted"], chart_data["close"], legend_label='Trend', line_width=2)
            st.bokeh_chart(p, use_container_width=True)
        
        except Exception as e:
            st.exception(f"Exception: {e}")
 
 
