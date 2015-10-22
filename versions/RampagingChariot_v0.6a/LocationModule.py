from RangeFinderModule import RangeFinderAbstract
from MotorModule import MotorAbstract

class Location:
    def __init__(self, rangeFinderAbstract, motorAbstract, locationObserverAbstractList):
        self.rangeFinderAbstract = rangeFinderAbstract
        self.motorAbstract = motorAbstract
        self.locationObserverAbstractList = locationObserverAbstractList
        self.x,self.y = motorAbstract.getCurrentPosition()
        motorAbstract.setSpeed(1)
        

    #Move the chariot in the current direction until obstacle
    #is detected and then stop.
    def moveUntilObstacle(self):
        while(self.rangeFinderAbstract.getRangeInMm() <> 0):
            self.motorAbstract.forward(self.motorAbstract.getSpeed())
            self.x,self.y = self.motorAbstract.getCurrentPosition()
            for observer in self.locationObserverAbstractList:
                observer.locationUpdated(self.x,self.y, 0)
            

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
