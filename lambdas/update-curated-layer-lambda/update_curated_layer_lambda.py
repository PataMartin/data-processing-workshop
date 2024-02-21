import os

import awswrangler as wr

PREFIX = "event_logs"
CURATED_BUCKET = os.environ["CURATED_BUCKET"]
DB_NAME = os.environ["DB_NAME"]


def lambda_handler(event: dict, context) -> None:
    """
    This lambda will recreate the curated layer on a schedule.

    Args:
    -----

    Returns:
    --------
    """
    query = """
        SELECT
            logs.id,
            source,
            ts,
            event_types.event_type
        FROM logs
        INNER JOIN event_types
        ON logs.event_type = event_types.id"""

    df = wr.athena.read_sql_query(sql=query, database=DB_NAME)

    df.to_csv(f"s3://{CURATED_BUCKET}/{PREFIX}/event_logs.csv", index=False)
