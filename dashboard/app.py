import streamlit as st
import requests

st.title("Dashboard")

data = requests.get("http://localhost:8000/metrics").json()
st.write(data)
