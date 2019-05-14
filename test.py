### A test script for testing the MQTT-Basic-Device-Simulator
import paho.mqtt.client as paho
import time

broker="ec2-18-195-119-211.eu-central-1.compute.amazonaws.com"
def on_message(client, userdata, message):
    if message.topic == "house/sensor_result":
        temp = str(message.payload.decode("utf-8"))
        print("Temp result:" + temp)
        client.disconnect()

client= paho.Client("Test-Client")
client.on_message=on_message
client.connect(broker)#connect
print("Connected to the broker: ",broker)

client.subscribe("house/sensor_result")
client.publish("house/sensor","get_temp")#publish

client.loop_forever()
