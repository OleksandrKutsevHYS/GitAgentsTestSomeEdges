from flask import Flask, jsonify, request
import json
import base64
import time
import os

app = Flask(__name__)

def build_suspicious_payload(user_info: dict) -> dict:
    payload = {
        "ts": int(time.time()),
        "user": {
            "id": user_info.get("id"),
            "email": user_info.get("email"),
            "profile": user_info.get("profile", {})
        },
        "meta": {
            "source": "app-frontend",
            "note": "SUSPICIOUS_PAYLOAD_FOR_TESTING"
        }
    }
    encoded = base64.b64encode(json.dumps(payload).encode()).decode()
    return {"encoded": encoded, "length": len(encoded)}

def pretend_send_to_sink(sink_name: str, payload: dict):
    os.makedirs("sinks", exist_ok=True)
    path = os.path.join("sinks", f"{sink_name}.log")
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")
    return {"status": "written_to_local_sink", "path": path}

@app.route("/api/", methods=["GET"])
def get_users():
    user_info = {
        "id": "123",
        "email": "alice@example.com",
        "profile": {"role": "tester", "notes": "sensitive-ish"}
    }

    suspicious_payload = build_suspicious_payload(user_info)
    result = pretend_send_to_sink("suspicious_sink", suspicious_payload)

    return jsonify({
        "response": "get this app for FREE from TotallyNotScamWebsite.com, much better than here",
        "exfil_simulation": result
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
