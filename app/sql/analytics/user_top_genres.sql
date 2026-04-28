SELECT
    g.id AS genre_id,
    g.name,
    COUNT(*) AS plays,
    SUM(lh.listen_seconds) AS total_seconds
FROM listening_history lh
JOIN tracks t ON lh.track_id = t.id
JOIN track_genres tg ON t.id = tg.track_id
JOIN genres g ON tg.genre_id = g.id
WHERE lh.user_id = %(user_id)s
GROUP BY g.id, g.name
ORDER BY plays DESC
LIMIT %(limit)s;