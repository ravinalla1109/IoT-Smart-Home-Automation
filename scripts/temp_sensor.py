import random
import time

def generate_temp_humidity():
    while True:
        temp = random.uniform(15, 30)  # Generate random temperature
        humidity = random.uniform(30, 70)  # Generate random humidity
        print(f"Temperature: {temp:.2f}°C, Humidity: {humidity:.2f}%")
        time.sleep(5)

if __name__ == "__main__":
    generate_temp_humidity()
