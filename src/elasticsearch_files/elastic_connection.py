import time
from config.config import ELASTIC_HOST
from src.elasticsearch_files.mapping import MAPPING
from pprint import pprint
from elasticsearch import Elasticsearch
from logger.logger import Logger

class ElasticConnection:

    def __init__(self):
        self.es = self.get_es_client()
        self.logger = Logger.get_logger()

    def get_es_client(self, max_retries: int = 2, sleep_time: int = 3) -> Elasticsearch:
        i = 0
        while i < max_retries:
            try:
                es = Elasticsearch(ELASTIC_HOST)
                pprint("Connected to Elasticsearch!")
                self.logger.info("Connected to Elasticsearch!")
                return es
            except Exception:
                pprint("Could not connect to Elasticsearch, retrying...")
                time.sleep(sleep_time)
                i += 1
        self.logger.error("Failed to connect to Elasticsearch after multiple attempts.")
        raise ConnectionError("Failed to connect to Elasticsearch after multiple attempts.")
