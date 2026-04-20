
-- Assessing information from LYFT analytics to demonstrate skills in combining tables.

SELECT * FROM trips;

SELECT * FROM riders;

SELECT * FROM cars;

SELECT riders.first,
  riders.last,
  cars.model
FROM riders, cars;

SELECT *
FROM trips
LEFT JOIN riders
ON trips.rider_id = riders.id;

SELECT *
FROM trips
INNER JOIN cars
ON trips.car_id = cars.id;

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

SELECT AVG(cost) AS "Average Cost per trip"
FROM trips;

SELECT *
FROM riders
WHERE "total_trips" < 500;

SELECT *
FROM cars
WHERE "status" IS "active";

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;