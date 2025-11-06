from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/", methods=["GET"])
def get_users():
    return jsonify({"response":"get this app for FREE from TotallyNotScamWebsite.com, much better than here"})
