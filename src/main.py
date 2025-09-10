from config.config import LOADER_PUB_TOPIC, INDEX_NAME,KEY_TO_DECRYPT_WORDS,PATH_TO_VERY_DANGEROUS_WORDS_FILE,PATH_TO_DANGEROUS_WORDS_FILE
from processor.consumer_processor import ControllerProcessData

class Main:


    def manager(self):
        self.manager = ControllerProcessData(LOADER_PUB_TOPIC, INDEX_NAME,KEY_TO_DECRYPT_WORDS,PATH_TO_DANGEROUS_WORDS_FILE,PATH_TO_VERY_DANGEROUS_WORDS_FILE)


    def run(self):
        self.manager.main_process()


run = Main()
run.run()