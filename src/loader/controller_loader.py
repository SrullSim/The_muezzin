from loader import Loader
from pub_loader import PublishLoaderData
from config.config import LOADER_PUB_TOPIC
from logger.logger import Logger




class ControlLoader:

    def __init__(self):
        self.publish_data = PublishLoaderData(LOADER_PUB_TOPIC)
        self.data_to_publish = Loader().collect_metadata()
        self.logger = Logger.get_logger()


    def send_all_files_to_kafka(self):
        """ send each file at the time (to distribute loads) """
        for file in self.data_to_publish:

            self.publish_data.publish_massage(file)

        self.logger.info("data publish to kafka consumer")
        return {"status": "all the files published "}


if __name__ == "__main__":
    # for testing
    from config.config import LOADER_PUB_TOPIC
    c = ControlLoader()
    print(c.send_all_files_to_kafka())
    pass

