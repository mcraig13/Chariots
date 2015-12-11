import time, threading, math, threading
from LocationModule import Location
from SimulatorModule import Simulator

### The representation of a chariot as a whole, controlling various subcomponents.
class Chariot:


    def __init__(self, motorAbstract, rangeAbstract, locationObserverAbstractList, chariotcf , waypoints):

        self.thread = threading.Thread(target = self.drive, args= (motorAbstract, rangeAbstract, locationObserverAbstractList, ))
        self.thread.daemon = True
        self.thread.start()
        
       
       
        ## Function Calls Here ### 
    def drive(self, motorAbstract, rangeAbstract, locationObserverAbstractList):
        self.location = Location(motorAbstract, rangeAbstract, locationObserverAbstractList)
        #self.location.forward(200)
        time.sleep(1)
        self.location.left(20)
        time.sleep(1)
        self.location.right(100)
        self.location.forward(240)
        self.location.reverse(50)
    

class ChariotConfig:
	
	def __init__(self):
		self.width = 45
		self.length = 35
		self.xoffset = 20
		self.yoffset = 10
		
	
	
	
