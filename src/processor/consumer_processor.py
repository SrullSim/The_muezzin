from kafka_files.consumer import Consumer




class GetData:

    def __init__(self, topic_to_listen):
        self.consumer = Consumer(topic_to_listen)
        self.events = self.consumer.get_consumer_events()



    def collect_the_data(self):
        """ Listens to the Topic constantly """
        try:
            for event in self.events:
                print(event)

        #         process and mapping


        except Exception as e :
            print("error: cant consume data: ", e)


if __name__ == "__main__":
    from config.config import LOADER_PUB_TOPIC

    get = GetData(LOADER_PUB_TOPIC)
    get.collect_the_data()
