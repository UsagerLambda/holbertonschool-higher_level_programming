SELECT tv_genres.name -- selec name de la table tv_genres
FROM tv_shows  -- on part de la table tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter' -- Condition pour selec uniquement l'émission Dexter
ORDER BY tv_genres.name ASC;

-- JOIN 1 fait le lien entre les id des émissions et leurs lien avec un genre dans tv_show_genres
-- JOIN 2 fait le lien entre le genre dans tv_show_genres et l'id du nom du genre dans tv_genre