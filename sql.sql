CREATE DATABASE login_system;
USE login_system;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
INSERT INTO users (email, password) VALUES ('test@example.com', '1234');
