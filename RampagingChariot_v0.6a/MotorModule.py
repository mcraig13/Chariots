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
        self.speed = 0
    
    def setSpeed(self, speed):
        self.speed = speed
        print "Setting speed to {}".format(self.speed)

    def getSpeed(self):
        return self.speed
            
    def forward(self, speed):
        self.speed = speed
        self.x += self.speed
        self.y += self.speed
        print "Moving forward at {}".format(self.speed)

    def reverse(self, speed):
        self.speed = speed
        self.x -= self.speed
        self.y -= self.speed
        print "Moving backwards at ".format(self.speed)

    def getCurrentPosition(self):
        return (self.x,self.y)
        
class Motor(MotorAbstract):

    def setSpeed(self, speed):
        return
    def getSpeed(self):
        return
    def forward(self, speed):
        return
    def reverse(self, speed):
        return
    def getCurrentPosition(self):
        return
