import streamlit as st
import requests

st.title("My app")
st.write("hello world")

if st.button("connect to fastapi"):
    url = "http://fastapi:8000/"
    res = requests.get(url)
    st.write(res.status_code)
    js = res.json()
    st.json(js)
