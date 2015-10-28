from abc import ABCMeta, abstractmethod

class MotorAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def setSpeed(self, speed):
        pass

    @abstractmethod
    def getSpeed(self):
        pass
        
    @abstractmethod
    def forward(self, speed, bearing):
        pass

    @abstractmethod
    def reverse(self, speed):
        pass

    @abstractmethod
    def turn(self, bearing):
        pass
        
    def updatePosition(self, x,y):
        pass
    
    @abstractmethod
    def getCurrentPosition(self):
        pass
    
        
class Motor(MotorAbstract):

    def setSpeed(self, speed):
        return
    def getSpeed(self):
        return
    def forward(self, speed):
        return
    def reverse(self, speed):
        return
    def turn(self, bearing):
        return
    def getCurrentPosition(self):
        return
