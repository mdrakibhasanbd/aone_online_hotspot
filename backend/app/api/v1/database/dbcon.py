import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, BulkWriteError
from bson import ObjectId


# Load environment variables and connect to MongoDB
def get_mongo_db():
    try:
        load_dotenv()  # Load environment variables from a .env file
        mongo_replica = os.getenv("MONGO_URI")
        mongoDatabase = os.getenv("MONGO_DB_NAME")

        if not mongo_replica or not mongoDatabase:
            raise ValueError("Required environment variables are missing.")

        # Connect to MongoDB with a timeout
        mongo_client = MongoClient(mongo_replica, serverSelectionTimeoutMS=5000)
        db = mongo_client.get_database(mongoDatabase)
        print("Connected to MongoDB successfully.")
        return mongo_client, db

    except ValueError as ve:
        print(f"Configuration error: {ve}")
    except ServerSelectionTimeoutError as e:
        print(f"Server selection timeout error: {e}")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    return None, None

client, database = get_mongo_db()
address_collection = database.get_collection("address")

# Custom JSON encoder to handle ObjectId serialization
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)
