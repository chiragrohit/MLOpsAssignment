import streamlit as st
import pandas as pd
import pickle

# Load the model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Create a Streamlit app
st.title("Model Inference: Miles Per Gallon Prediction")

# Create input fields
cylinders = st.number_input("Cylinders", min_value=1, step=1)
weight = st.number_input("Weight", min_value=0, step=500)
acceleration = st.number_input("Acceleration", min_value=0, step=5)

# Create a button for prediction
if st.button("Predict"):
    # Create a DataFrame from the user input
    input_data = {
        "cylinders": [cylinders],
        "weight": [weight],
        "acceleration": [acceleration],
    }
    input_df = pd.DataFrame(input_data)

    # Perform inference using the loaded model
    prediction = model.predict(input_df)
    st.write(f"Miles per gallon Prediction: {prediction[0]}")
