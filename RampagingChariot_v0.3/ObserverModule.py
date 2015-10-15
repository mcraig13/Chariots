from abc import ABCMeta, abstractmethod

class ObserverAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def locationUpdated(self, x, y):
        pass

class Log(ObserverAbstract):
    def locationUpdated(self, x, y):
        print "Chariot location updated: {} {}".format(x,y)
