SELECT name FROM people, stars, movies
WHERE people.id = stars.person_id and stars.movie_id = movies.id and title = "Toy Story";