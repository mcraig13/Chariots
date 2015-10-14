from abc import ABCMeta, abstractmethod

class LocationObserverAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def locationUpdated(self, x, y):
        pass

class Logger(LocationObserverAbstract):
    def locationUpdated(self, x, y):
        print "Chariot location updated: {} {}".format(x,y)
