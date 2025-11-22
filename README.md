
---

# Overview

This dataset is a simulation that was modeled for flight operations across major US airlines. Each record in the dataset represents a single flight with the realistic distributions for these columns: 

- **Load Factor (%)**
- **Net Profit Margin (%)**
- **Delay (Minutes)**
- **Operating Cost / Revenue**
- **Fuel Price**
- **Fleet Availability**
- **Maintenance Downtime**
- **Aircraft Utilization**
- **Turnaround Time**
- **ASK-based financial metrics**


The objective in this project was to find the depths of flight operations, see what drives profits in airlines, inefficiencies (what holds airline profitability back), and how operational behavior scales financially. 

## Project Goals

This project explores the operational and financial behavior of airlines through synthetic flight-level data.  
Key questions addressed:

- **What operational factors have the strongest impact on profitability?**
- **Is there a load factor “sweet spot” where profits peak?**
- **How do delays influence operating costs and margins?**
- **How sensitive are airlines to fuel price fluctuations?**
- **Which operational inefficiencies erode profitability the fastest?**

The goal is to simulate airline economics and understand how day-to-day operational behavior scales financially.



---

# Tableau Visualizations

### **1. Load Factor vs Net Profit Margin: Profitability Curve**

This scatterplot was to see where profit margin peaks, compared to load factor. The graph reveals that the profits increase as the load factor goes up, and especially increase sharply near **70-85% load factor**. The returns are diminishing near the **90%** mark. 
A scatterplot showing the “**sweet spot**” where profit margin peaks.  

---

### **2. Delay, Load Factor Heatmap**

The heatmap shows the relationship, showing that **higher delays lead to lower profit margins**. Also, we see that flights with low loads are very unprofitable when delayed, which is shown by the lumps of red near the bottom. 

Operational reliability directly impacts the margin in airlines.

### **3. Fuel Price vs Net Profit Margin (Monthly Trend)**

The dual-axis bar + line chart tracks the monthly fuel prices and the monthly average net profit margin. In this, we see that as fuel prices rise, the profit margin decreases. We also see that margins show a small recovery in months that have lower/stable fuel prices. This shows us how sensitive fuel costs are to the operations and profitability of airlines. 

Demonstrates the sensitivity of airline profitability to fuel costs.

## Dataset Creation (Python)

The dataset that I used in the project was based on a Kaggle dataset (user absinthepapi), but I created a Python script which made the dataset more realistic. In here, I adjusted the 200,000+ flight records to 100,000 records, and converted it to statistically accurate patterns for all of the data. 

The dataset used in this project was generated using a custom Python script designed to simulate realistic U.S. airline operations.  
The code creates 5,000+ synthetic flight records with statistically accurate patterns for load factor, delays, fuel prices, utilization, and profitability.

### Key Generation Logic:
- **Load Factor (%)** — normally distributed around 80%, clipped to 40–100%.
- **Delays (Minutes)** — based on a normal distribution with realistic spread and minimum 0.
- **Fuel Prices** — assigned per month using random uniform monthly averages (2.2–3.4 USD/gal).
- **Aircraft Utilization** — daily hours normally distributed around major airline averages (10–12 hours/day).
- **Maintenance Downtime** — exponential distribution to model occasional high downtime events.
- **Turnaround Time** — normally distributed around 70 minutes.
- **Financial Modeling**
  - **Revenue (USD)** increases with load factor + utilization.
  - **Operating Cost (USD)** increases with delays, fuel price, and maintenance downtime.
  - **Profit** = Revenue – Operating Cost
  - **Net Profit Margin (%)** = Profit / Revenue × 100


## PROJECT REPRODUCTION

### Clone the repository:

git clone https://github.com/xdhyungsik/ProfitabilityInsights.git
cd ProfitabilityInsights

Project2.twbx

## Tools & Technologies
- **Python (Pandas, NumPy, MatPlotLib)** — dataset creation and feature engineering  
- **Tableau** — dashboards and visual analytics  
- **GitHub** — project documentation and version control





