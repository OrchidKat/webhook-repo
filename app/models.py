from pymongo import MongoClient
from datetime import datetime
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
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
