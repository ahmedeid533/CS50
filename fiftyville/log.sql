-- Keep a log of any SQL queries you execute as you solve the mystery.

-- READ description for crime scene
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = "Humphrey Street" AND year = 2021;

-- what intrviews has
SELECT transcript, name
FROM interviews
WHERE month = 7 AND day = 28 AND year = 2021;

-- bakery logs
SELECT *
FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10;
-- ATM
SELECT name,people.license_plate
FROM atm_transactions, bank_accounts, people, flights, passengers, bakery_security_logs
WHERE atm_location = "Leggett Street" AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.year = 2021
AND atm_transactions.account_number = bank_accounts.account_number
AND bank_accounts.person_id = people.id
AND people.passport_number = passengers.passport_number
AND passengers.flight_id = flights.id
AND flights.month = 7 AND flights.day = 29 AND flights.year = 2021 AND flights.hour <= 8
AND people.license_plate = bakery_security_logs.license_plate
AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.year = 2021;
-- susbect Bruce AND Luca
SELECT *
FROM phone_calls, people
WHERE month = 7 AND day = 28 AND year = 2021 AND duration < 60 AND caller = people.phone_number;
-- thift is Bruce
SELECT name FROM people WHERE phone_number = (
SELECT receiver
FROM phone_calls, people
WHERE month = 7 AND day = 28 AND year = 2021 AND duration < 60 AND people.name = "Bruce" AND caller = people.phone_number);
-- by help of robin
SELECT city FROM airports
WHERE id = 4;
SELECT destination_airport_id
FROM flights, passengers, people
WHERE month = 7 AND day = 29 AND year = 2021 AND people.name = "Bruce"
AND people.passport_number = passengers.passport_number AND passengers.flight_id = flights.id;
