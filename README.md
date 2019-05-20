## A simple physical sensor device simulator with using MQTT communication protocol.

- Connects to a broker and subscribes to "house/sensor" channel
- If a request comes into this channel, then creates a random temperature result
- And sends to the "house/sensor_result" channel back
- This simulator is running on a free tier amazon server(ec2-18-195-119-211.eu-central-1.compute.amazonaws.com) 
- And you can send MQTT requests to "house/sensor" channel to get a result

- Usage:
    ~~~~
    git clone https://github.com/BurakDmb/MQTT-Basic-Device-Simulator.git
    cd MQTT-Basic_Device-Simulator
    pip3 install paho-mqtt
    python3 main.py
    ~~~~

- Also you can use this command to use this script in background
  ~~~~
  nohup python3 main.py &
  ~~~~
- And you can kill using:
  ~~~~
  ps -aux | grep main.py
  kill PID(the pid of main.py process)
  ~~~~
