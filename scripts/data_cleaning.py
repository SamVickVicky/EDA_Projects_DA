import pandas as pd
import os

# Project folder paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get 'Capston_Project/' folder path
DATA_DIR = os.path.join(BASE_DIR, 'data')  # Path to 'data/' folder

# File paths
raw_data_path = os.path.join(DATA_DIR, 'data_from_mysql.csv')
cleaned_data_path = os.path.join(DATA_DIR, 'cleaned_data.csv')

# Load data
df = pd.read_csv(raw_data_path)
print("✅ Data loaded successfully!")

# Display basic info
print("🔍 Initial Data Overview:")
print(df.info())
print(df.head())

# Handling missing values
df.dropna(inplace=True)  # Drop rows with missing values
print("✅ Missing values handled!")

# Remove duplicates
df.drop_duplicates(inplace=True)
print("✅ Duplicates removed!")

# Convert column types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to datetime

# Remove invalid dates
df = df.dropna(subset=['Date'])

# Ensure 'Price' is positive
df = df[df['Price'] > 0]

# Ensure 'Sales' is a positive integer
df['Sales'] = df['Sales'].astype(int)
df = df[df['Sales'] > 0]

print("✅ Data cleaning complete!")

# Save cleaned data
df.to_csv(cleaned_data_path, index=False)
print(f"📁 Cleaned data saved to: {cleaned_data_path}")