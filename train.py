import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the training data
train_df = pd.read_csv("data/train.csv")

# Extract the target variable and predictor features
target = train_df["mpg"]
predictor_df = train_df[["cylinders", "weight", "acceleration"]]

# Create and train the model
model = LinearRegression()
model.fit(predictor_df, target)

# Save the trained model to a file
filename = "models/model.pkl"
pickle.dump(model, open(filename, "wb"))

print("Model trained and saved to the 'models' folder as model.pkl.")
