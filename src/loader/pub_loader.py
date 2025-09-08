import json
from datetime import datetime, date

from kafka_files.producer import Producer
from loader import Loader



class PublishLoaderData:

    def __init__(self, topic_to_publish):
        self.producer = Producer()
        self.loader =  Loader()
        self.topic_to_publish = topic_to_publish


    def publish_massage(self, data_to_publish):
        """ publish the massage to kafka """
        try:
            # json_data = self.fix_json_serialization(data_to_publish)
            self.producer.publish_message(self.topic_to_publish,data_to_publish)
            return True

        except Exception as e:
            print("error to publish : ", e )
            return False


    def fix_json_serialization(self, data_to_publish):
        """  Fix JSON serialization issues for Kafka publishing
        Handles ObjectId, datetime, and other non-serializable types
        Args:
            data_to_publish: Data to fix (dict, list, or any type)
         Returns:
            JSON serializable data """
        if isinstance(data_to_publish, list):
            return [self.fix_json_serialization(item) for item in data_to_publish]

        elif isinstance(data_to_publish, dict):
            fixed_data = {}
            for key, value in data_to_publish.items():
                fixed_data[key] = self.fix_json_serialization(value)
            return fixed_data
        elif isinstance(data_to_publish, (datetime, date)):
            return data_to_publish.isoformat()

        else:
            return data_to_publish




if __name__ == "__main__":
    # for testing
    # from config.config import LOADER_PUB_TOPIC
    #
    # p = PublishLoaderData(LOADER_PUB_TOPIC)
    # l = Loader()
    # print(p.publish_massage(l.collect_metadata()))
    pass