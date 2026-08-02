import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing TotalCharges with median
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Business Rule 1: Monthly Charges Category
df["ChargeCategory"] = df["MonthlyCharges"].apply(
    lambda x: "Low" if x < 35 else ("Medium" if x < 70 else "High")
)

# Business Rule 2: Customer Tenure Category
df["TenureCategory"] = df["tenure"].apply(
    lambda x: "New" if x <= 12 else ("Regular" if x <= 36 else "Loyal")
)

# Number of churned customers
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Average Monthly Charges
print("\nAverage Monthly Charges:")
print(df["MonthlyCharges"].mean())

# Average Tenure
print("\nAverage Tenure:")
print(df["tenure"].mean())

# Save processed dataset
df.to_csv("Processed_Telco_Customer_Churn.csv", index=False)

print("\nProcessed dataset saved as 'Processed_Telco_Customer_Churn.csv'")
