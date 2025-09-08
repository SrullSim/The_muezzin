from pymongo import MongoClient
from config.config import MONGO_HOST
from mongo_crud import MongoCRUD


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



if __name__ == "__main__":
    # for testing
    # from config.config import DB_NAME, COLLECTION_NAME
    # d = MongoDal(DB_NAME,COLLECTION_NAME)
    # data = {'download (9).wav': {'file_name': 'download (9).wav', 'unique_id': '20250907104952_1672890', 'file_size_in_byts': 1672890, 'file_create_time': 315522000000000000, 'file_modify_time': '20250907104952'}}
    #
    # res = d.insert_one(data)
    # print(res)
    # get = d.get_doc_by_id('68be86f922aae32eb47e5ed2')
    # print(get)
    pass