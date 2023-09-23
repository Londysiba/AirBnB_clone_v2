-- a script to prepare a MySQL server for the project
-- query that sets up database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- query that creates new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- query that grants basic usage
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- query that grants select privelges on performance shema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- query that granst all privileges on hbnbh_dev
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
