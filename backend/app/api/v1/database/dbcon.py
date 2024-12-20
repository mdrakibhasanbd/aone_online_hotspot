from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json
from bson import ObjectId
from pymongo.errors import ServerSelectionTimeoutError

def get_mongo_db():
    try:
        load_dotenv()
        mongoDatabase = os.getenv("MONGO_DB_NAME")
        mongo_replica = os.getenv("MONGO_REPLICA_URI")

        # mongo_client = MongoClient(mongoUri, int(mongoport))
        mongo_client = MongoClient(mongo_replica)
        db = mongo_client.get_database(mongoDatabase)
        return mongo_client, db
    except ServerSelectionTimeoutError as e:
        print(f"Server selection timeout error: {e}")
        # Handle the error (e.g., log, retry, return a default value)
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        # Handle the error as needed (e.g., log, raise, return a default value)
        return None

client, database = get_mongo_db()
# Ensure the connection is successful before proceeding
address_collection = database.get_collection("address")


# Custom JSON encoder to handle ObjectId serialization
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)
