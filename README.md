## A simple physical sensor device simulator with using MQTT communication protocol.

- Connects to a broker and subscribes to "house/sensor" channel
- If a request comes into this channel, then creates a random temperature result
- And sends to the "house/sensor_result" channel back

Usage:
~~~~
git clone https://github.com/BurakDmb/MQTT-Basic-Device-Simulator.git
cd MQTT-Basic_Device-Simulator
pip install paho-mqtt
python main.py
~~~~