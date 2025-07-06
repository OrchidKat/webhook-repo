from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import os

uri = os.getenv("MONGO_URI")

# Ensure the client uses the latest secure API version
client = MongoClient(uri, server_api=ServerApi('1'))

# Optional: Validate connection (remove in production)
try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas")
except Exception as e:
    print("❌ MongoDB Connection Error:", e)

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
