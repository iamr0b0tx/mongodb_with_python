from pymongo import MongoClient
from pymongo import errors


class MongoDB:
    def __init__(self, username: str, password: str, dbname: str, collection_name: str):
        try:
            self._client = self.connect(username, password)
            self.connection_status = self._client.is_mongos
            self._db = self._client[dbname][collection_name]

        except errors.ConnectionFailure as e:
            raise errors.ConnectionFailure(f"Unable to connect to database: {e}")

    @staticmethod
    def connect(username: str, password: str):
        # connect to the mongo
        return MongoClient(
            f"mongodb+srv://{username}:{password}@cluster0.6zd4q.mongodb.net/?retryWrites=true&w=majority"
        )

    def create(self, query_document: dict) -> bool:
        """
        returns True if successfully created document, False otherwise
        """
        try:
            self._db.insert_one(query_document)
            return True

        except errors.PyMongoError as e:
            return False

    def read(self, query_document: dict):
        """
        returns a cursor of successfully read documents, throws error otherwise
        """
        return self._db.find(query_document)

    def update(self, query_document: dict, new_document: dict):
        """
        returns JSON of successfully updated documents, throws error otherwise
        """
        docs = {}
        for doc in self._db.find(query_document):
            self._db.replace_one(doc, new_document)
            docs[doc["_id"]] = doc
        return docs

    def delete(self, query_document: dict):
        """
        returns JSON of successfully updated documents, throws error otherwise
        """
        docs = {}
        for doc in self._db.find(query_document):
            self._db.delete_one(doc)
            docs[doc["_id"]] = doc
        return docs
