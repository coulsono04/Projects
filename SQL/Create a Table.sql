CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, "Ororo Munroe", 1940-05-30);

SELECT *
FROM friends;

INSERT INTO friends (id, name, birthday)
VALUES (2, "Morgan Thomas", 2004-03-09);

INSERT INTO friends (id, name, birthday)
VALUES (3, "Harvey Steadman", 2003-09-18);

UPDATE friends
SET name = "Storm"
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = "storm@codecademy.com"
WHERE id = 1;

UPDATE friends
SET email = "morgan@codecademy.com"
WHERE id = 2;

UPDATE friends
SET email = "harvey@codecademy.com"
WHERE id = 3;

DELETE FROM friends
WHERE id IS 1;

SELECT *
FROM friends;