import os
import pandas as pd
import exceptions
from logger_handler import get_logger
from bigquery_handler import getDatasetBQ

_LOGGER = get_logger(os.path.realpath(__file__))


def main(event, _):
    _LOGGER.info("Starting process")

    getDataset = getDatasetBQ()
    query_to_execute = """SELECT vendor_id, passenger_count, dropoff_longitude, dropoff_latitude, pickup_datetime, dropoff_datetime FROM bigquery-public-data.new_york.tlc_yellow_trips_2016 limit 10"""

    df = getDataset.execute_big_query(query_to_execute)

    # Getting only rides between 1 and 6 passengers
    df_filtered = df.loc[(df['passenger_count'] >= 1) & (df['passenger_count'] <= 6)]

    # Getting only valid longitudes [-99, 90]
    df_filtered = df_filtered.loc[(df_filtered['dropoff_longitude']>=-99) & (df_filtered['dropoff_longitude']<=90)]

    print(df_filtered)

if __name__ == "__main__":
    main("event", None)