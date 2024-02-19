import datetime as dt
import os
import time

import requests

API_KEY = os.environ["API_KEY"]
URL = os.environ["URL"]


def main():
    """
    This function will send events to the log enpoint.
    """
    event_id = 0

    header = {"X-API-Key": API_KEY}
    while event_id < 11:
        print(f"Sending event {event_id}")
        payload = {
            "id": "event_id",
            "source": "PAYMENTS" if event_id % 2 == 0 else "AUTH",
            "event_type": 1 if event_id % 2 == 0 else 2,
            "ts": str(dt.datetime.today()),
        }
        r = requests.post(URL, json=payload, headers=header)
        r.raise_for_status()

        time.sleep(10)
        event_id += 1


if __name__ == "__main__":
    main()
