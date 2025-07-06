import os
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from app.routes import routes
from app.models import get_all_events

load_dotenv()

app = Flask(__name__, template_folder="templates")
app.register_blueprint(routes)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events", methods=["GET"])
def fetch_events():
    events = get_all_events()
    return jsonify(events)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets this
    app.run(host="0.0.0.0", port=port, debug=True)
