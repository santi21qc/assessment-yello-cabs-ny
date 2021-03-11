import logging

MSG_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
DATETIME_FORMAT = '%Y-%m-%d %I:%M:%S %p'

def get_logger(file_name: str):
    logging.basicConfig(format=MSG_FORMAT, datefmt=DATETIME_FORMAT)
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.INFO)
    return logger