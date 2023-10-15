import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error
import pytest

# Get the tests's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the parent directory
parent_dir = os.path.dirname(script_dir)
os.chdir(parent_dir)

def load_test_data():
    # Load the testing data
    test_df = pd.read_csv("data/test.csv")

    # Extract the target variable and predictor features
    target = test_df["mpg"]
    predictor_df = test_df[["cylinders", "weight", "acceleration"]]

    return target, predictor_df

def load_trained_model():
    # Load the trained model
    model = pickle.load(open("models/model.pkl", "rb"))
    return model

def test_inference():
    target, predictor_df = load_test_data()
    model = load_trained_model()

    # Perform inference using the model
    predicted_target = model.predict(predictor_df)

    # Calculate the Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mean_squared_error(target, predicted_target))

    assert rmse < 1.0  # Add your desired threshold for RMSE here

if __name__ == "__main__":
    target, predictor_df = load_test_data()
    model = load_trained_model()
    predicted_target = model.predict(predictor_df)

    # Create a dataframe to compare actual vs. predicted values
    results_df = pd.DataFrame({"Actual mpg": target, "Predicted mpg": predicted_target})

    # Print the results
    print("Testing Results")
    print(results_df[:1])

    # Calculate the Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mean_squared_error(target, predicted_target))
    print(f"Root Mean Squared Error (RMSE): {rmse}")
