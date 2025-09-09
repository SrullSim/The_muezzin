from datetime import datetime, date
from bson import ObjectId
from pymongo import MongoClient
from config.config import MONGO_HOST,GRIDFS_CHUNKS_COLLECTION



class MongoCRUD:

    def __init__(self,db_name, collection):
        self.db_name = db_name
        self.collection = collection
        self.uri = MONGO_HOST
        self.client = None



    def open_connection(self):
        """ create connection to mongo db """
        try:
            self.client = MongoClient(self.uri)
            self.client.admin.command("ping")
            return True
        except Exception as e:
            self.client = None
            print("Error: ", e)
            return False


    def close_connection(self):
        if self.client:
            self.client.close()


    def insert_one(self, data):
        """ insert one document to mongodb """
        if self.client:
            db = self.client[self.db_name]
            collection = db[self.collection]
            results = collection.insert_one(data)

            return results


    def insert_many(self, data):
        """ insert many documents """
        if self.client:
            db = self.client[self.db_name]
            collection = db[self.collection]
            results = collection.insert_many(data)

            return results


    def get_all(self):
        """ get all the data from db """
        if self.client:
            db = self.client[self.db_name]
            collection = db[self.collection]
            data = collection.find({}, {"_id": 0})
            return list(data)


    def get_doc_by_id(self, doc_id):
        """ Get a document from MongoDB by its _id
        Args: doc_id (str): The document ID to retrieve
        Returns: dict: The document if found, None if not found """
        if self.client:
            try:
                db = self.client[self.db_name]
                collection = db[self.collection]

                # Convert string to ObjectId if needed
                if isinstance(doc_id, str):
                    doc_id = ObjectId(doc_id)

             # Find the document by _id, exclude _id from result
                document = collection.find_one({"_id": doc_id})
                return document
            except Exception as e:
                print(f"Error retrieving document: {e}")
                return None
        return None


    def get_doc_by_id_from_gridFS(self, id_to_search):
        """ Get a document from MongoDB by its _id
                Args: doc_id (str): The document ID to retrieve
                Returns: dict: The document if found, None if not found """
        if self.client:
            try:
                db = self.client[self.db_name]
                collection = db[GRIDFS_CHUNKS_COLLECTION]

                # Convert string to ObjectId if needed
                if isinstance(id_to_search, str):
                    id_to_search = ObjectId(id_to_search)

                # Find the document by _id, exclude _id from result
                document = collection.find_one({"_id": id_to_search})
                return document
            except Exception as e:
                print(f"Error retrieving document: {e}")
                return None
        return None


    def delete_one(self, id):
        """ delete one document by id given """
        if self.client:
            db = self.client[self.db_name]
            collection = db[self.collection]
            results = collection.delete_one({'id': id})
            return results


    def update_one(self, id, field, new_value):
        """ update one document """
        if self.client:
            db = self.client[self.db_name]
            collection = db[self.collection]
            results = collection.update_one({'_id': id}, {'$set': {field: new_value}})

            return results

