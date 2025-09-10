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
