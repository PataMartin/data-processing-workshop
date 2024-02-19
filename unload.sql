UNLOAD
(
    SELECT
        logs.id,
        source,
        ts,
        event_types.event_type
    FROM logs
    INNER JOIN event_types
    ON logs.event_type = event_types.id
)
TO 's3://curated-bucket-development-dev/event_logs/2024-02-19/'
WITH (format = 'TEXTFILE')
