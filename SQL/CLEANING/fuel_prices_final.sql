CREATE TABLE fuel_prices_final AS
SELECT
  DateText AS DateText_US,
  SUBSTR(DateText, 9, 4) || '-' ||           
  CASE SUBSTR(DateText, 1, 3)
    WHEN 'Jan' THEN '01' WHEN 'Feb' THEN '02'
    WHEN 'Mar' THEN '03' WHEN 'Apr' THEN '04'
    WHEN 'May' THEN '05' WHEN 'Jun' THEN '06'
    WHEN 'Jul' THEN '07' WHEN 'Aug' THEN '08'
    WHEN 'Sep' THEN '09' WHEN 'Oct' THEN '10'
    WHEN 'Nov' THEN '11' WHEN 'Dec' THEN '12'
  END || '-' || SUBSTR(DateText, 5, 2) AS Date_ISO,
  Jet_Fuel_Price_USD_per_Gal
FROM fuel_prices_clean;
