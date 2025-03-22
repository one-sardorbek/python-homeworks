import pandas as pd

df_flights=pd.read_parquet("data/flights")
# Check for missing values in the dataset
missing_values = df_flights.isnull().sum()
print("Missing Values in Each Column:\n", missing_values)

# Fill missing values in numerical columns with their respective mean
numeric_cols = df_flights.select_dtypes(include=['number'])  # Select only numeric columns
df_flights[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())

# Verify that missing values are filled
print("\nMissing Values After Filling:\n", df_flights.isnull().sum())