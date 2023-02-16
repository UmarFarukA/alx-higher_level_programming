--List all genres of the show `Dexter`
SELECT tg.name from tv_genres AS tg INNER JOIN tv_show_genres as tsg ON tg.id = tsg.genre_id INNER JOIN tv_shows as ts ON tsg.show_id = ts.id WHERE ts.title = 'Dexter' ORDER BY tg.name;
