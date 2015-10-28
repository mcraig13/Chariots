from RangeFinderModule import RangeFinderAbstract
from MotorModule import MotorAbstract

class Simulator(RangeFinderAbstract, MotorAbstract):
    
    def __init__(self, course):
        self.x = 130
        self.y = 15
        self.bearing = 90
        self.speed = 0
        self.isStopped = False
        self.rangeToObstacle = 0
        self.course = course
        self.objectList = course.getObjectList
        self.wallList = course.getWallList
        self.courseHeight = course.getCourseDimensions()[1]
        self.courseWidth = course.getCourseDimensions()[0]
        
    def getRangeInMm(self, chariotx, charioty):
        for o in self.objectList():
            self.rangeToObstacle = math.hypot(o.x - chariotx, o.y - charioty)
        return self.rangeToObstacle
    
    def getObject(self):
        return self.objectList()
        
    def getWall(self):
        return self.wallList()
        
    def closestObject(self):
        return
        
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
            self.x -= self.speed
            
        #print "Moving forward at {}".format(self.speed)

    def reverse(self, speed):
        self.isStopped = False
        self.speed = speed
        self.x -= self.speed
        print "Moving backwards at {}".format(self.speed)

    def turn(self, bearing):
        self.bearing = bearing
        print "Turning on a bearing of {}".format(self.bearing)
        
    def updatePosition(self, x, y):
        self.x = x
        self.y = y
        
    def getCurrentPosition(self):
        return (self.x,self.y)
        
    def getBearing(self):
        return self.bearing