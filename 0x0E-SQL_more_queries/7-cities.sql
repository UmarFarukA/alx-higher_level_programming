-- Creats database hbtn_0d_usa anda table 'cities'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	`id` INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREING KEY (state_id) REFERENCES states (state_id)
	);
