#!/usr/bin/env python3
#coding: utf-8
#
import json
import paho.mqtt.client as mqtt_client

class Temperature(object):
  ACQUIRE_FREQ =30
  client = None

def __init__(self):
  #MQTT client initialization 
  self.client = mqtt_client.Client()
  self.client.on_connect = self.on_connect
  self.client.on_message = self.on_message
  self.client.connect('172.19.17.236',1883,60);
  self.client.loop_start()
         
def on_connect(self, client, userdata,flags, rc):
    if(rc != 0 ): return
    self.client.subscribe('R1/014/temperature/command');

def _on_message(self, client, userdata, msg):
    if msg.topic != self._command_topic:
       #this module is not concerned by this message, returning
       log.debug("received a message not for me on" + msg.topic)
    try:
       #loading nd verifiying payload 
       payload = json.load(msg.payload.decode('utf-8'))
    except Exception as ex:
      log.error("exception handling json paload: " + str(ex))
      return
    else:
      # executed if no exception arise
      if payload['dest'] != "all" and payload['dest'] != str(self.unitID):
          return

    temperature = Temperature()
    client.loop_forever ()