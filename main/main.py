#!/usr/bin/python

import atexit
import logging

# Local classes
from Config import Config
from MQTT import MQTT
from BuildHat import BuildHat

# Logging
Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "../logs/logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.DEBUG)

logger = logging.getLogger()

# Basic
config = Config()
mqtt = MQTT(config)
buildHat = BuildHat()

def execute_app():
    # Exit Handler
    atexit.register(handle_cleanup)

    # MQTT Client Connect    
    mqtt.connect()
    
    # Build Hat 
    buildHat.startMotor(10)

    while True:

        mqtt.publish(
                    'testtopic/motor/speed',
                    'sensor=buildhat,sensor_connect=serial,device=motor,tag=speed',
                    'speed=' + buildHat.getMotorSpeed()
                    )
        mqtt.publish(
                    'testtopic/motor/connected',
                    'sensor=buildhat,sensor_connect=serial,device=motor,tag=connected',
                    'connected=' + buildHat.getMotorConnected()
                    )
        mqtt.publish(
                    'testtopic/motor/aposition',
                    'sensor=buildhat,sensor_connect=serial,device=motor,tag=aposition',
                    'aposition=' + buildHat.getMotorAPosition()
                    )
        mqtt.publish(
                    'testtopic/motor/position',
                    'sensor=buildhat,sensor_connect=serial,device=motor,tag=position',
                    'position=' + buildHat.getMotorPosition()
                    )

def handle_cleanup(*args):
    print('Application Cleanup')
    print('Stop Motor')
    buildHat.stopMotor()
    print('Application Exit')
    exit()

def main():
    #execute_app() # Debug Purpose
    try:        
        execute_app()
        pass
    except Exception as e:
       print('Application Error')
       print("Oops!", e.__class__, str(e), "occurred.")
       pass    
    finally:
        handle_cleanup()

if __name__=='__main__':
    main()


    

    

