from flask import Flask, jsonify, render_template
from app.routes import routes
from app.models import get_all_events

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
    app.run(debug=True)
