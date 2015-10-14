from abc import ABCMeta, abstractmethod

class RangeFinderAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getRangeInMm(self):
        pass
    

class RangeFinderSim(RangeFinderAbstract):
    
    def __init__(self):
        self.rangeToObstacle = 10

    def getRangeInMm(self):
        self.rangeToObstacle -= 1
        return self.rangeToObstacle


class RangeFinder(RangeFinderAbstract):

    def getRangeInMm(self):
      return  
