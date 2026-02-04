import os
import pymongo
from bson.objectid import ObjectId
from pymongo.synchronous.database import Database
from pymongo.synchronous.collection import Collection
from pymongo.synchronous.mongo_client import MongoClient

def create_connection() -> MongoClient:
    """
    Defines a Mongo client.
    
    Returns:
        MongoClient: The Mongo client.
    """
    mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI") + os.getenv("DATABASE_NAME"))

    try:
        mongo_client.admin.command("ping")
        return mongo_client
    except Exception as error:
        raise Exception(f"Unable to establish a connection to the database: {error}")

def create_database(mongo_client: MongoClient) -> Database:
    """
    Create a Mongo database.
    
    Args:
        mongo_client (MongoClient): The Mongo client.
    
    Returns:
        Database: The Mongo database.
    """
    try:
        mongo_database = getattr(mongo_client, os.getenv("DATABASE_NAME"))
        return mongo_database
    except Exception as error:
        raise Exception(f"The database could not be created: {error}")

def create_collection(mongo_database: Database) -> Collection:
    """
    Defines a collection in the Mongo database.
    
    Args:
        mongo_database (Database): A Mongo database.
    
    Returns:
        Collection: The defined collection.
    """
    try:
        mongo_collection = getattr(mongo_database, os.getenv("COLLECTION_NAME"))
        return mongo_collection
    except Exception as error:
        raise Exception(f"The collection could not be created: {error}")

def search_for_specific_file(mongo_collection: Collection, file_id: str) -> dict:
    """
    Search for a specific file in a collection in the Mongo database. 
    
    Args:
        mongo_collection (Collection): A collection.
        file_id (str): File ID have searched in the collection. 

    Returns:
        dict: File ID searched in a Mongo database collection.
    """
    try: 
        file_data = mongo_collection.find_one({"_id": ObjectId(file_id)})
        return file_data
    except Exception as error:
        raise Exception(f"The file could not be found in the database: {error}")

def drop_database():
    """
    Drop the SQLite database.
    """
    try:
        if os.path.exists(os.getenv("DATABASE_PATH")):
            os.remove(os.getenv("DATABASE_PATH"))
    except Exception as error:
        raise Exception(f"It was not possible to delete the database: {error}")
    
def calls_database_resources() -> Collection:
    """
    Calls the resources related to the Mongo database.
    
    Returns:
        Collection: A database Mongo collection.
    """
    mongo_client = create_connection()
    mongo_database = create_database(mongo_client)
    mongo_collection = create_collection(mongo_database)
    return mongo_collection