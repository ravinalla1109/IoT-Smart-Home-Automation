 
import random
import time

def detect_motion():
    return random.choice([True, False])

if __name__ == "__main__":
    while True:
        print(f"Motion Detected: {detect_motion()}")
        time.sleep(3)
