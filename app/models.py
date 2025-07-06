from pymongo import MongoClient
from datetime import datetime
import os

mongo_uri = os.getenv("MONGO_URI")

# ✅ Ensure tls is enabled explicitly
client = MongoClient(mongo_uri, tls=True, tlsAllowInvalidCertificates=True)

# ✅ Use the correct DB name from your URI (like 'webhookdb')
db = client["webhookdb"]
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
