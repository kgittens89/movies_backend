-- settings.sql
CREATE DATABASE movies;
CREATE USER moviesuser WITH PASSWORD 'movies';
GRANT ALL PRIVILEGES ON DATABASE movies TO moviesuser;