SELECT title FROM movies, ratings, people, stars
WHERE people.id = stars.person_id  AND stars.movie_id = movies.id AND people.name = "Chadwick Boseman" and movies.id = ratings.movie_id
ORDER BY rating DESC LIMIT 5;