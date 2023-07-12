SELECT DISTINCT name FROM people, stars, movies
where people.id = stars.person_id and stars.movie_id = movies.id and year = 2004
ORDER BY birth;