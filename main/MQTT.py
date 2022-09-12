#!/usr/bin/python

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import threading

class MQTT:
    
    #https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php
    
    def __init__(self, config):    
        self.config = config
        self.publish_lock = threading.Lock()
        self.mqttc = mqtt.Client(
            transport=self.config.get_mqtt_transport(),
            client_id=self.config.get_mqtt_client_id(),
            clean_session=True,
            userdata=None            
            )

    def connect(self):
        self.mqttc.username_pw_set(self.config.get_mqtt_username(), self.config.get_mqtt_password())
        if self.config.get_mqtt_tls().lower() == 'true': self.mqttc.tls_set()
        self.mqttc.enable_logger(logger=None)

        self.mqttc.connect(self.config.get_mqtt_hostname(), self.config.get_mqtt_port(), 60)        
        
    def publish(self, topic, tags, message):
        self.publish_lock.acquire()
        now_ns = time.time_ns()
        message = 'sensor,clientid=' + self.config.get_mqtt_client_id() + ',' + tags + ' ' + str(message) + ' ' + str(now_ns)
        self.mqttc.publish(topic, message)
        self.mqttc.loop_start()
        self.publish_lock.release()