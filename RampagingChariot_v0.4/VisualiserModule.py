from Tkinter import *
from CourseModule import *
from LoggerModule import *
import math


class Visualiser(LocationObserverAbstract):

	def __init__(self, chariotcf, course):
	
		self.xoffset = chariotcf.xoffset
		self.yoffset = chariotcf.yoffset
		self.chariotx = 0
		self.charioty = 0
		self.chariotWidth = chariotcf.width
		self.chariotLength = chariotcf.length
		self.chariot = chariotcf
		self.chariotBearing = 0
		self.course = course
		self.objectList = course.getObjectList
		self.root = Tk()
		self.root.wm_title("Rampyge Visualiser")
		self.courseWidth = course.getCourseDimensions()[0]
		self.courseHeight = course.getCourseDimensions()[1]
		self.canvas = Canvas(self.root, width=self.courseWidth,height=self.courseHeight)
		self.canvas.pack()
		self.root.after_idle(self.paint)
		mainloop()
		
		
		

	def locationUpdated(self, x, y, bearing):
		self.charioty = x
		self.charioty = y
		self.chariotBearing = bearing
		paint()
		
	def getArena(self):
		for i in range(len(objectList)):
			if objectList[i].oType == "course":
				return (objectList[i].width,objectList[i].height)
	
	
		### Redraw the contents of the window.
	def paint(self):
		self.canvas.delete("all")
		self.canvas.create_rectangle(0,0,self.courseWidth,self.courseHeight,\
									fill="#DDDDDD")
		points = []
		
		for o in self.objectList():
			objectType = o.oType
			if objectType == "pole":
				self.canvas.create_oval(o.x-(o.width)/2, o.y-(o.width)/2+5, o.x+(o.width)/2, \
				o.y+(o.width)/2+5, fill="white")
		#Rotate and paint the chariot
		self.canvas.create_polygon(self.getChariotPoints(), fill="#FFFF00", outline="black")

		
		self.root.update_idletasks()
		self.root.after(100,self.paint)
		### Finds the points required to draw a distance sensor

	def getChariotPoints(self):
		v = [self.chariotx - self.chariotWidth/2, self.chariotx+self.chariotWidth/2,\
				  self.charioty - self.chariotLength/2, self.charioty+self.chariotLength/2]
		points = [(v[0],v[2]),(v[1],v[2]),(v[1],v[3]),(v[0],v[3])]
		angle = -math.radians(self.chariotBearing)
		#Find center points
		cx = self.chariotx
		cy = self.charioty
		for i in range (0,4): #rotational transform on each vertex
			x0 = points[i][0] - cx
			y0 = points[i][1] - cy
			tx= math.cos(angle)*x0-math.sin(angle)*y0
			ty= math.sin(angle)*x0+math.cos(angle)*y0
			points[i] = (int(tx + cx)+self.xoffset,\
						 self.courseHeight - (int(ty+cy)+self.yoffset))
		#print(points)
		return points


