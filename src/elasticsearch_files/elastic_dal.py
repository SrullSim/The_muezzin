from src.elasticsearch_files.elastic_crud import ElasticCRUD
from src.elasticsearch_files.index_init import IndexInit
from src.elasticsearch_files.elastic_connection import ElasticConnection

class ElasticDAL:

    def __init__(self, index_name, create_index=False, mapping=None):
        self.index_name = index_name
        self.crud = ElasticCRUD(index_name)
        if create_index:
            IndexInit(index_name,mapping)
        self.es = ElasticConnection().es


    def get_all_data(self):
            return self.crud.search_data({"query":{"match_all":{}}})


    def insert_one_document(self, document):
        return self.crud.insert_one_document(document)


    def insert_bulk(self,data: list[dict]):
        return self.crud.insert_data_bulk(data)

