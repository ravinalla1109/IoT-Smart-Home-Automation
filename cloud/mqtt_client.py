import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPIC = "iot/home/updates"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, 1883, 60)
    client.loop_forever()
