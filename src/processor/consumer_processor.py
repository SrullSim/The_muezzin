from kafka_files.consumer import Consumer
from src.elasticsearch_files.elastic_dal import ElasticDAL



class GetData:

    def __init__(self, topic_to_listen, index_name, create_index= False, mapping=None):
        self.consumer = Consumer(topic_to_listen)
        self.events = self.consumer.get_consumer_events()
        self.elastic_dal = ElasticDAL(index_name,create_index=create_index, mapping=mapping)



    def collect_the_data(self):
        """ Listens to the Topic constantly """
        try:
            for document in self.events:
                print(document.value)
                self.elastic_dal.insert_one_document(document.value)


        #         process and mapping


        except Exception as e :
            print("error: cant consume data: ", e)


if __name__ == "__main__":
    from config.config import LOADER_PUB_TOPIC, INDEX_NAME

    get = GetData(LOADER_PUB_TOPIC, INDEX_NAME)
    get.collect_the_data()
