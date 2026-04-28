INSERT INTO users (email, display_name) VALUES
('alice@example.com', 'Alice'),
('bob@example.com', 'Bob');

INSERT INTO artists (name) VALUES
('Radiohead'),
('Daft Punk');

INSERT INTO albums (title, artist_id, release_year) VALUES
('OK Computer', 1, 1997),
('Discovery', 2, 2001);

INSERT INTO genres (name) VALUES
('Alternative'),
('Electronic'),
('Rock');

INSERT INTO tracks (title, album_id, duration_seconds) VALUES
('Paranoid Android', 1, 386),
('Karma Police', 1, 260),
('Harder Better Faster Stronger', 2, 224);

INSERT INTO track_genres (track_id, genre_id) VALUES
(1, 1),
(1, 3),
(2, 1),
(3, 2);

INSERT INTO listening_history (user_id, track_id, listen_seconds) VALUES
(1, 1, 300),
(1, 1, 200),
(1, 2, 180),
(2, 3, 220),
(2, 3, 210);