from ChariotModule import *
from RangeFinderModule import RangeFinderSim
from MotorModule import MotorSim
from LoggerModule import *
from VisualiserModule import *


l = Logger()

observerList = [l]

r = RangeFinderSim()

m = MotorSim()

cf = ChariotConfig()


c = Chariot(r,m,observerList, cf)

co = Course('assault.csv')

v  = Visualiser(cf, co)

