SELECT AVG(rating) FROM ratings, movies
WHERE movies.id = ratings.movie_id AND year = '2012';