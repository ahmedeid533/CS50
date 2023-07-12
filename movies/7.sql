SELECT title, rating
FROM movies, ratings
WHERE movie_id = id and year = 2010 and rating > 0
ORDER BY rating DESC, title ASC;