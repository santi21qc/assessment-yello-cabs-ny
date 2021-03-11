import os
import pandas as pd
from logger_handler import get_logger

_LOGGER = get_logger(os.path.realpath(__file__))

class responseHandler:
    def __init__(self, master_dict):
        self.str_columns=['passenger_count', 'total_time_minutes', 'number_trips', 'number_cabs_required']
        self.master_dict = master_dict
    
    def build_body(self, df):
        for col in self.str_columns:
            df[col] = df[col].apply(lambda v: int(v) if not pd.isnull(v) else None).tolist()

        for k, v in self.master_dict.items():
            df = df.rename(columns={k: v})

        records = df.to_dict("records")

        return records
