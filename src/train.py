import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn
import joblib
import os

# Create directory if it doesn't exist
os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/raw/housing.csv")
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

models = {
    "LinearRegression": LinearRegression(),
    "DecisionTree": DecisionTreeRegressor()
}

mlflow.set_experiment("housing-experiment")

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        mlflow.log_param("model", name)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")
        joblib.dump(model, f"models/{name}.pkl")

