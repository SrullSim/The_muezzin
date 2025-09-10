import base64
import json
from logger.logger import Logger



class AnalysisData:

    def __init__(self, key_to_decrypt_words, path_to_dangerous_words, path_to_vdw,):
        self.key_to_decrypt_words = key_to_decrypt_words
        self.logger = Logger.get_logger()
        self.dangerous_words = self.load_words(path_to_dangerous_words)
        self.very_dangerous_words = self.load_words(path_to_vdw)


    def load_words(self,path_to_dangerous_words )-> list:
        """ got path to file with encrypt words and decrypt them
         :return list of this words """
        try:
            with open(path_to_dangerous_words, 'r') as file:
                json_data = json.load(file)
                data = base64.b64decode(json_data[self.key_to_decrypt_words]).decode('utf-8')
                list_of_words = data.lower().split(',')
                self.logger.info("words loaded successfully")
                return list_of_words
        except Exception as e:
            self.logger.info("words loaded failed")
            return None


if __name__ == "__main__":

    anls = AnalysisData("WORDS", 'BDS_WORDS/dangerous_words.json','BDS_WORDS/very_dangerous_words.json')
    print(anls.dangerous_words)