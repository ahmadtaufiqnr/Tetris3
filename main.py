import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQMqC_6fkaH6oZweJDIIYFDdE9o3P3G1hB0OKLzkGGf0pB-FjWJoAMoYca2iXV2ID5dE7hoklCSx6hE/pub?gid=0&single=true&output=csv')

df['order_date']=pd.to_datetime(df['order_date'])
df['ship_date']=pd.to_datetime(df['ship_date'])
df['order_year']=df['order_date'].dt.year

CURR_YEAR=max(df['order_date'].dt.year)

st.title("Tokopedia Dashboard")
st.metric("Sales", 1000, -10)