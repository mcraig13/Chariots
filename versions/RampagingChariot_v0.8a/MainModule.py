from ChariotModule import *
from RangeFinderModule import RangeFinderSim
from MotorModule import MotorSim
from LoggerModule import *
from VisualiserModule import *
from CourseModule import *

co = Course('assault.csv')

cf = ChariotConfig()

v  = Visualiser(cf, co)

l = Logger()

observerList = [l, v]

r = RangeFinderSim(co)

m = MotorSim()

c = Chariot(r,m,observerList, cf)



       
