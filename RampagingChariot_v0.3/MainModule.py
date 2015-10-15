from ChariotModule import Chariot
from RangeFinderModule import RangeFinderSim
from MotorModule import MotorSim
from ObserverModule import *
from CourseModule import Course
#from VisualiserModule import *

l = Log()
observerList = [l]

r = RangeFinderSim()
m = MotorSim()
c = Chariot(r,m,observerList)

co = Course('assault.csv')

#v = Visualiser(c)


objectList = co.getObjectList()

for i in range(len(objectList)):
	print (objectList[i].oType,objectList[i].x,objectList[i].y)