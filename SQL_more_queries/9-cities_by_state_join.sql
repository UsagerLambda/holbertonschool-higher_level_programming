-- list all cities in database
SELECT cities.id, cities.name, states.name --selectionne les colonnes voulus
FROM cities, states --ou les colonnes vont être cherchées
WHERE cities.state_id = states.id --seulement les id dans la table cities correspondant à l'id dans states
ORDER BY cities.id ASC;
