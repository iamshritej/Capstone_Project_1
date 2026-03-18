if st.button("Predict"):
    url = "https://capstone-project-1-0icy.onrender.com/predict"

    data = {
        "data": [input1, input2, input3, input4]
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result}")
        else:
            st.error(f"Error: {response.text}")

    except:
        st.error("Error connecting to API")