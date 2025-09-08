from src.elasticsearch_files.elastic_connection import ElasticConnection
from src.elasticsearch_files.mapping import MAPPING
from logger.logger import Logger

class IndexInit:

    def __init__(self,index_name, mapping=None):
        self.es = ElasticConnection().es
        self.index_name = index_name
        self.logger = Logger.get_logger()
        self.create_index()
        if mapping is None:
            self.create_mapping()



    def create_index(self):
        if not self.es.indices.exists(index=self.index_name):
            try:
                self.es.indices.create(index=self.index_name)
                self.logger.info(f"Index {self.index_name} created successfully.")
                print(f"Index {self.index_name} created successfully.")
            except Exception as e:
                print(f"Failed to create index {self.index_name}: {e}")
                self.logger.error(f"Failed to create index {self.index_name}: {e}")


    def create_mapping(self):
        try:
            self.es.indices.put_mapping(index=self.index_name, body=MAPPING)
            self.logger.info(f"mapping in {self.index_name} created successfully.")

        except Exception as e:
            self.logger.error(f"Failed to create mapping for index {self.index_name}: {e}")




    def delete_index(self):
        try:
            self.es.indices.delete(index=self.index_name, ignore_unavailable=True)
            print(f"Index {self.index_name} deleted successfully.")
            self.logger.info(f"Index {self.index_name} deleted successfully.")
        except Exception as e:
            self.logger.error(f"Failed to delete index {self.index_name}: {e}")