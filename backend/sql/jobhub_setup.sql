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
insert into jobs(title,company,location,salary)
values('Frontend Developer', 'Nexus Labs', 'Remote', '₹5-8 LPA');
INSERT INTO jobs (title, company, location, salary)
VALUES ('Data Analyst Intern', 'BrightPath', 'Hyderabad', '₹15k/month');
INSERT INTO jobs (title, company, location, salary)
VALUES ('Junior Python Developer', 'PixelCraft', 'Bengaluru', '₹4-6 LPA');
select * from jobs
CREATE TABLE companies(
id INT AUTO_INCREMENT PRIMARY KEY,
name varchar(100),
email varchar(100)
);
INSERT INTO companies (name, email) VALUES ('PixelCraft', 'careers@pixelcraft.example');
INSERT INTO companies (name, email) VALUES ('Nexus Labs', 'careers@nexuslabs.example');
INSERT INTO companies (name, email) VALUES ('BrightPath', 'careers@brightpath.example');
select * from companies
ALTER TABLE jobs ADD COLUMN company_id INT;
DESCRIBE jobs;
ALTER TABLE jobs
ADD CONSTRAINT fk_company
FOREIGN KEY (company_id) REFERENCES companies(id);
SET SQL_SAFE_UPDATES = 0;
UPDATE jobs SET company_id = 1 WHERE company = 'PixelCraft';
UPDATE jobs SET company_id = 2 WHERE company = 'Nexus Labs';
UPDATE jobs SET company_id = 3 WHERE company = 'BrightPath';
SELECT * FROM jobs;