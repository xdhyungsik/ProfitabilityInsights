CREATE TABLE monthly_averages AS
SELECT
    STRFTIME('%Y-%m', "Scheduled Departure Time") AS Month,
    AVG("Jet_Fuel_Price_USD_per_Gal") AS Avg_FuelPrice,
    AVG("Net Profit Margin (%)") AS Avg_ProfitMargin,
    AVG("Load Factor (%)") AS Avg_LoadFactor,
    AVG("Aircraft Utilization (Hours/Day)") AS Avg_Utilization,
    AVG("Operating Cost (USD)") AS Avg_OperatingCost
FROM flights_with_routes
GROUP BY Month
ORDER BY Month;
