import uuid
from pprint import pprint
from typing import List
from uuid import uuid4
from elasticsearch import helpers
from elasticsearch.helpers import bulk
from src.elasticsearch_files.elastic_connection import ElasticConnection
from src.elasticsearch_files.mapping import MAPPING


class ElasticCRUD:

    def __init__(self, index_name):
        self.es = ElasticConnection().es
        self.index_name = index_name


    def insert_one_document(self, data):
        """ Insert a single document into Elasticsearch.
        :param data:
        :return: """
        try:
            res = self.es.index(index=self.index_name, document=data)
            return res
        except Exception as e:
            print(f"Failed to insert data: {e}")



    def insert_data_bulk(self, data: List[dict]):
        """ Insert a pandas DataFrame into Elasticsearch using bulk API.
        Each row becomes a document."""
        try:
            actions = \
            [
                {
                    "_index": self.index_name,
                    "_id" :doc['unique_id'],
                    "_source": doc
                }
                for doc in data
            ]
            res = bulk(self.es, actions= actions, index=self.index_name)
            pprint(f"Bulk inserted successfully. Inserted {res[0]} documents.")

        except Exception as e:
            print(f"Failed to insert data: {e}")



    def search_data(self, query):
        """ Search for documents in Elasticsearch.
        :param query:
        :return: obj """
        try:
            res = self.es.search(index=self.index_name, body=query)
            return res
        except Exception as e:
            print(f"Failed to search data: {e}")