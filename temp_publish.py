#!/usr/bin/env python3
#coding: utf-8
#
import json
import paho.mqtt.publish as publish

class Temperature(object):
  ACQUIRE_FREQ =30
  client = None

  def sendData(self):

   jsonFrame= dict();
   jsonFrame['unitID'] = '02:00:c0:a8:00:11'|'vm-dyn-0-211.siame.univ-tlse3.fr'
   jsonFrame['temperature'] = '10'
   res, mid = self.client.publish( 'R1/014/temperature/command', json.dumps(jsonFrame))

   temperature = Temperature()
   temperature.sendData()