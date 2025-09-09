from gridfs import GridFS
from pymongo import MongoClient
import gridfs
from config.config import MONGO_HOST
from src.mongo.mongo_crud import MongoCRUD
from logger.logger import Logger


class MongoDal:

    def __init__(self,db_name, collection):
        self.db_name = db_name
        self.collection = collection
        self.uri = MONGO_HOST
        self.mongo_crud = MongoCRUD(db_name, collection)
        self.client = None
        self.logger = Logger.get_logger()


    def insert_one(self, document):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.insert_one(document)
            self.logger.info("insert one document")
            return result
        except Exception as e:
            self.logger.error("error to insert mongodal :", e)

            return {"error :": e }
        finally:
            self.mongo_crud.close_connection()


    def insert_many(self, documents):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.insert_many(documents)
            self.logger.info("insert all documents")
            return result
        except Exception as e :
            self.logger.error("error to insert mongodal :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def get_all(self):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.get_all()
            self.logger.info("get all data successfully")
            return result
        except Exception as e:
            self.logger.error("error to get MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def get_doc_by_id(self, doc_id):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.get_doc_by_id(doc_id)
            self.logger.info("get the doc by id successfully")
            return result
        except Exception as e:
            self.logger.error("error to get MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def delete_one_document(self,doc_id):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.delete_one(doc_id)
            self.logger.info("data deleted successfully")
            return result
        except Exception as e:
            self.logger.error("error to update MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def update_document(self, doc_id, field, new_value):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.update_one(doc_id, field, new_value)
            self.logger.info("update data successfully")
            return result
        except Exception as e:
            self.logger.error("error to update MongoDB :", e)

            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def load_data_to_mongo_with_GridFS(self, path_to_file):
        """ read the content of a file
        param: path to the current file
        return: id  """
        try:
            self.mongo_crud.open_connection()
            fs = GridFS(self.mongo_crud.client[self.db_name])
            with open(path_to_file, 'rb') as audio_file:

                file_id = fs.put(audio_file)
            self.logger.info("load file with GridFS successfully")
            return file_id
        except Exception as e:
            self.logger.error("read file failed because: ", e)


    def get_doc_by_id_from_gridFS(self, id_to_search):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.get_doc_by_id_from_gridFS(id_to_search)
            self.logger.info("get the doc by id from GridFS was successfully")
            if result:
                return result
            else:
                print("get_doc_by_id_from_gridFS failed ")
                self.logger.info("get_doc_by_id_from_gridFS failed ")
        except Exception as e:
            self.logger.error("error to get MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


if __name__ == "__main__":
    # for testing
    pass