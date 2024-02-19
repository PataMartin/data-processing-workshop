import json
import os

import boto3
import pandas as pd


PREFIX = "event_logs"
RAW_BUCKET = os.environ["RAW_BUCKET"]
REFINED_BUCKET = os.environ["REFINED_BUCKET"]

s3_client = boto3.client("s3")


def lambda_handler(event: dict, context) -> dict:
    """
    This lambda function will take the input events, dump then on the raw
    bucket, perform some transformations and dump the refined event on the
    refined bucket.

    Args:
    -----
        - event:
            {

            }
        - context
    Returns:
        {
            statusCode:
        }
    """
    try:
        print(f"Storing raw event: {event}")
        event_key = f"{PREFIX}/{event['id']}_{event['source']}.json"
        s3_client.put_object(
            Bucket=RAW_BUCKET, Key=event_key, Body=json.dumps(event)
        )

        print("Storing refined event")
        df = pd.DataFrame(event)
        df.to_parquet(
            f"s3://{REFINED_BUCKET}/{PREFIX}/{event['id']}_"
            f"{event['source']}.parquet",
            index=False,
        )
    except Exception as e:
        print(f"Error processing event: {e}")
        return {"statusCode": 500}

    return {"statusCode": 200}
