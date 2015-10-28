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
    def rotate(self, bearing):
        pass
    
    @abstractmethod
    def setCurrentPosition(self, x,y,bearing):
        pass
    
    @abstractmethod
    def getCurrentPosition(self):
        pass
        
    @abstractmethod
    def distanceTravelled(self):
        pass
        
class Motor(MotorAbstract):

    def setSpeed(self, speed):
        return
    def getSpeed(self):
        return
    def forward(self, speed, bearing):
        return
    def reverse(self, speed):
        return
    def rotate(self, bearing):
        return
    def setCurrentPosition(self, x,y,bearing):
        return
    def getCurrentPosition(self):
        return
    def distanceTravelled(self):
        return