import time
import paho.mqtt.client as paho
from random import randint

broker="ec2-18-195-119-211.eu-central-1.compute.amazonaws.com"
def on_message(client, userdata, message):
    if message.topic == "house/sensor":
        temp = randint(30,45)    
        client.publish("house/sensor_result", str(temp))
        print("received message=" + str(message.payload.decode("utf-8"))+", topic=" + str(message.topic.decode("utf-8")) +". Sent temp="+str(temp))

client= paho.Client("Device Simulator")
######Bind function to callback
client.on_message=on_message
#####

client.connect(broker)#connect
print("Connected to the broker: ",broker)
client.subscribe("house/sensor")#subscribe
client.loop_forever()

