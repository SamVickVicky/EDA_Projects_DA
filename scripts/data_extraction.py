import mysql.connector
import pandas as pd
import numpy as np
import os
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of records to generate
NUM_RECORDS = 1000

# Project folder paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get 'Capston_Project/' folder path
DATA_DIR = os.path.join(BASE_DIR, 'data')  # Path to 'data/' folder

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Function to generate synthetic data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        product_id = fake.unique.uuid4()  # Unique Product ID
        product_name = fake.word()  # Random product name
        sales = np.random.randint(1, 1000)  # Random sales number between 1 and 1000
        category = np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Furniture'])  # Random category
        price = round(np.random.uniform(5, 1000), 2)  # Random price between 5 and 1000
        region = np.random.choice(['North', 'South', 'East', 'West'])  # Random region
        date = fake.date_this_decade()  # Random date within the last decade

        data.append([product_id, product_name, sales, category, price, region, date])

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Product_ID', 'Product_Name', 'Sales', 'Category', 'Price', 'Region', 'Date'])
    return df

# Generate synthetic data
df = generate_data(NUM_RECORDS)

# MySQL connection details
host = "localhost"
user = "root"
password = "Aniket%40123"
database = "marketing_analytics"

# Connect to MySQL server (without specifying database first)
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)
cursor = conn.cursor()

# Create database if it does not exist
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
cursor.close()
conn.close()

# Reconnect to MySQL with the database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        Product_ID VARCHAR(255),
        Product_Name VARCHAR(255),
        Sales INT,
        Category VARCHAR(255),
        Price FLOAT,
        Region VARCHAR(255),
        Date DATE
    )
""")

# Insert data into the sales_data table
for row in df.itertuples(index=False, name=None):
    cursor.execute("""
        INSERT INTO sales_data (Product_ID, Product_Name, Sales, Category, Price, Region, Date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, row)

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

# Save data to 'data/' folder inside the project
csv_path = os.path.join(DATA_DIR, 'data_from_mysql.csv')
excel_path = os.path.join(DATA_DIR, 'data_from_excel.xlsx')

df.to_csv(csv_path, index=False)
df.to_excel(excel_path, index=False)

print(f"✅ Data inserted successfully into MySQL and saved to: \n📁 {csv_path} \n📁 {excel_path}")
