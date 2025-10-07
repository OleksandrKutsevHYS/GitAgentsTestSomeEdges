from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": []})


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/api/export', methods=['POST'])
def export_data():
    format = request.json.get('format', 'json')
    data = get_all_user_data()
    
    if format == 'csv':
        return generate_csv(data)
    return jsonify(data)