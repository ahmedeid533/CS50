SELECT DISTINCT name FROM movies, people, stars
WHERE movies.id in
(SELECT stars.movie_id FROM people, stars
WHERE people.id = stars.person_id AND name = "Kevin Bacon" AND birth = 1958)
AND stars.movie_id = movies.id AND people.id = stars.person_id AND name != "Kevin Bacon";