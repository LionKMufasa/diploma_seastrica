import paho.mqtt.client as mqtt
import time

def test_connection():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "test_generator")
    
    def on_connect(client, userdata, flags, rc, properties=None):
        print(f"✅ Generator connected to MQTT: {rc}")
        if rc == 0:
            # Отправим тестовое сообщение
            result = client.publish("test/topic", "Hello from generator!")
            print(f"✅ Test message sent! (mid: {result.mid})")
        else:
            print(f"❌ Connection failed: {rc}")
    
    def on_publish(client, userdata, mid, reason_code, properties):
        print(f"✅ Message published confirmed (mid: {mid})")
    
    client.on_connect = on_connect
    client.on_publish = on_publish
    
    print("Connecting generator to MQTT...")
    client.connect("localhost", 1883, 60)
    client.loop_start()
    time.sleep(3)
    client.loop_stop()
    client.disconnect()

test_connection()