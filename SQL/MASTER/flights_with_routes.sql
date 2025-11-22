CREATE TABLE flights_with_routes AS
SELECT
    a.*,
    r.Unique_Source_Airports,
    r.Unique_Destination_Airports,
    r.Total_Routes
FROM flights_with_fuel a
LEFT JOIN route_summary r
    ON 1 = 1; 
