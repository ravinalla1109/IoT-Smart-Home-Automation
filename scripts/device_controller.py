 import requests

BASE_URL = "http://127.0.0.1:5000"  # Update with your deployed URL when ready

def turn_device_on(device):
    response = requests.post(f"{BASE_URL}/control", json={"device": device, "state": "on"})
    return response.json()

def turn_device_off(device):
    response = requests.post(f"{BASE_URL}/control", json={"device": device, "state": "off"})
    return response.json()

if __name__ == "__main__":
    print(turn_device_on("light"))
    print(turn_device_off("light"))

