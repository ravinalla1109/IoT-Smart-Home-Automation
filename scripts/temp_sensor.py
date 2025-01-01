import random
import time
import requests

BASE_URL = "http://127.0.0.1:5000"

def get_temperature():
    return round(random.uniform(20.0, 30.0), 2)

if __name__ == "__main__":
    while True:
        temp = get_temperature()
        response = requests.post(f"{BASE_URL}/control", json={"device": "temperature", "state": temp})
        print(f"Temperature Sent: {temp}, Response: {response.json()}")
        time.sleep(5)
