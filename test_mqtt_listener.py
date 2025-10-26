# test_mqtt_listener.py
import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"✅ Connected to MQTT with code {rc}")
    if rc == 0:
        client.subscribe("robot/axis_j2/current")
        print("📡 Subscribed to topic: robot/axis_j2/current")
    else:
        print(f"❌ Connection failed: {rc}")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"📨 Topic: {msg.topic}")
        print(f"   Data: {data}")
        print("-" * 50)
    except Exception as e:
        print(f"❌ Error parsing message: {e}")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "test_listener")
    client.on_connect = on_connect
    client.on_message = on_message
    
    print("🔍 Starting MQTT listener...")
    print("Connecting to localhost:1883")
    
    try:
        client.connect("localhost", 1883, 60)
        print("🔄 Starting message loop...")
        client.loop_forever()
    except Exception as e:
        print(f"❌ Connection error: {e}")
    except KeyboardInterrupt:
        print("\n🛑 Stopping listener...")
        client.disconnect()

if __name__ == "__main__":
    main()