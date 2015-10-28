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
    
    @abstractmethod
    def getCurrentPosition(self):
        pass

class MotorSim(MotorAbstract):

    def __init__(self):
        self.x = 130
        self.y = 15
        self.bearing = 90
        self.speed = 0
        self.isStopped = False
    
    def setSpeed(self, speed):
        self.speed = speed
        print "Setting speed to {}".format(self.speed)

    def getSpeed(self):
        return self.speed
            
    def forward(self, speed, bearing):
        if(bearing == 90):
            self.isStopped = False
            self.speed = speed
            self.x += self.speed
        elif(bearing == 0):
            self.isStopped = False
            self.speed = speed
            self.y += self.speed
        elif(bearing == 180):
            self.isStopped = False
            self.speed = speed
            self.y -= self.speed
        elif(bearing == 270):
            self.isStopped = False
            self.speed = speed
            self.y -= self.speed
            
        print "Moving forward at {}".format(self.speed)

    def reverse(self, speed):
        self.isStopped = False
        self.speed = speed
        self.x -= self.speed
        print "Moving backwards at {}".format(self.speed)

    def turn(self, bearing):
        self.bearing = bearing
        print "Turning on a bearing of {}".format(self.bearing)
        
    def getCurrentPosition(self):
        return (self.x,self.y)
        
    def getBearing(self):
        return self.bearing
        
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
