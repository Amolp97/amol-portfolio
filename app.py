from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    success = request.args.get("success")  # get success flag from query params
    return render_template("index.html", success=success)

# API to serve project data
@app.route("/api/projects")
def get_projects():
    with open("data/projects.json") as f:
        projects = json.load(f)
    return jsonify(projects)

# Contact form handler
@app.route("/send-message", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Log the message (or save it, or send an email later)
    print("Message from:", name)
    print("Email:", email)
    print("Content:", message)

    # Redirect back to homepage with success flag
    return redirect(url_for('home', success="true"))

# Run the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or fallback to 5000
    app.run(debug=False, host="0.0.0.0", port=port)
