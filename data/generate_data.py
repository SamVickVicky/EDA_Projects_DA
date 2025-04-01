import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Create a synthetic dataset
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        product_id = fake.unique.uuid4()
        product_name = fake.word()
        sales = np.random.randint(1, 1000)
        category = np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Furniture'])
        price = round(np.random.uniform(5, 1000), 2)
        region = np.random.choice(['North', 'South', 'East', 'West'])
        date = fake.date_this_decade()

        data.append([product_id, product_name, sales, category, price, region, date])

    df = pd.DataFrame(data, columns=['Product_ID', 'Product_Name', 'Sales', 'Category', 'Price', 'Region', 'Date'])
    return df

# Generate 1000 records
df = generate_data(1000)

# Save to CSV for MySQL and Excel
df.to_csv('data_from_mysql.csv', index=False)
df.to_excel('data_from_excel.xlsx', index=False)
