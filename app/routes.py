from flask import Blueprint, request, jsonify
from app.models import save_event

routes = Blueprint('routes', __name__)

@routes.route("/webhook", methods=["POST"])
def github_webhook():
    payload = request.json
    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "push":
        data = {
            "author": payload["pusher"]["name"],
            "to_branch": payload["ref"].split("/")[-1]
        }

    elif event_type == "pull_request":
        # Check if this PR is merged
        if payload["action"] == "closed" and payload["pull_request"].get("merged"):
            event_type = "merge"  # ✅ change type
            data = {
                "author": payload["pull_request"]["merged_by"]["login"],
                "from_branch": payload["pull_request"]["head"]["ref"],
                "to_branch": payload["pull_request"]["base"]["ref"]
            }
        else:
            data = {
                "author": payload["pull_request"]["user"]["login"],
                "from_branch": payload["pull_request"]["head"]["ref"],
                "to_branch": payload["pull_request"]["base"]["ref"]
            }

    else:
        return jsonify({"status": "ignored"}), 200

    save_event(event_type, data)
    return jsonify({"status": "success"}), 201
