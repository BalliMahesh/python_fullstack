CREATE DATABASE jobhub;
USE jobhub;
CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    company VARCHAR(100),
    location VARCHAR(100),
    salary VARCHAR(50)
);
show tables;