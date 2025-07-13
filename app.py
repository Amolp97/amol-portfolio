from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# API to serve project data
@app.route("/api/projects")
def get_projects():
    with open("data/projects.json") as f:
        projects = json.load(f)
    return jsonify(projects)

# Run the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or fallback to 5000
    app.run(debug=False, host="0.0.0.0", port=port)
