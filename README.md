# IoT Smart Home Automation

## Overview
The **IoT Smart Home Automation** project showcases an advanced implementation of a Python-based system for controlling and monitoring home devices. This project leverages APIs for device communication and lays the foundation for future cloud integration, enabling seamless remote access and data analytics. It is designed to demonstrate both the simplicity and scalability of IoT solutions.

## Features
- **Device Control**: APIs for controlling devices like lights, temperature sensors, and motion detectors.
- **Real-Time Monitoring**: Simulated IoT sensors provide dynamic data visualization.
- **Scalability**: Framework ready for integration with cloud platforms (AWS IoT Core, Google Cloud IoT).
- **Extensibility**: Modular design for adding new devices and sensors.
- **Security**: Basic token-based authentication for API endpoints.
- **Future Enhancements**: Cloud data storage, MQTT messaging, and advanced analytics.

## Advanced Project Structure
```
IoT-Smart-Home-Automation/
│
├── backend/
│   ├── app.py              # Flask API for handling device control and monitoring
│   ├── requirements.txt    # Dependencies for the backend API
│
├── scripts/
│   ├── temp_sensor.py       # Simulated temperature sensor script
│   ├── motion_sensor.py     # Simulated motion sensor script
│   ├── device_controller.py # Controls virtual devices
│
├── cloud/
│   ├── mqtt_client.py       # MQTT client for cloud communication (future)
│
├── tests/
│   ├── test_api.py          # Placeholder for API unit tests
│   ├── test_sensors.py      # Placeholder for sensor scripts testing
│
├── generate_token.py        # Token generation utility for API authentication
├── README.md                # Project documentation
├── .gitignore               # Git ignored files
```

## Prerequisites
- **Python**: Version 3.8 or higher
- **pip**: Python package installer
- Optional: **Git**, a code editor like **VS Code**, and **Postman** for API testing.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ravinalla1109/IoT-Smart-Home-Automation.git
   cd IoT-Smart-Home-Automation
   ```

2. **Set up the backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the Flask API**:
   ```bash
   python app.py
   ```

4. **Simulate sensors**:
   Open a new terminal and run the following scripts:
   ```bash
   python scripts/temp_sensor.py
   python scripts/motion_sensor.py
   ```

5. **Test API Endpoints**:
   Use Postman or `curl`:
   - Check device status:
     ```bash
     curl http://127.0.0.1:5000/status
     ```
   - Control a device:
     ```bash
     curl -X POST http://127.0.0.1:5000/control -H "Content-Type: application/json" -d "{\"device\": \"light\", \"state\": \"on\"}"
     ```

## API Documentation
| Endpoint         | Method | Description                              | Example Payload            |
|-------------------|--------|------------------------------------------|----------------------------|
| `/status`        | `GET`  | Fetches the current state of all devices | -                          |
| `/control`       | `POST` | Controls a specific device               | `{"device": "light", "state": "on"}` |

## Roadmap
1. **Cloud Integration**:
   - Implement MQTT messaging for real-time communication.
   - Store sensor data in AWS DynamoDB or Google Cloud Firestore.
2. **Security Enhancements**:
   - Add OAuth 2.0 or JWT for secure API access.
3. **Data Analytics**:
   - Integrate real-time analytics dashboards using tools like Grafana.
4. **Edge AI**:
   - Deploy AI models on edge devices for intelligent automation.

## Contributing
We welcome contributions to enhance this project! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes and open a pull request.
