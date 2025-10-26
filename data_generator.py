# data_generator.py
import paho.mqtt.client as mqtt
import time
import json
import random

# ========== НАСТРОЙКИ MQTT ==========
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
TOPIC_CURRENT = "robot/axis_j2/current"

# ========== ПАРАМЕТРЫ РОБОТА ==========
NOMINAL_CURRENT = 2.5
LOAD_CURRENT = 5.0
CYCLE_TIME = 3.0

# ========== ПОДКЛЮЧЕНИЕ К MQTT ==========
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_data_generator")
client.connect(MQTT_BROKER, MQTT_PORT)
print(f"Подключились к MQTT брокеру на {MQTT_BROKER}:{MQTT_PORT}")

# ========== ФУНКЦИЯ ГЕНЕРАЦИИ ДАННЫХ ==========
def generate_robot_data(cycle_count):
    """Генерирует данные, имитирующие работу робота-паллетизатора."""
    
    time_in_cycle = cycle_count % CYCLE_TIME
    
    if time_in_cycle < 0.5:
        current = NOMINAL_CURRENT + random.uniform(-0.1, 0.1)
        status = "waiting"
    elif time_in_cycle < 1.5:
        current = LOAD_CURRENT + random.uniform(-0.2, 0.2)
        status = "lifting"
    elif time_in_cycle < 2.5:
        current = NOMINAL_CURRENT + 1.0 + random.uniform(-0.1, 0.1)
        status = "moving"
    else:
        current = NOMINAL_CURRENT + random.uniform(-0.1, 0.1)
        status = "returning"
    
    message = {
        "timestamp": time.time(),
        "current": round(current, 2),
        "status": status,
        "cycle_count": cycle_count
    }
    
    return message

# ========== ОСНОВНОЙ ЦИКЛ РАБОТЫ ==========
def main():
    print("Запуск генератора данных робота-паллетизатора...")
    print("Нажмите Ctrl+C для остановки")
    print("-" * 50)
    
    cycle_count = 0
    
    try:
        while True:
            data = generate_robot_data(cycle_count)
            json_data = json.dumps(data)
            
            # Публикуем данные в MQTT (без callback)
            result = client.publish(TOPIC_CURRENT, json_data)
            
            print(f"Цикл {cycle_count:4d} | Ток: {data['current']:4.1f} А | Статус: {data['status']:10s}")
            
            cycle_count += 1
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nОстановка генератора данных...")
    finally:
        client.disconnect()
        print("Отключились от MQTT брокера.")

# Запускаем программу
if __name__ == "__main__":
    main()