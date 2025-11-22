CREATE TABLE fuel_prices_clean AS
SELECT
  TRIM("Back to Contents") AS DateText,
  CAST(TRIM("Data 1: U.S. Gulf Coast Kerosene-Type Jet Fuel Spot Price FOB (Dollars per Gallon)") AS REAL)
      AS Jet_Fuel_Price_USD_per_Gal
FROM "Jet_fuel_prices"
WHERE "Back to Contents" NOT IN ('Sourcekey', 'Date', '', ' ')
  AND "Data 1: U.S. Gulf Coast Kerosene-Type Jet Fuel Spot Price FOB (Dollars per Gallon)" NOT IN ('', 'NA');
