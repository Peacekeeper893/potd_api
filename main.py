import streamlit as st
import requests

st.set_page_config(layout="wide")

api_key = "oorsbckeObfDzstCNmq3dlrG6yaKI2gFcAp0KRU0"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()

st.title(content["title"])

st.write(" ")

st.image(f"{content['hdurl']}")

st.write(content["explanation"])
