import pandas as pd
from sklearn.model_selection import train_test_split

# Load the original dataset
df = pd.read_csv("data/data.csv")

# Split the data into training and testing sets
X = df[["cylinders", "weight", "acceleration"]]
y = df["mpg"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create dataframes for training and testing
train_df = pd.DataFrame(
    data={
        "cylinders": X_train["cylinders"],
        "weight": X_train["weight"],
        "acceleration": X_train["acceleration"],
        "mpg": y_train,
    }
)
test_df = pd.DataFrame(
    data={
        "cylinders": X_test["cylinders"],
        "weight": X_test["weight"],
        "acceleration": X_test["acceleration"],
        "mpg": y_test,
    }
)

# Save the data to CSV files
train_df.to_csv("data/train.csv", index=False)
test_df.to_csv("data/test.csv", index=False)
