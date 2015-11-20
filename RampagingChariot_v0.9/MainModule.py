from ChariotModule import *
from SimulatorModule import Simulator
from LoggerModule import *
from VisualiserModule import *
from CourseModule import *
from RealMotor import *

waypoints = [(300,232),
                (289,175),
                (500,233)
             ]

co = Course('assault.csv')

cf = ChariotConfig()

v  = Visualiser(cf, co, waypoints)

l = Logger()

observerList = [l, v]

s = Simulator(co, observerList)

#r = RealMotor()

c = Chariot(s,s,observerList, cf, waypoints)

v.startMainLoop()
