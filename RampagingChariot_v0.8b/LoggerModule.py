from abc import ABCMeta, abstractmethod

class LocationObserverAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def locationUpdated(self, x, y, bearing):
        pass

		
		
class Logger(LocationObserverAbstract):
    def locationUpdated(self, x, y, bearing):
        print "Chariot location updated: {} {}".format(x,y)
