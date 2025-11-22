CREATE TABLE route_summary AS
SELECT
    Airline,
    COUNT(DISTINCT "Source airport") AS Unique_Source_Airports,
    COUNT(DISTINCT "Destination airport") AS Unique_Destination_Airports,
    COUNT(*) AS Total_Routes
FROM airline_routes
GROUP BY Airline;
