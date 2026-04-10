SELECT *
FROM startups;

SELECT COUNT(DISTINCT name)
FROM startups;

SELECT SUM(valuation)
FROM startups;

SELECT MAX(raised)
FROM startups
WHERE stage = "Seed";

SELECT MIN(founded)
FROM startups;

SELECT AVG(valuation)
FROM startups;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2) AS average
FROM startups
GROUP BY category
ORDER BY average DESC;

SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(category) >= 3;

SELECT location, AVG(employees)
FROM startups
GROUP BY location;
SELECT location, AVG(employees)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;