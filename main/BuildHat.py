from buildhat import Hat
from buildhat import Motor

class BuildHat:

  #https://buildhat.readthedocs.io/en/latest/buildhat/index.html

  def __init__(self):
    self.hat = Hat()
    print('Check Build Hat Connection Status')
    print(self.hat.get())
    self.motor = Motor('A')
    print('Motor connected: ' + str(self.motor.connected))
    
  def stopMotor(self):
    self.motor.stop()
  
  def startMotor(self, speed):    
    self.motor.set_default_speed(speed)
    self.motor.stop()
    self.motor.start()

  def setMotorSpeed(self, speed):
    self.motor.stop()
    self.motor.set_default_speed(speed)
    self.motor.start()

  def getMotorSpeed(self) -> str:
    return str(self.motor.get_speed())

  def getMotorConnected(self) -> str:
    return str(self.motor.connected)

  def getMotorAPosition(self) -> str:
    return str(self.motor.get_aposition())

  def getMotorPosition(self) -> str:
    return str(self.motor.get_position())