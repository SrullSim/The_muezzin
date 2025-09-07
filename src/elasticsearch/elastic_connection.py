import time
from config.config import ELASTIC_HOST
from mapping import MAPPING
from pprint import pprint
from elasticsearch import Elasticsearch

class ElasticConnection:

    def __init__(self):
        self.es = self.get_es_client()

    def get_es_client(self, max_retries: int = 2, sleep_time: int = 3) -> Elasticsearch:
        i = 0
        while i < max_retries:
            try:
                es = Elasticsearch(ELASTIC_HOST)
                pprint("Connected to Elasticsearch!")
                return es
            except Exception:
                pprint("Could not connect to Elasticsearch, retrying...")
                time.sleep(sleep_time)
                i += 1
        raise ConnectionError("Failed to connect to Elasticsearch after multiple attempts.")
