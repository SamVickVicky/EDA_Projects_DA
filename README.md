# **Marketing Analytics Capstone Project**

## **1. Project Overview**
This project focuses on **Exploratory Data Analysis (EDA)** and **Dashboard Development** for marketing analytics using Python, MySQL, Excel, and Power BI. The goal is to analyze sales trends, category performance, and regional insights.

## **2. Tools & Technologies Used**
- **Programming & Analysis:** Python, Jupyter Notebook
- **Data Storage:** MySQL, Excel
- **Visualization & Reporting:** Power BI
- **Code Editor:** VS Code

## **3. Data Sources & ETL Process**
### **Data Collection**
- **MySQL Database:** `marketing_analytics.clean_sales_data`
- **Excel File:** `data/cleaned_data.csv`

### **ETL Process**
1. **Extract:** Data was sourced from MySQL and Excel.
2. **Transform:** Data cleaning was performed using Python (`data_cleaning.py`).
3. **Load:** Cleaned data was stored back into MySQL and used in Power BI.

## **4. Exploratory Data Analysis (EDA)**
### **EDA Insights & Key Findings:**
✅ **Sales Distribution:** Sales data follows a right-skewed distribution, indicating a few high-value sales drive revenue.  
✅ **Category Performance:** The **Electronics** category generates the highest revenue.  
✅ **Regional Insights:** The **South** region has the highest sales.  
✅ **Price vs. Sales Analysis:** Higher-priced products show moderate sales, while mid-range priced products have higher volumes.  
✅ **Seasonality Trends:** Sales peak during festive seasons.  

## **5. Power BI Dashboard Development**
### **Key Visualizations:**
- **Sales Distribution (Histogram)** – Displays overall sales patterns.
- **Category-wise Sales (Bar Chart)** – Highlights top-performing product categories.
- **Region-wise Sales (Bar Chart)** – Compares sales by region.
- **Sales Over Time (Line Chart)** – Identifies trends and seasonality.
 

## **6. Business Recommendations**
📌 **Category Strategy:** Increase investment in **Electronics** and **Furniture**, as they drive the most revenue.  
📌 **Regional Focus:** Expand operations in the **South** region to capitalize on high sales potential.  
📌 **Pricing Optimization:** Mid-range pricing strategy performs best; adjust pricing for high-end products.  
📌 **Seasonal Promotions:** Target major sales spikes with tailored marketing campaigns.  

## **7. Project Files & Folder Structure**
📂 **Capstone_Project/**  
│── 📁 `data/` – Stores raw & cleaned data  
│── 📁 `scripts/` – Python scripts for ETL & EDA  
│── 📁 `notebooks/` – Jupyter Notebooks for analysis  
│── 📁 `dashboard/` – Power BI dashboard file  
│── 📁 `reports/` – Final project report & dashboard summary  
│── 📄 `README.md` – Project description  

## **8. Conclusion**
This project successfully demonstrated the use of **EDA, data visualization, and business intelligence** for marketing analytics. The insights extracted help businesses optimize sales, pricing, and marketing strategies.  

🚀 **Final Deliverables:**  
✅ **Power BI Dashboard:** `dashboard/marketing_dashboard.pbix`  
✅ **EDA Report:** `reports/eda_report.md`  
✅ **Power BI Summary:** `reports/powerbi_dashboard_summary.pdf`
