SELECT
    t.id AS track_id,
    t.title,
    COUNT(*) AS plays,
    SUM(lh.listen_seconds) AS total_seconds
FROM listening_history lh
JOIN tracks t ON lh.track_id = t.id
GROUP BY t.id, t.title
ORDER BY plays DESC
LIMIT %(limit)s;