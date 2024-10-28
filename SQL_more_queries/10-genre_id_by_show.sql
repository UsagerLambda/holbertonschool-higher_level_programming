-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id --(selectionne les genre associés aux shows)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
