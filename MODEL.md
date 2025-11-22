# Predictive Modeling: Net Profit Margin (%)

Model.md is to summarize the predictive modeling & machine learning component of this project, which coincides with the Tableau dashboard by quantifying the operational drivers of profitability through a regression-based approach. 
---

## Objective

The objective was to build a regression model that predicts the profits of an airline from a operational and financial point of view, using the metrics used for the data. 
The model shows the profit relationships mathematically, instead of just a visual output. 


---

## Modeling Pipeline

### 1. Data Preparation
- Loaded the final flight dataset and removed missing values  
- Converted scheduled departure timestamps into:
  - Year
  - Month
  - Day
  - Day of Week  
- Selected operational + financial predictors
- Standardized all numerical inputs using `StandardScaler`

### 2. Models Trained
To evaluate predictive power, two regression models were trained:

- **Random Forest Regressor**  
- **XGBoost Regressor**

Both were trained on a 10% stratified sample of the dataset to ensure computational efficiency and representative distribution.

### 3. Evaluation Metrics
- **R² Score**  
- **Mean Absolute Error (MAE)**  

---

## Results

### Random Forest
- R²: **0.9986**  
- MAE: **0.0889**

### XGBoost
- R²: **0.9981**  
- MAE: **0.1140**

The near-perfect R² value is expected due to the deterministic financial relationships in the dataset.

---

## Feature Importance (Random Forest)

Revenue (USD) 0.512
Operating Cost (USD) 0.486
Maintenance Downtime (Hours) 0.00028
Fleet Availability (%) 0.00025
Load Factor (%) 0.00023
Day 0.00023
Aircraft Utilization (Hours/Day) 0.00021
Delay (Minutes) 0.00014
Month 0.00014
Jet_Fuel_Price_USD_per_Gal 0.00013
DayOfWeek 0.00012
Year 0.00000


### Interpretation
- **Revenue + Operating Cost** overwhelmingly determine margin  
- Operational disruptions (delays, downtime) contribute, but at a smaller scale  
- Air travel economics remain dominated by cost and revenue structures  

---

## Full Modeling Script

See:  
`/modeling/profitability_model.py`

---

## Summary

The predictive modeling validates the insights generated in the Tableau dashboard:
- Higher load factor → higher profit  
- Delays and downtime reduce profitability  
- Fuel price affects cost structure  
- Profit margin is mathematically driven by revenue and cost  

This section provides a quantitative layer behind the visual analysis.
