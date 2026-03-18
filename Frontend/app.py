import streamlit as st
import requests

st.title("Manufacturing Machine Output Prediction")

st.write("Enter machine parameters")

temp = st.number_input("Injection Temperature")
pressure = st.number_input("Injection Pressure")
cycle = st.number_input("Cycle Time")
cooling = st.number_input("Cooling Time")

if st.button("Predict Output"):

    data = [temp, pressure, cycle, cooling]

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.success(result)