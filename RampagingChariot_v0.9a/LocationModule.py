from RangeFinderModule import RangeFinderAbstract
from MotorModule import MotorAbstract
import math, time


class Location:
    def __init__(self, motorAbstract, rangeAbstract, locationObserverAbstractList):
        self.motor = motorAbstract
        self.rangeFinder = rangeAbstract
        self.locationObserverAbstractList = locationObserverAbstractList
        self.x,self.y= self.motor.getCurrentPosition()
        self.bearing = self.motor.bearing
        self.isStopped = self.motor.isStopped
        self.courseHeight = self.motor.courseHeight
        self.courseWidth = self.motor.courseWidth   
        self.direction = (1,0)
    
    
    def isColliding(self):
        return (self.rangeFinder.getRangeInMm() < 100)

        
    def moveToWaypoint(self,waypoints):
        
        for w in waypoints:
            
            while(self.motor.getCurrentPosition() != w):
                #get current position of chariot
                self.x,self.y = self.motor.getCurrentPosition()
                chariotLocation = (self.x , self.y)
                #get the bearing towards the waypoint
                bearingToWaypoint = self.getBearing(w)
                self.motor.rotate(bearingToWaypoint)

                #move the chariot towards to waypoint
                self.motor.move((self.getBearing(w)), (self.unitVector(w,chariotLocation)))
                for observer in self.locationObserverAbstractList:
                    observer.locationUpdated(self.x,self.y, self.motor.bearing)
              
        
    #Creates a line between the chariot (p1) and the waypoint (p2)
    def unitVector(self, p1, p2):
        v = tuple(map(lambda a, b: a-b, p1, p2)) #vector from a to b
        
        uv0, uv1 = [0,0] 
        factorX = 1
        factorY = 1
        
       #if the distance between the points < 0 then create a line between the ponts
 
        if v[0] != 0:
            if (v[1] > v[0]):
                factorY = v[1]/v[0]
            uv0 = (v[0]/abs(v[0]))*factorX 
        else:
            uv0 = v[0]
        if v[1] != 0:
            if (v[0] > v[1]):
                factorX = v[0]/v[1]
            uv1 = (v[1]/abs(v[1]))*factorY
        else:
            uv1 = v[1]

        uv = (uv0,uv1)
        return uv

   
    #def getAngle(self, v1, v2):
        #mpmqcostheta = sum(p*q for p,q in zip(v1, v2))
       # mp = abs(v1[0])+abs(v1[1])
      #  mq = abs(v2[0])+abs(v2[1])
     #   costheta = mpmqcostheta/mp/mq
       # print "\n+getAngle = {}".format(math.acos(costheta))
    #    return math.acos(costheta)


    def getBearing(self, point):
       # print("point:{}\n".format(point))
       # print("x,y:{},{}\n".format(self.x,self.y))
        print int(math.degrees(self.getAngle((1,0),self.unitVector(point,(self.x,self.y) ))))
        return int(math.degrees(self.getAngle((1,0),self.unitVector(point,(self.x,self.y) ))))
        
        
    ### You should call this method after you have initialised the Location
    ### object, but before you attempt to use any other methods.
    ### This resets the motor to its default starting position.
    def setDefaultPosition(self):
        return

    ### Scans, finds the next change in distance that looks like an edge,
    ### reports its position, and stops.
    ### threshold -> how much change to allow before detecting an edge
    ### maxDistance -> the maximum distance from which to use readings. (int)
    ### timeToFind -> how long (s) to keep trying to find one. (int)
    ### returns => list with edge position (int), distance (float) or 0
    def findNextEdge(self, threshold, maxDistance, timeToFind):
        return
        
    ### Finds the next object (surface with distance variance under
    ### the given threshold, and within the given distance) and returns
    ### a new Obstacle.
    ### threshold -> how much change to allow before detecting edges (int)
    ### maxDistance -> the maximum distance to search for objects (int)
    ### timeToFind -> how long (s) to keep trying to find one. (int)
    ### returns => the obstacle if one was found, otherwise 0
    def findNextObstacle(self, threshold, maxDistance, timeToFind):
             return

    ### Scans forward and back once, then returns the distance from the
    ### closest found surface.
    ### returns => the distance from the closest surface.
    def findClosestObject(self):
        return

    ### Checks if an object is still where it is expected to be by
    ### scanning between the points given.
    ### obstacle -> The Obstacle to check for
    ### startPosition -> Tne start of the range to check within (int)
    ### endPosition -> The end of the range to check within (int)
    ### returns => True if the object has not moved, otherwise false
    def checkObjectPosition(self, obstacle, startPosition, endPosition):
        return

    ### Finds the nearest pole and restrcts the scan to within its boundaries.
    def trackNextPole():
        return
        
        
        
        
        
    ### Abstract Calls ###   
        
    def forward(self, speed):
        #if (speed >127):
        print "forward call"
        self.motor.forward(speed)
            
    def reverse(self, speed):
        if(speed<127):
            self.motor.reverse(speed)
      
    def right(self, rspeed):
        if(rspeed > 127):
            print "right call"
            self.motor.right(rspeed)
            
    def left(self, lspeed):
        if(lspeed < 127):
            print "left call"
            self.motor.left(lspeed)
    
    def center(self):
        self.motor.center()
        
    def stop(self):
        self.motor.stop()
