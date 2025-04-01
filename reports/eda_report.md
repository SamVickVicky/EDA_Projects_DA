# Exploratory Data Analysis (EDA) Report

## 1. Introduction
This report presents the findings from the Exploratory Data Analysis (EDA) conducted on the dataset for marketing analytics. The dataset consists of product sales data extracted from MySQL and Excel, followed by data cleaning and transformation processes.

---

## 2. Dataset Overview
- **Source:** MySQL (`marketing_analytics.sales_data`) & Excel (`cleaned_data.csv`)
- **Total Rows:** 1,000
- **Total Columns:** 7
- **Columns & Data Types:**
  - `Product_ID` - *String* (Unique identifier for products)
  - `Product_Name` - *String* (Name of the product)
  - `Sales` - *Integer* (Total sales count per product)
  - `Category` - *String* (Category of the product: Electronics, Clothing, etc.)
  - `Price` - *Float* (Product price in INR)
  - `Region` - *String* (Region where sales occurred)
  - `Date` - *Date* (Sales transaction date)

---

## 3. Data Cleaning Summary
- **Missing Values:** No missing values were found after cleaning.
- **Duplicates:** Duplicate records were removed before analysis.
- **Outliers:** Identified and treated using IQR method for `Sales` and `Price`.

---

## 4. Descriptive Statistics
### **Numerical Data Summary**
| Column    | Mean  | Median | Std Dev | Min  | Max  |
|-----------|-------|--------|---------|------|------|
| Sales     | 500.2 | 495    | 287.5   | 10   | 990  |
| Price     | 450.7 | 400    | 300.2   | 5.0  | 1000 |

### **Categorical Data Summary**
| Category       | Count |
|---------------|-------|
| Electronics   | 250   |
| Clothing      | 300   |
| Groceries     | 250   |
| Furniture     | 200   |

---

## 5. Key Insights & Visualizations
### **Sales Distribution (Histogram)**
- **Observation:** The sales data follows a near-normal distribution with some high-sales outliers.

### **Category-wise Sales Trends (Bar Chart)**
- **Observation:** Clothing has the highest sales, followed by Electronics and Groceries.

### **Sales Correlation Analysis (Heatmap)**
- **Observation:** Price and Sales have a weak negative correlation (-0.15), suggesting that lower-priced products sell more.

### **Price vs. Sales (Scatter Plot)**
- **Observation:** Most sales happen at mid-range prices (₹200-₹700). High-end products (₹900+) have fewer sales.

### **Region-wise Sales Comparison (Box Plot)**
- **Observation:** Sales in the 'West' region show higher variability, indicating diverse product demand.

---

## 6. Business Insights
- **Popular Products:** Clothing dominates the sales market.
- **Sales Trends:** Mid-range priced products sell the most.
- **Regional Insights:** The West region has the highest fluctuation in sales.
- **Strategic Recommendation:**
  - Focus on mid-range pricing for higher sales volume.
  - Target marketing campaigns for high-demand regions.
  - Offer discounts for high-priced products to boost sales.

---

## 7. Next Steps
- Implement Power BI Dashboard to visualize these insights.
- Create interactive filters for deeper analysis.
- Use forecasting models to predict future sales trends.

**Report Created By:** Vijay Singh Parmar  
**Date:** 2 April 2025

