import time, threading, math
from LocationModule import Location

### The representation of a chariot as a whole, controlling various subcomponents.
class Chariot:

    ### Creates a chariot object but does not start the loop thread. 
    ### To start operation call (Chariot).start() from your Main script.
    def __init__(self, rangeFinderAbstract, motorAbstract, locationObserverAbstractList):
        self.width, self.length = [31,45]
        self.x, self.y = [160,47]
        self.bearing = 0
        self.speed = 90

        #self.run = True
        #self.cb = ControlBoard()
        
        self.location = Location(rangeFinderAbstract, motorAbstract, locationObserverAbstractList)
        self.location.moveUntilObstacle()
        #self.main = threading.Thread(target=self.loop)
        #self.main.daemon = True

