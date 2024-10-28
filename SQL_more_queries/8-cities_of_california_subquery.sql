-- list all the cities of california that can be found in the database
SELECT id, name FROM cities -- id dans cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California') -- Renvoie l'id de California dans states
ORDER BY id ASC; -- trié de manière ascendante