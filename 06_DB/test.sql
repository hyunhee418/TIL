-- CREATE TABLE friends(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- name TEXT,
-- location TEXT
-- );

-- INSERT INTO friends(name, location)
-- VALUES
-- ('Justin', 'Seoul'),
-- ('Simon', 'New York'),
-- ('Chang', 'Las Vegas'),
-- ('John', 'Sydney');

-- ALTER TABLE friends ADD COLUMN married INT;
UPDATE friends SET married = 1 WHERE id = 1;
UPDATE friends SET married = 0 WHERE id = 2;
UPDATE friends SET married = 0 WHERE id = 3;
UPDATE friends SET married = 1 WHERE id = 4;