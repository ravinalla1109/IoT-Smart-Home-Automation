import jwt
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing"}), 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 403
        return func(*args, **kwargs)
    return wrapper

@app.route('/status', methods=['GET'])
@token_required
def get_status():
    # Same as previous
    pass

@app.route('/control', methods=['POST'])
@token_required
def control_device():
    # Same as previous
    pass

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
