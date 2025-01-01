from flask import Flask, request, jsonify

app = Flask(__name__)

devices = {"light": "off", "temperature": 0, "motion": False}

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(devices)

@app.route("/control", methods=["POST"])
def control_device():
    data = request.json
    device, state = data.get("device"), data.get("state")
    if device in devices:
        devices[device] = state
        return jsonify({"message": f"{device} turned {state}"}), 200
    return jsonify({"error": "Invalid device"}), 400

if __name__ == "__main__":
    app.run(debug=True)

