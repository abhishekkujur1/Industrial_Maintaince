import paho.mqtt.client as mqtt
import json
import sys
import os

# Allow importing from the sibling database directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db_manager import insert_reading

# --- MQTT Configuration ---
# If running Mosquitto locally on your machine, use localhost. 
# Make sure your ESP32 config.h points to this machine's local IP address.
BROKER = "127.0.0.1" 
PORT = 1883
TOPIC = "machine/sensor_data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker successfully!")
        client.subscribe(TOPIC)
        print(f"Listening for data on topic: {TOPIC}")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        # Decode the JSON payload from the ESP32
        payload = json.loads(msg.payload.decode())
        
        device_id = payload.get("device_id", "Unknown")
        sound = payload.get("sound", 0)
        rpm_pulse = payload.get("rpm_pulse", 0)
        
        # Save to SQLite Database
        insert_reading(device_id, sound, rpm_pulse)
        print(f"Saved -> Device: {device_id} | Sound: {sound} | RPM Pulse: {rpm_pulse}")
        
    except json.JSONDecodeError:
        print("Error: Received malformed JSON")
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    print(f"Attempting to connect to broker at {BROKER}...")
    try:
        client.connect(BROKER, PORT, 60)
        client.loop_forever() # Keep the script running
    except ConnectionRefusedError:
        print("Connection Refused: Is your MQTT Broker (Mosquitto) running?")