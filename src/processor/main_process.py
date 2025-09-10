from analysis.manager_analysis import ManagerAnalysis
from src.elasticsearch_files.elastic_dal import ElasticDAL
from src.mongo.mongo_dal import MongoDal
from config.config import DB_NAME, COLLECTION_NAME
from my_speech_app import Stt
from logger.logger import Logger


class MainProcess:


    def __init__(self, key_to_decrypt_words, path_to_dangerous_words, path_to_vdw):
        self.mongo_dal = MongoDal(DB_NAME, COLLECTION_NAME)
        self.stt = Stt()
        self.processor = ManagerAnalysis(key_to_decrypt_words,  path_to_dangerous_words, path_to_vdw)
        self.logger = Logger.get_logger()

    def div_and_build_the_data(self, data_to_process):
        try:

            if data_to_process:
                # push to mongodb by GridFS lib and get the id given
                file_id = self.mongo_dal.load_data_to_mongo_with_GridFS(data_to_process['file_details']['file_path'])

                # extract the content in text
                text = self.file_transcribe(file_id)

                bds_data = self.processor.main_analysis(text)

                # build the dict to send to elastic index
                data_to_elastic = {'file_name': data_to_process['file_details']['file_name'],
                                   'file_path': data_to_process['file_details']['file_path'],
                                   'unique_id': data_to_process['file_details']['unique_id'],
                                   'file_size_in_byts': data_to_process['file_details']['file_size_in_byts'],
                                   'file_create_time': data_to_process['file_details']['file_create_time'],
                                   'file_modify_time': data_to_process['file_details']['file_modify_time'],
                                   "is_bds": bds_data['is_bds'],
                                   "bds_percent": bds_data['bds_percent'],
                                   "bds_threat_level": bds_data['bds_threat_level'],
                                   'content_file': text
                                   }

                data_to_mongodb = {'_id':file_id}

                return [data_to_elastic,data_to_mongodb]
            else:
                print("div_the_data failed")
                return None

        except Exception as e :
            self.logger.info("div_and_build_the_data failed")


    def file_transcribe(self, id_of_doc):
        """ :return content file from byts to text """
        document = self.mongo_dal.get_doc_by_id_from_gridFS(id_of_doc)
        return self.stt.transcribe_content_from_binary_to_text(document)
