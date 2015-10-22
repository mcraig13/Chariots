from abc import ABCMeta, abstractmethod

class MotorAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def setSpeed(self, speed):
        pass
        
    @abstractmethod
    def forward(self, speed):
        pass

    @abstractmethod
    def reverse(self, speed):
        pass
        
    @abstractmethod
    def getCurrentPosition(self):
        pass

class MotorSim(MotorAbstract):

    def __init__(self):
        self.x = 160
        self.y = 47
    
    def setSpeed(self, speed):
        self.speed = speed
        print "Setting speed to {}".format(speed)
            
    def forward(self, speed):
        self.speed = speed
        self.x += 1
        self.y += 1
        print "Moving forward at ".format(speed)

    def reverse(self, speed):
        self.speed = speed
        self.x -= 1
        self.y -= 1
        print "Moving backwards at ".format(speed)

    def getCurrentPosition(self):
        return (self.x,self.y)
        
class Motor(MotorAbstract):

    def setSpeed(self, speed):
        return  
    def forward(self, speed):
        return
    def reverse(self, speed):
        return
