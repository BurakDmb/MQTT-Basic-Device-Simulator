### A simple physical sensor device simulator with using MQTT communication protocol.
import paho.mqtt.client as paho
from random import randint

broker="ec2-18-195-119-211.eu-central-1.compute.amazonaws.com"
def on_message(client, userdata, message):
    if str(message.topic.decode("utf-8")) == "house/sensor" and str(message.payload.decode("utf-8")) == "get_temp":
        temp = randint(30,45)    
        client.publish("house/sensor_result", str(temp))
        print("received message=" + str(message.payload.decode("utf-8"))+", topic=" + str(message.topic.decode("utf-8")) +". Sent temp="+str(temp))

client= paho.Client("Device Simulator")
client.on_message=on_message

client.connect(broker)#connect
print("Connected to the broker: ",broker)
client.subscribe("house/sensor")#subscribe

client.loop_forever()