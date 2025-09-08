from kafka_files.consumer import Consumer
from src.elasticsearch_files.elastic_dal import ElasticDAL
from src.mongo.mongo_dal import MongoDal
from config.config import DB_NAME, COLLECTION_NAME
from gridfs import GridFS



class ControllerProcessData:

    def __init__(self, topic_to_listen, index_name, create_index= False, mapping=None):
        self.consumer = Consumer(topic_to_listen)
        self.events = self.consumer.get_consumer_events()
        self.elastic_dal = ElasticDAL(index_name,create_index=create_index, mapping=mapping)
        self.mongo_dal = MongoDal(DB_NAME,COLLECTION_NAME)


    def collect_the_data(self):
        """ Listens to the Topic constantly """
        try:
            for document in self.events:
                data_to_send = document.value

                list_of_div_data = self.div_the_data(data_to_send)

                # send to index of Elasticsearch
                data_to_elastic = list_of_div_data[0]
                data_to_mongodb = list_of_div_data[1]

                self.elastic_dal.insert_one_document(data_to_elastic)
                self.mongo_dal.insert_one(data_to_mongodb)

        except Exception as e :
            print("error: cant consume data: ", e)


    def div_the_data(self, document):
        if document:

            data_to_elastic = {'file_name': document['file_details']['file_name'],
                               'file_path': document['file_details']['file_path'],
                               'unique_id': document['file_details']['unique_id'],
                               'file_size_in_byts': document['file_details']['file_size_in_byts'],
                               'file_create_time': document['file_details']['file_create_time'],
                               'file_modify_time': document['file_details']['file_modify_time']
                               }
            content_file = self.mongo_dal.read_file_content(document['file_details']['file_path'])
            data_to_mongodb = {'_id':content_file}

            return [data_to_elastic,data_to_mongodb]
        else:
            return None





if __name__ == "__main__":
    # from config.config import LOADER_PUB_TOPIC, INDEX_NAME
    #
    # get = ControllerProcessData(LOADER_PUB_TOPIC, INDEX_NAME)
    # get.collect_the_data()
    pass