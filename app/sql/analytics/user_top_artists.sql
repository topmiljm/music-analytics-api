SELECT
    a.id AS artist_id,
    a.name,
    COUNT(*) AS plays,
    SUM(lh.listen_seconds) AS total_seconds
FROM listening_history lh
JOIN tracks t ON lh.track_id = t.id
JOIN artists a ON t.artist_id = a.id
WHERE lh.user_id = %(user_id)s
GROUP BY a.id, a.name
ORDER BY plays DESC
LIMIT %(limit)s;