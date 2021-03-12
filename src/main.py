import os
import pandas as pd
import exceptions
from response_handler import responseHandler
from logger_handler import get_logger
from bigquery_handler import getDatasetBQ
from math import radians, cos, sin, asin, sqrt


_LOGGER = get_logger(os.path.realpath(__file__))
_MASTER_DICT = {
    "passenger_count": "passengerCount",
    "total_time_minutes": "totalTimeMinutes",
    "number_trips": "numberOfTrips",
    "number_cabs_required": "numberOfCabsRequired"
}


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def main(event):
    _LOGGER.info("Starting process")

    getDataset = getDatasetBQ()
    query_to_execute = """SELECT vendor_id, passenger_count, dropoff_longitude, dropoff_latitude, pickup_datetime, dropoff_datetime FROM bigquery-public-data.new_york.tlc_yellow_trips_2016"""

    df = getDataset.execute_big_query(query_to_execute)

    # Getting only rides between 1 and 6 passengers
    df_filtered = df.loc[(df['passenger_count'] >= 1) & (df['passenger_count'] <= 6)]

    # Getting only valid longitudes [-99, 90]
    df_filtered = df_filtered.loc[(df_filtered['dropoff_longitude']>=-99) & (df_filtered['dropoff_longitude']<=90)]

    # Datetime type
    df_filtered[['pickup_datetime', 'dropoff_datetime']] = df_filtered[['pickup_datetime', 'dropoff_datetime']].apply(pd.to_datetime, format='%Y-%m-%d %H:%M:%S.%f') 

    # Filtering the droppingoff inside 3.5 km radius.
    statue_of_liberty_point = [{'lat': 40.6895436, 'lng': -74.0474287}]
    radius_threshold = 3.5 #In kilometer
    lat1 = statue_of_liberty_point[0]['lat']
    lon1 = statue_of_liberty_point[0]['lng']

    new_rows =  []
    df_final = pd.DataFrame()

    # Put in new column number of kilometers of distince to the statue of liberty
    df_filtered['radius_km'] = df_filtered.apply(lambda row: haversine(lon1, lat1, row.dropoff_longitude, row.dropoff_latitude), axis=1)
    
    # Filter by radius threshold
    df_final = df_filtered.loc[df_filtered['radius_km']<=radius_threshold]

    # Put in new column minutes of trip
    df_final['total_time_minutes'] = (df_final.dropoff_datetime - df_final.pickup_datetime).astype('timedelta64[m]').astype(int)
    
    # Build response
    df_groupby = df_final.groupby(["passenger_count"]).agg({'total_time_minutes': 'sum', 'radius_km': 'count', 'vendor_id': 'nunique'}).rename(columns={'total_time_minutes':'total_time_minutes', 'radius_km':'number_trips', 'vendor_id': 'number_cabs_required'})
    df_groupby = df_groupby.reset_index()

    response_handler = responseHandler(_MASTER_DICT)

    try:
        body_response = response_handler.build_body(df_groupby)
    except:
        _LOGGER.error("Something went wrong parsing response")
    else:
        return str(body_response)

if __name__ == "__main__":
    response = main("event")
    print(response)