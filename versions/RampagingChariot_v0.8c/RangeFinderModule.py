from abc import ABCMeta, abstractmethod
import math

class RangeFinderAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getRangeInMm(self, chariotx, charioty):
        pass
        
    @abstractmethod
    def getCurrentScanAngle(self):
        pass
    
    @abstractmethod
    def setCurrentScanAngle(self):
        pass
    
class RangeFinder(RangeFinderAbstract):

    def __init__(self):
        return

    def getRangeInMm(self):
        return  
    
    def getCurrentScanAngle(self):
        return
    
    def setCurrentScanAngle(self):
        return
