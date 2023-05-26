-- a script that create a database htbn_0d_us and a table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL)
