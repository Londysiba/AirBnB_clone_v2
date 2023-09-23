-- a script to prepare a MySQL server for the project
-- query that sets up database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- query that creates new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- query that grants basic usage
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';

-- query that grants select privelges on performance shema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- query that grants all privileges on hbnbh_test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
