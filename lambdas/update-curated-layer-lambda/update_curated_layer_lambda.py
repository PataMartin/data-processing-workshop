import os

from pyathena import connect
from pyathena.pandas.cursor import PandasCursor


PREFIX = "event_logs"
CURATED_BUCKET = os.environ["CURATED_BUCKET"]
DB_NAME = os.environ["DB_NAME"]

conn = connect(
    s3_staging_dir=f"s3://{CURATED_BUCKET}/athena_queries", schema_name=DB_NAME
)


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

    cur = conn.cursor(cursor=PandasCursor)
    df = cur.execute(query).as_pandas()

    df.to_csv(f"s3://{CURATED_BUCKET}/{PREFIX}/event_logs.csv", index=False)
