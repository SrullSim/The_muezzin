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

            self.producer.publish_message(self.topic_to_publish,data_to_publish)
            return True

        except Exception as e:
            print("error to publish : ", e )
            return False


if __name__ == "__main__":
    # for testing
    from config.config import LOADER_PUB_TOPIC

    p = PublishLoaderData(LOADER_PUB_TOPIC)
    l = Loader()
    print(p.publish_massage(l.collect_metadata()))