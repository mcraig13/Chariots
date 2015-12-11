import time, threading, math, threading
from LocationModule import Location
from SimulatorModule import Simulator

### The representation of a chariot as a whole, controlling various subcomponents.
class Chariot:

    ### Creates a chariot object but does not start the loop thread. 
    ### To start operation call (Chariot).start() from your Main script.
    def __init__(self, motorAbstract, rangeAbstract, locationObserverAbstractList, chariotcf , waypoints):

        self.thread = threading.Thread(target = self.drive, args= (motorAbstract, rangeAbstract, locationObserverAbstractList, ))
        self.thread.daemon = True
        self.thread.start()
        
       
       
        ## Function Calls Here ### 
    def drive(self, motorAbstract, rangeAbstract, locationObserverAbstractList):
        self.location = Location(motorAbstract, rangeAbstract, locationObserverAbstractList)
        self.location.forward(200)
        time.sleep(1)
        self.location.left(126)
        time.sleep(1)
        self.location.right(200)
    

class ChariotConfig:
	
	def __init__(self):
		self.width = 45
		self.length = 35
		self.xoffset = 20
		self.yoffset = 10
		
	
	
	
