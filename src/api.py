from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": []})


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})
