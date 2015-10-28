from abc import ABCMeta, abstractmethod
import math

class RangeFinderAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getRangeInMm(self, chariotx, charioty):
        pass
        
    def closestObject(self):
        pass

class RangeFinderSim(RangeFinderAbstract):
    
    def __init__(self, course):
        self.rangeToObstacle = 0
        self.course = course
        self.objectList = course.getObjectList
        self.wallList = course.getWallList
        self.courseHeight = course.getCourseDimensions()[1]
        
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

class RangeFinder(RangeFinderAbstract):

    def __init__(self):
        return

    def getRangeInMm(self):
        return  
    
    def closestObject(self):
        return