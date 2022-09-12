#!/usr/bin/python

import configparser

class Config:
  #Documentation https://zetcode.com/python/configparser/
    
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read('config.ini')

  def get_mqtt_transport(self) -> str:
    return self.config['mqtt']['transport']

  def get_mqtt_hostname(self) -> str:
    return self.config['mqtt']['hostname']

  def get_mqtt_port(self) -> int:
    return int(self.config['mqtt']['port'])

  def get_mqtt_username(self) -> str:
    return self.config['mqtt']['username']

  def get_mqtt_password(self) -> str:
    return self.config['mqtt']['password']  

  def get_mqtt_client_id(self) -> str:
    return self.config['mqtt']['clientid'] 

  def get_mqtt_tls(self) -> str:
    return self.config['mqtt']['tls']  