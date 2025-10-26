# 🤖 Система предиктивного обслуживания робота-паллетизатора АО "Сестрица"

## 🛠️ Требуемое ПО для разработки

### Обязательное:
- **Docker Desktop** - контейнеризация системы
  - Скачать: https://docker.com
- **Git** - контроль версий  
  - Скачать: https://git-scm.com
- **Python 3.11+** - основной язык разработки
  - Скачать: https://python.org
  - ✅ Важно: отметить "Add Python to PATH" при установке

### Рекомендуемое:
- **VS Code** - редактор кода
  - Скачать: https://code.visualstudio.com
- **CoppeliaSim** - 3D симулятор робота (для следующих этапов)
  - Скачать: https://coppeliarobotics.com

## 📦 Python библиотеки

### Установите все зависимости одной командой:
```bash
pip install paho-mqtt influxdb-client numpy matplotlib scikit-learn jupyter pandas scipy torch tensorflow seaborn plotly requests beautifulsoup4 lxml opencv-python pillow