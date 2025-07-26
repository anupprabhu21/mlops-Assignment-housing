# src/preprocess.py

from sklearn.datasets import fetch_california_housing
import pandas as pd
import os

# Ensure directory exists
os.makedirs("data/raw", exist_ok=True)

# Load dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Save dataset
df.to_csv("data/raw/housing.csv", index=False)

