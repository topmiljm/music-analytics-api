DROP TABLE IF EXISTS listening_history CASCADE;
DROP TABLE IF EXISTS track_genres CASCADE;
DROP TABLE IF EXISTS tracks CASCADE;
DROP TABLE IF EXISTS albums CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS artists CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    display_name TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    artist_id INT REFERENCES artists(id),
    release_year INT
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE tracks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    album_id INT REFERENCES albums(id),
    duration_seconds INT
);

CREATE TABLE track_genres (
    track_id INT REFERENCES tracks(id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY (track_id, genre_id)
);

CREATE TABLE listening_history (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    track_id INT REFERENCES tracks(id),
    listened_at TIMESTAMP DEFAULT NOW(),
    listen_seconds INT NOT NULL
);