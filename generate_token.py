import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'secret_key'

def generate_token():
    payload = {
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

if __name__ == "__main__":
    print("JWT Token:", generate_token())
