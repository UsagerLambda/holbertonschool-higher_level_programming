-- list all cities in database
SELECT cities.id, cities.name, states.name FROM cities, states ORDER BY id ASC;