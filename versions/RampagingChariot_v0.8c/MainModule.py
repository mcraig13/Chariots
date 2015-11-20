from ChariotModule import *
from SimulatorModule import Simulator
from LoggerModule import *
from VisualiserModule import *
from CourseModule import *

co = Course('assault.csv')

cf = ChariotConfig()

v  = Visualiser(cf, co)

l = Logger()

observerList = [l, v]

s = Simulator(co, observerList)

c = Chariot(s,observerList, cf)