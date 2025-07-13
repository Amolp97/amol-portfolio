from flask import Flask, render_template, jsonify
import json

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
    app.run(debug=True)
