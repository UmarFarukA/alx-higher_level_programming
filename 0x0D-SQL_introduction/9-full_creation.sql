-- Creates a second_table and inserts multiple records
CREATE TABLE IF NOT EXISTS second_table(`id` INT PRIMARY KEY, `name` VARCHAR(256) NOT NULL,`store` INT);
INSERT INTO second_table(id, name, store) VALUES (1, 'John' 10);
INSERT INTO second_table(id, name, store) VALUES(2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES(3, 'Bob', 14);
INSERT INTO second_table(id, name, store) VALUES(4, 'George', 8);
