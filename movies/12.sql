SELECT title FROM movies, people, stars
WHERE movies.id in
(SELECT stars.movie_id FROM people, stars
WHERE people.id = stars.person_id AND name = "Johnny Depp")
AND stars.movie_id = movies.id AND people.id = stars.person_id AND name = "Helena Bonham Carter" ;