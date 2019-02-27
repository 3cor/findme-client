#!/usr/bin/env python3

# MQTT Client for EPAPER Application
# Developed by Nitis Monburinon (2018)

import paho.mqtt.client as mqtt
import os
import urllib.parse as urlparse
import epaper 
import threading

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    message = msg.payload.decode("utf-8")
    # Using multithread to update screen
    t = threading.Thread(target=show_message, name="Print message", args=(message,))
    t.daemon = True
    t.start()
    mqttc.publish(rsp_topic,message)
    print(msg.topic + " " + str(msg.qos) + " " + message)

def on_publish(client, obj, mid):
    print("mid: " + str(mid))
    
def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

def cache_message(title,msg):
    with open("cache.txt","w") as f:
        f.write(title + "####" + msg)

def restore_message():
    with open("cache.txt") as f:
        title, msg = f.readlines().split("####")
    return title, msg

def show_message(text):
    ep = epaper.EPScreen('landscape')
    title, msg = text.split("####")
    ep.set_title(title)
    ep.print(msg)
    ep.update_screen()

print("MQTT Client for Epaper Application")
print("Developed by Nitis Monburinon (2018)")

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
hostname="m12.cloudmqtt.com"
port=18109
username="vplfvxvo"
password="g9ssGd-XOM4z"
device_id="001"
msg_topic="msg/request/"+device_id
rsp_topic="msg/response/"+device_id

# Connect
mqttc.username_pw_set(username, password)
mqttc.connect(hostname, port)

# Start subscribe, with QoS level 0
mqttc.subscribe([(msg_topic,0)])

# Publish a message
# mqttc.publish(topic, "Hello world")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
