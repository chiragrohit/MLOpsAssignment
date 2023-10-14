import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

# Load the testing data
test_df = pd.read_csv("data/test.csv")

# Extract the target variable and predictor features
target = test_df["mpg"]
predictor_df = test_df[["cylinders", "weight", "acceleration"]]

# Load the trained model
model = pickle.load(open("models/model.pkl", "rb"))

# Perform inference using the model
predicted_target = model.predict(predictor_df)

# Create a dataframe to compare actual vs. predicted values
results_df = pd.DataFrame({"Actual mpg": target, "Predicted mpg": predicted_target})

# Print the results
print("Testing Results")
print(results_df)


# Calculate the Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(target, predicted_target))

print(f"Root Mean Squared Error (RMSE): {rmse}")
