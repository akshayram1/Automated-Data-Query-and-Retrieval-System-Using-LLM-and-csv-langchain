from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME
import logging

class DatabaseManager:
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        self.connect()

    def connect(self):
        try:
            self.client = MongoClient(MONGODB_URI)
            self.client.admin.command('ismaster')  # Check if the connection is successful
            self.db = self.client[DATABASE_NAME]
            self.collection = self.db[COLLECTION_NAME]
            logging.info("Successfully connected to MongoDB")
        except ConnectionFailure:
            logging.error("Failed to connect to MongoDB")
            raise

    def insert_many(self, documents):
        try:
            result = self.collection.insert_many(documents)
            logging.info(f"Inserted {len(result.inserted_ids)} documents")
            return result.inserted_ids
        except OperationFailure as e:
            logging.error(f"Failed to insert documents: {e}")
            raise

    def execute_query(self, query):
        try:
            return list(self.collection.find(query))
        except OperationFailure as e:
            logging.error(f"Failed to execute query: {e}")
            raise

    def update_one(self, filter_query, update_data):
        try:
            result = self.collection.update_one(filter_query, {"$set": update_data})
            logging.info(f"Modified {result.modified_count} document")
            return result.modified_count
        except OperationFailure as e:
            logging.error(f"Failed to update document: {e}")
            raise

    def delete_one(self, filter_query):
        try:
            result = self.collection.delete_one(filter_query)
            logging.info(f"Deleted {result.deleted_count} document")
            return result.deleted_count
        except OperationFailure as e:
            logging.error(f"Failed to delete document: {e}")
            raise

    def get_collection_schema(self):
        try:
            sample_document = self.collection.find_one()
            if sample_document:
                return {key: type(value).__name__ for key, value in sample_document.items()}
            else:
                logging.warning("Collection is empty. Unable to infer schema.")
                return {}
        except OperationFailure as e:
            logging.error(f"Failed to get collection schema: {e}")
            raise

    def close_connection(self):
        if self.client:
            self.client.close()
            logging.info("MongoDB connection closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()