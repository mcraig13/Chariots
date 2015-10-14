from ChariotModule import Chariot
from RangeFinderModule import RangeFinderSim
from MotorModule import MotorSim
from LocationObserverModule import *
from CourseModule import Course

l = Logger()
observerList = [l]

r = RangeFinderSim()
m = MotorSim()
c = Chariot(r,m,observerList)

co = Course('assault.csv')



