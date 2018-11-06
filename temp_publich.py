#!/usr/bin/env python3
#coding: utf-8
#
import json
import paho.mqtt.publish as publish

class Temperature(object):
  ACQUIRE_FREQ =30
  client = None

  def sendData(self):
  "'sending temperatures'"

  jsonFrame= dict();
  jsonFrame['unitID'] = '60:30:d4:7e:b0:02'|'MacBook-Air-de-Roukaya.local'
  jsonFrame['temperature'] = '10'
  
  res, mid = self.client.publish( 'R1/014/temperature/command', json.dumps(jsonFrame))

  temperature = Temperature()
  temperature.sendData()