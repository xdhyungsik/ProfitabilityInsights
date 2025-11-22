import pandas as pd
import numpy as np

# Number of rows (REDUCED)
n = 5_000
np.random.seed(42)

# Helper for dates
dates = pd.date_range("2024-01-01", "2024-12-31", freq="H")
chosen_dates = np.random.choice(dates, size=n)

df = pd.DataFrame({
    "Flight Number": ["AA" + str(i).zfill(4) for i in np.random.randint(1, 9999, n)],
    "Scheduled Departure Time": chosen_dates,
    "Actual Departure Time": chosen_dates + pd.to_timedelta(
        np.random.normal(10, 25, n).clip(-20, 180),
        unit="m"
    ),
})

df["Delay (Minutes)"] = (df["Actual Departure Time"] - df["Scheduled Departure Time"]).dt.total_seconds()/60
df["Delay (Minutes)"] = df["Delay (Minutes)"].clip(lower=0)

df["Load Factor (%)"] = np.random.normal(80, 10, n).clip(40, 100)
df["Aircraft Utilization (Hours/Day)"] = np.random.normal(11, 2, n).clip(5, 16)
df["Turnaround Time (Minutes)"] = np.random.normal(70, 15, n).clip(30, 120)
df["Fleet Availability (%)"] = np.random.normal(92, 5, n).clip(70, 100)
df["Maintenance Downtime (Hours)"] = np.random.exponential(2, n).clip(0, 10)
df["Fuel Efficiency (ASK)"] = np.random.normal(3.5, 0.7, n).clip(1.5, 5.5)

# Monthly fuel prices
monthly_fuel_price = {m: p for m, p in zip(range(1, 13), np.random.uniform(2.2, 3.4, 12))}
df["Jet_Fuel_Price_USD_per_Gal"] = df["Scheduled Departure Time"].dt.month.map(monthly_fuel_price)

# Revenue
df["Revenue (USD)"] = (
    15000 +
    df["Load Factor (%)"] * 180 +
    df["Aircraft Utilization (Hours/Day)"] * 120 +
    np.random.normal(0, 1500, n)
).clip(3000, None)

# Costs
df["Operating Cost (USD)"] = (
    14000 +
    df["Delay (Minutes)"] * 8 +
    df["Maintenance Downtime (Hours)"] * 50 +
    df["Jet_Fuel_Price_USD_per_Gal"] * 600 +
    np.random.normal(0, 1200, n)
).clip(2000, None)

# Profit + Margin
df["Profit (USD)"] = df["Revenue (USD)"] - df["Operating Cost (USD)"]
df["Net Profit Margin (%)"] = (df["Profit (USD)"] / df["Revenue (USD)"]) * 100

# Additional KPIs
df["Ancillary Revenue (USD)"] = np.random.normal(1500, 400, n).clip(0, None)
df["Debt-to-Equity Ratio"] = np.random.uniform(0.4, 2.5, n)
df["Revenue per ASK"] = df["Revenue (USD)"] / np.random.uniform(10000, 20000, n)
df["Cost per ASK"] = df["Operating Cost (USD)"] / np.random.uniform(10000, 20000, n)

# AA network stats (static)
df["Unique_Source_Airports"] = 430
df["Unique_Destination_Airports"] = 432
df["Total_Routes"] = 2354

# Export
path = "/Users/xdhyungsik/Downloads/AA Profitability Project/AA_synthetic_5k_2.csv"
df.to_csv(path, index=False)

path
