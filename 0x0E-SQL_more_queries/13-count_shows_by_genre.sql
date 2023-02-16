-- Create list of genres with the number of show
SELECT tg.name AS genre, COUNT(tsg.genre_id) AS number_of_shows FROM tv_genres AS tg INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id GROUP BY tg.name ORDER BY `number_of_shows` DESC;
