from kafka_files.consumer import Consumer
from src.elasticsearch_files.elastic_dal import ElasticDAL
from src.mongo.mongo_dal import MongoDal
from config.config import DB_NAME, COLLECTION_NAME
from my_speech_app import Stt
from main_process import MainProcess
from logger.logger import Logger



class ControllerProcessData:

    def __init__(self, topic_to_listen, index_name,
                 key_to_decrypt_words, path_to_dangerous_words,path_to_vdw,
                 create_index= False, mapping=None,):
        self.consumer = Consumer(topic_to_listen)
        self.events = self.consumer.get_consumer_events()
        self.elastic_dal = ElasticDAL(index_name,create_index=create_index, mapping=mapping)
        self.mongo_dal = MongoDal(DB_NAME,COLLECTION_NAME)
        self.stt = Stt()
        self.processor = MainProcess(key_to_decrypt_words, path_to_dangerous_words,path_to_vdw)
        self.logger = Logger.get_logger()



    def main_process(self):
        """ Listens to the Topic constantly """
        try:
            for document in self.events:

                # extract the data from the event
                data_to_send = document.value

                #  split the data into list
                list_of_div_data = self.processor.div_and_build_the_data(data_to_send)


                data_to_elastic = list_of_div_data[0]
                data_to_mongodb = list_of_div_data[1]

                # send to mongodb
                self.mongo_dal.insert_one(data_to_mongodb)
                # send to index of Elasticsearch
                self.elastic_dal.insert_one_document(data_to_elastic)

            self.logger.info("event finished")
        except Exception as e :
            print("error: cant consume data: ", e)





if __name__ == "__main__":
    from config.config import (LOADER_PUB_TOPIC, INDEX_NAME,KEY_TO_DECRYPT_WORDS,
                               PATH_TO_VERY_DANGEROUS_WORDS_FILE,PATH_TO_DANGEROUS_WORDS_FILE)
    #
    get = ControllerProcessData(LOADER_PUB_TOPIC, INDEX_NAME,KEY_TO_DECRYPT_WORDS,
                                PATH_TO_DANGEROUS_WORDS_FILE,PATH_TO_VERY_DANGEROUS_WORDS_FILE)
    get.main_process()
    pass

