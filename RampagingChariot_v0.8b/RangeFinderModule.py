from abc import ABCMeta, abstractmethod
import math

class RangeFinderAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getRangeInMm(self, chariotx, charioty):
        pass
        
    def closestObject(self):
        pass

class RangeFinder(RangeFinderAbstract):

    def __init__(self):
        return

    def getRangeInMm(self):
        return  
    
    def closestObject(self):
        return