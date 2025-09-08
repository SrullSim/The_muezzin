from gridfs import GridFS
from pymongo import MongoClient
import gridfs
from config.config import MONGO_HOST
from src.mongo.mongo_crud import MongoCRUD


class MongoDal:

    def __init__(self,db_name, collection):
        self.db_name = db_name
        self.collection = collection
        self.uri = MONGO_HOST
        self.mongo_crud = MongoCRUD(db_name, collection)
        self.client = None


    def insert_one(self, document):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.insert_one(document)
            return result
        except Exception as e:
            print("error to insert mongodal :", e)
            return {"error :": e }
        finally:
            self.mongo_crud.close_connection()


    def insert_many(self, documents):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.insert_many(documents)
            return result
        except Exception as e :
            print("error to insert mongodal :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def get_all(self):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.get_all()
            return result
        except Exception as e:
            print("error to get MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def get_doc_by_id(self, doc_id):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.get_doc_by_id(doc_id)
            return result
        except Exception as e:
            print("error to get MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def delete_one_document(self,doc_id):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.delete_one(doc_id)
            return result
        except Exception as e:
            print("error to delete MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def update_document(self, doc_id, field, new_value):
        try:
            self.mongo_crud.open_connection()
            result = self.mongo_crud.update_one(doc_id, field, new_value)
            return result
        except Exception as e:
            print("error to update MongoDB :", e)
            return {"error :": e}
        finally:
            self.mongo_crud.close_connection()


    def read_file_content(self,  path_to_file):
        try:
            self.mongo_crud.open_connection()
            fs = GridFS(self.mongo_crud.client[self.db_name])
            with open(path_to_file, 'rb') as audio_file:
                file_id = fs.put(audio_file)

            return file_id
        except Exception as e:
            print("error to read file :", e)



if __name__ == "__main__":
    # for testing
    pass