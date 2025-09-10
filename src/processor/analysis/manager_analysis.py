from src.processor.analysis.analysis import AnalysisData
from logger.logger import Logger


class ManagerAnalysis:

    def __init__(self, key_to_decrypt_words,  path_to_dangerous_words, path_to_vdw):
        self.analyser = AnalysisData(key_to_decrypt_words,  path_to_dangerous_words, path_to_vdw)
        self.logger = Logger.get_logger()


    def main_analysis(self, text_to_check, threshold=0.12) -> dict:
        try:
            is_bds = False
            danger_rate = self.calculate_rate(text_to_check)
            if danger_rate > threshold :
                is_bds = True
            threat_level = self.analyser.classify_danger_level(danger_rate)

            result = { 'is_bds' : is_bds,
                       "bds_percent": danger_rate,
                       "bds_threat_level": threat_level
                       }
            self.logger.info("calculate rate done successfully")
            return result

        except Exception as e:
            self.logger.info(f"calculate rate failed{e}")
            return None




    def calculate_rate(self, text_to_check)-> float :
        """ calculate danger words percent to all the text """
        rate_dangerous_word = self.analyser.danger_rate(text_to_check, self.analyser.dangerous_words)

        rate_vdw = self.analyser.danger_rate(text_to_check, self.analyser.very_dangerous_words)

        calc_rate = rate_dangerous_word + (rate_vdw * 2 )

        return calc_rate








if __name__ == "__main__":
    text = "welcome resistance back ceasefire ceasefire flotilla today I can't stop free palestine thinking liberation about Gaza the blockade has turned daily life into a humanitarian crisis families can't even get clean water and the reports of war crimes it's overwhelming some call it genocide and honestly it feels that way when you see the destruction that's why groups like BTS keep pu"
    anls = ManagerAnalysis("WORDS", 'dangerous_words.json', 'very_dangerous_words.json')
    print(anls.main_analysis(text))