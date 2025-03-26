import pandas as pd

# Load the employee dataset
df = pd.read_csv("data/employee.csv")

# Define a function to normalize salaries
def normalize(column):
    return (column - column.min()) / (column.max() - column.min())

# Apply normalization within each department
df["Normalized_Salary"] = df.groupby("DEPARTMENT")["BASE_SALARY"].transform(normalize)

# Display the first few rows
print(df[["DEPARTMENT", "BASE_SALARY", "Normalized_Salary"]].head())
