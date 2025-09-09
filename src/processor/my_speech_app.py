import speech_recognition as sr
import io
from logger.logger import Logger


class Stt:

    def __init__(self):
        self.logger = Logger.get_logger()
        self.recognizer = sr.Recognizer()


    def convert_file(self, file_to_transcribe):

        audio_bytes = file_to_transcribe

        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio = self.recognizer.record(source)

            print("audio", audio)
            try:
                text = self.recognizer.recognize_google(audio_data=audio)
                self.logger.info("stt successfully")
                return text

            except sr.UnknownValueError:
                self.logger.error("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                self.logger.error(f"Could not request results from Google Speech Recognition service; {e}")

            except Exception as e:
                print("error: read from binary file", e)
                self.logger.error("error: read from binary file", e)


if __name__ == "__main__":
    # from src.mongo.mongo_dal import MongoDal
    # from config.config import DB_NAME,COLLECTION_NAME_testing
    #
    # d = MongoDal(DB_NAME,COLLECTION_NAME_testing)
    # file = d.get_doc_by_id("68bedc798b2437a99797b0bc")
    # stt = Stt(file['data'])
    pass

