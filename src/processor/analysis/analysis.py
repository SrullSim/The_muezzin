import base64
import json
from logger.logger import Logger
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



class AnalysisData:

    def __init__(self, key_to_decrypt_words, path_to_dangerous_words, path_to_vdw):
        self.key_to_decrypt_words = key_to_decrypt_words
        self.logger = Logger.get_logger()
        self.dangerous_words = self.load_words_danger(path_to_dangerous_words[0])
        self.very_dangerous_words = self.load_words(path_to_vdw)



    def load_words_danger(self,path_to_dangerous_words):
        try:
            print(path_to_dangerous_words)
            with open(path_to_dangerous_words, 'r') as file:
                json_words = json.load(file)
                print(type(json_words))
                words = base64.b64decode(json_words[self.key_to_decrypt_words]).decode('utf-8')
                list_of_words = words.lower().split(',')
                self.logger.info("words loaded successfully")
                return list_of_words
        except Exception as e:
            self.logger.info(f"words loaded from {path_to_dangerous_words} failed: {e}")
            return None


    def load_words(self,path_to_dangerous_words)-> list[str] | None:
        """ got path to file with encrypt words and decrypt them
         :return list of this words """
        try:
            print(path_to_dangerous_words)
            with open(path_to_dangerous_words, 'r') as file:
                json_words = json.load(file)
                print(type(json_words))
                words = base64.b64decode(json_words[self.key_to_decrypt_words]).decode('utf-8')
                list_of_words = words.lower().split(',')
                self.logger.info("words loaded successfully")
                return list_of_words
        except Exception as e:
            self.logger.info(f"words loaded from {path_to_dangerous_words} failed: {e}")
            return None


    def clean_text_and_remove_stop_words(self, text) -> str:
        nltk.download('stopwords', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text.lower())
        filtered_tokens = [word for word in tokens if word not in stop_words]
        text = re.sub(r'[^\w\s]', '', text.lower())
        return  " ".join(filtered_tokens)


    def danger_rate(self, text_to_check, words_to_check)-> float:
        clean_text = self.clean_text_and_remove_stop_words(text_to_check)
        words = clean_text.split()
        total_words = len(words)
        word_counts = Counter(words)
        dangerous_count = sum(word_counts[word.lower()] for word in words_to_check)
        if total_words == 0:
            return 0
        return dangerous_count / total_words

    def classify_danger_level(self, ratio)-> str:
        if ratio > 0.20:
            return "high"
        elif ratio > 0.10:
            return "medium"
        else:
            return "none"




if __name__ == "__main__":
    pass




