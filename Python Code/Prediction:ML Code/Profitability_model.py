import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_absolute_error


# 1. Load dataset
flights = pd.read_csv('/Users/xdhyungsik/Downloads/AA Profitability Project/AA_synthetic_100k.csv')

# 2. Basic cleaning
flights.dropna(inplace=True)

# 3. Create FlightDate from Scheduled Departure Time
flights['FlightDate'] = pd.to_datetime(
    flights['Scheduled Departure Time'],
    errors='coerce'
)

# Remove rows where date conversion failed
flights = flights.dropna(subset=['FlightDate'])

# 4. Extract date features
flights['Year'] = flights['FlightDate'].dt.year
flights['Month'] = flights['FlightDate'].dt.month
flights['Day'] = flights['FlightDate'].dt.day
flights['DayOfWeek'] = flights['FlightDate'].dt.dayofweek

# 5. Feature selection (using REAL column names)
features = [
    'Jet_Fuel_Price_USD_per_Gal',
    'Load Factor (%)',
    'Aircraft Utilization (Hours/Day)',
    'Maintenance Downtime (Hours)',
    'Operating Cost (USD)',
    'Revenue (USD)',
    'Fleet Availability (%)',
    'Delay (Minutes)',
    'Year', 'Month', 'Day', 'DayOfWeek'
]

target = 'Net Profit Margin (%)'

# Randomly sample 10% of the data
flights_sampled = flights.sample(frac=0.1, random_state=42)

# Use the sampled data for training
X = flights_sampled[features]
y = flights_sampled[target]

# 6. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Scale numeric features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 8. Random Forest model
rf = RandomForestRegressor(n_estimators=300, random_state=42)
rf.fit(X_train_scaled, y_train)
rf_pred = rf.predict(X_test_scaled)


# 9. XGBoost model
xgb = XGBRegressor(n_estimators=500, learning_rate=0.05, random_state=42)
xgb.fit(X_train_scaled, y_train)
xgb_pred = xgb.predict(X_test_scaled)

# 10. Evaluation function
def evaluate(model_name, y_true, y_pred):
    print(f"\n{model_name} Performance:")
    print(f"R² Score: {r2_score(y_true, y_pred):.4f}")
    print(f"Mean Absolute Error: {mean_absolute_error(y_true, y_pred):.4f}")

evaluate("Random Forest", y_test, rf_pred)
evaluate("XGBoost", y_test, xgb_pred)

# 11. Feature importance
importances = pd.Series(rf.feature_importances_, index=features)
print("\nTop Predictors of Profitability:")
print(importances.sort_values(ascending=False))





