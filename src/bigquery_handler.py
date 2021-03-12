import sys
import os
sys.path[0] += "\\site-packages"

from google.cloud import bigquery
from logger_handler import get_logger
from exceptions import ClientConnectionError
# from google.cloud import bigquery_storage

_LOGGER = get_logger(os.path.realpath(__file__))


class getDatasetBQ:
    def __init__(self):
        self.gcp_project = 'intense-base-307119'
        self.bq_dataset = 'yellow_cabs_ny_2016'
        self._make_clients(self.gcp_project, self.bq_dataset)

    def _make_clients(self, gcp_project, bq_dataset):
        try:
            self.client = bigquery.Client(project=gcp_project)
            self.dataset_ref = self.client.get_dataset(bq_dataset)
        except:
            msg = 'Error creating client connection'
            _LOGGER.error(msg)
            raise ClientConnectionError(msg)
        else:
            _LOGGER.info('Client connection created successfully')

    def execute_big_query(self, sql_query):

        """
        params:
        :sql_query query to execute
        
        return:
        """

        try:
            _LOGGER.info(f"Executing query {sql_query}")
            query = self.client.query(sql_query)
        except Exception as e:
            _LOGGER.error(f"Error executing SQL {sql_query}")
            _LOGGER.error(str(e))
            raise Exception(e)
        else:
            _LOGGER.info("Query executed successfully")
            results = query.result()
            return results.to_dataframe()

# query = """Select * FROm bigquery-public-data.new_york.tlc_yellow_trips_2016 limit 10"""
# # query = """Select * ny_cabs_2016 limit 100"""

# df = gcptodf(query)
# print(df.columns)