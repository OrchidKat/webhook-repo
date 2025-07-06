from pymongo import MongoClient
from datetime import datetime
import os

# ✅ Use MONGO_URI with TLS enabled
mongo_uri = os.getenv("MONGO_URI")

# Important: Use tls=True if it's not already in the URI
client = MongoClient(mongo_uri, tls=True)

db = client["webhookdb"]  # ✅ Use the DB name from your URI
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
