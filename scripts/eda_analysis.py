import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Project folder paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get 'Capston_Project/' folder path
DATA_DIR = os.path.join(BASE_DIR, 'data')  # Path to 'data/' folder
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')  # Path to 'reports/' folder

# Ensure the reports directory exists
os.makedirs(REPORTS_DIR, exist_ok=True)

# File path for cleaned data
cleaned_data_path = os.path.join(DATA_DIR, 'cleaned_data.csv')

# Load cleaned data
df = pd.read_csv(cleaned_data_path)
print("✅ Data loaded successfully!")

# Display basic statistics
print("🔍 Data Overview:")
print(df.describe())
print(df.info())

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sales distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'], bins=30, kde=True, color='blue')
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig(os.path.join(REPORTS_DIR, 'sales_distribution.png'))  # Save image
plt.close()

# Sales by Category
plt.figure(figsize=(8, 5))
sns.boxplot(x='Category', y='Sales', data=df, palette='coolwarm')
plt.title("Sales by Product Category")
plt.xticks(rotation=45)
plt.savefig(os.path.join(REPORTS_DIR, 'sales_by_category.png'))  # Save image
plt.close()

# Sales Trend Over Time
plt.figure(figsize=(10, 5))
df.groupby('Date')['Sales'].sum().plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid()
plt.savefig(os.path.join(REPORTS_DIR, 'sales_trend_over_time.png'))  # Save image
plt.close()

# Region-wise Sales
plt.figure(figsize=(8, 5))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum, palette='viridis')
plt.title("Total Sales by Region")
plt.savefig(os.path.join(REPORTS_DIR, 'sales_by_region.png'))  # Save image
plt.close()

print("✅ EDA Completed Successfully! All images saved to the reports folder.")
