from RangeFinderModule import RangeFinderAbstract
from MotorModule import MotorAbstract
import math, time

class Simulator(RangeFinderAbstract, MotorAbstract):

   
    def __init__(self, course, locationObserverAbstractList):
        self.x = 150
        self.y = 25
        self.bearing = 0
        self.speed = 0
        self.ver = 127
        self.hor = 127
        self.MAX = 253
        self.CEN = 127
        self.MIN = 2
        self.isStopped = False
        self.rangeToObstacle = 0
        self.course = course
        self.objectList = course.getObjectList
        self.courseHeight = course.getCourseDimensions()[1]
        self.courseWidth = course.getCourseDimensions()[0]
        self.locationObserverAbstractList = locationObserverAbstractList
        self.sleeptime = 1
        
    ###NEW FUNCTIONS###
    
    def forward(self, speed):
        while self.ver < speed:
            self.ver += 1
            self.x += 1
            for observer in self.locationObserverAbstractList:
                    observer.locationUpdated(self.x,self.y, self.bearing)

    ### Ease the chariot into backward motion.
    ### speed -> The speed to accelerate to. (int)
    def reverse(self, speed):
        if speed < self.MIN or speed > self.CEN: return
        while self.ver > speed:
            self.ver-=1
            for observer in self.locationObserverAbstractList:
                    observer.locationUpdated(self.x,self.y, self.bearing)

    ### Ease the chariot into a right/clockwise turn.
    ### rspeed -> the final speed to turn with. (int)
    def right(self, rspeed):
        #if rspeed > self.MAX or rspeed < self.CEN: return
        while self.hor < rspeed:
            self.hor+=1
            self.bearing+=1
            for observer in self.locationObserverAbstractList:
                    observer.locationUpdated(self.x,self.y, self.bearing)

    ### Ease the chariot into a left/anticlockwise turn.
    ### rspeed -> the final speed to turn with. (int)
    def left(self, lspeed):
        while self.hor > lspeed:
            self.hor-=1
            self.bearing-=1
            for observer in self.locationObserverAbstractList:
                    observer.locationUpdated(self.x,self.y, self.bearing)

    ### Ease the rotation of the chariot to a full stop.
    def center(self):
        while self.hor > self.CEN:
            hor-=1
            time.sleep(0.1)
        while self.hor < self.CEN:
            self.hor+=1
            time.sleep(self.sleeptime)


    ### Ease the motion of the chariot to a full stop. 
    def stop(self):
        while self.ver > self.CEN:
            self.ver-=1
            time.sleep(0.1)
        while self.ver < self.CEN:
            self.ver+=1
            time.sleep(self.sleeptime)
        
    def getRangeInMm(self):   
        for o in self.objectList():
            self.rangeToObstacle = math.hypot(o.x - self.x, o.y - self.y)
        return self.rangeToObstacle

    def getCurrentScanAngle(self):
        return
   
   
    def setCurrentScanAngle(self):
        return

        
    def setSpeed(self, speed):
        self.speed = speed
        print "Setting speed to {}".format(self.speed)

        
    def getSpeed(self):
        return self.speed

    
    # v = vector of line between chariot and waypoint
    def move(self, bearing, v):
        #self.rotate(bearing)
        self.x += v[0]
        self.y += v[1]
        
    def setCurrentPosition(self, x, y, bearing):
        self.x = x
        self.y = y
        self.bearing = bearing
        
    def getCurrentPosition(self):
        return (self.x,self.y)
        
