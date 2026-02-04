import os
import yaml
import base64
import pymongo
from pymongo.synchronous.database import Database
from pymongo.synchronous.collection import Collection
from pymongo.synchronous.mongo_client import MongoClient

def read_database_config_file():
    with open("../essay/database-config.yaml", "r") as file:
        loaded_data = yaml.safe_load(file)
    return loaded_data

def convert_pdf_to_base64(path_file: str) -> str:
    with open (path_file, "rb") as file:
        data = file.read()
    
    encoded_data = base64.b64encode(data)
    encoded_data = encoded_data.decode("utf-8")

    return encoded_data

def create_connection(loaded_data) -> MongoClient:
    mongo_client = pymongo.MongoClient(loaded_data["mongo_uri"] + loaded_data["database_name"])

    try:
        mongo_client.admin.command("ping")
        return mongo_client
    except Exception as error:
        raise Exception(f"Unable to establish a connection: {error}")

def create_database(mongo_client: MongoClient, loaded_data: dict) -> Database:
    mongo_database = getattr(mongo_client, loaded_data["database_name"])
    return mongo_database

def create_collection(mongo_database: Database, loaded_data: dict) -> Collection:
    mongo_collection = getattr(mongo_database, loaded_data["collection_name"])
    return mongo_collection

def insert_file_into_the_database(mongo_collection: Collection, loaded_data) -> bool:
    file_list = []

    for file_path in os.listdir(loaded_data["dir_path"]):
        file_list.append({"file": convert_pdf_to_base64(loaded_data["dir_path"] + file_path), "name": file_path})
    
    acknowledged = getattr(mongo_collection.insert_many(file_list), "acknowledged")
    return acknowledged

def main():
    loaded_data = read_database_config_file()

    mongo_client = create_connection(loaded_data)
    mongo_database = create_database(mongo_client, loaded_data)
    mongo_collection = getattr(mongo_database, loaded_data["collection_name"])

    acknowledged = insert_file_into_the_database(mongo_collection, loaded_data)
    if acknowledged is True:
        print("Documents successfully inserted!")

if __name__ == "__main__":
    main()
