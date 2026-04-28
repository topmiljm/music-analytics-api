SELECT
    DATE(lh.listened_at) AS day,
    SUM(lh.listen_seconds) AS total_seconds,
    COUNT(*) AS plays
FROM listening_history lh
WHERE lh.user_id = %(user_id)s
GROUP BY day
ORDER BY day DESC;