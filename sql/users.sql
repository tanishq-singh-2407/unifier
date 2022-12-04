CREATE TABLE users(
    email VARCHAR(60) PRIMARY KEY NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL default CURRENT_TIMESTAMP(),
    password_hash VARCHAR(60) NOT NULL
);