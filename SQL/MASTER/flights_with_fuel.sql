CREATE TABLE flights_with_fuel AS
SELECT
    a.*,
    f.Jet_Fuel_Price_USD_per_Gal
FROM "Aviation_KPIs_Dataset" a
LEFT JOIN fuel_prices_final f
    ON DATE(a."Scheduled Departure Time") = f.Date_ISO;
