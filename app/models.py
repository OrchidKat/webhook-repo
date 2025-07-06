from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import os

uri = os.getenv("MONGO_URI")
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["github_events"]
collection = db["events"]

def save_event(event_type, data):
    event = {
        "event_type": event_type,
        "author": data["author"],
        "from_branch": data.get("from_branch"),
        "to_branch": data["to_branch"],
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(event)

def get_all_events():
    return list(collection.find({}, {"_id": 0}))

# models.py
def get_all_events():
    try:
        return list(collection.find({}, {"_id": 0}))
    except Exception as e:
        print("MongoDB Error:", e)
        return []

