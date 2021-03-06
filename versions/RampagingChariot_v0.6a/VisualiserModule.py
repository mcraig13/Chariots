from Tkinter import *
from CourseModule import *
from LoggerModule import *
import math


class Visualiser(LocationObserverAbstract):

	def __init__(self, chariotcf, course):
	
		self.xoffset = chariotcf.xoffset
		self.yoffset = chariotcf.yoffset
		self.chariotBearing = 0
		self.chariotWidth = chariotcf.width
		self.chariotLength = chariotcf.length
		self.chariot = chariotcf
		self.course = course
		self.chariotx = 0
		self.charioty = 0
		self.objectList = course.getObjectList
		self.wallList = course.getWallList
		self.waypointList = course.getWaypointList
		self.root = Tk()
		self.root.wm_title("Rampyge Visualiser")
		self.courseWidth = course.getCourseDimensions()[0]
		self.courseHeight = course.getCourseDimensions()[1]
		self.canvas = Canvas(self.root, width=self.courseWidth,height=self.courseHeight)
		self.canvas.pack()
		self.root.after_idle(self.paint)
                self.root.update_idletasks()
                self.root.update()
		#mainloop()
		
	
		

	def locationUpdated(self, x, y, bearing):
		self.chariotx = x
		self.charioty = y
		self.chariotBearing = bearing
		self.paint()
		        
	
	
	### Redraw the contents of the window.
	def paint(self):
                self.canvas.delete("all")
                self.canvas.create_rectangle(0,0,self.courseWidth,self.courseHeight,fill="#DDDDDD")
                points = []
                for o in self.wallList():
                        objectType = o.oType
                        if objectType == "wall":
                                points += o.x,o.y
                                self.canvas.create_line(o.x, o.y, o.width, o.height)
                self.canvas.create_polygon(points, fill="#408040", outline='black', width=2)
                self.canvas.create_line(25,25,475,475, fill="#DDDDDD", width=2) #diagonal marking
                self.canvas.create_oval(200,200,300,300, outline="#DDDDDD", width=2) #circle marking
                for o in self.objectList():
                        objectType = o.oType
                        if objectType == "pole":
                                self.canvas.create_oval(o.x-(o.width)/2, o.y-(o.width)/2+5, o.x+(o.width)/2, \
                                o.y+(o.width)/2+5, fill="white")
                        elif objectType == "ramp":
                                self.canvas.create_rectangle(o.x,o.y,o.x+o.width,o.y+o.height,fill="#222222")
                                self.canvas.create_line((o.x+o.x+o.width)/2,o.y+8,(o.x+o.x+o.width)/2,o.y+o.height-2,\
                                    fill="white", dash=(10,5))
                        elif objectType == "barrel":
                                self.canvas.create_rectangle(o.x,o.y,o.x+o.width,o.y+o.height, fill="black")
                        elif objectType == "ball":
                                self.canvas.create_oval(o.x-o.width, o.y-o.width, o.x+o.width,\
                                       o.y+o.width, fill="orange")
                        elif objectType == "net":
                                self.canvas.create_line(o.x,o.y,o.width,o.height, fill="grey", width=4)
                        elif objectType == "door":
                                self.canvas.create_line(o.x,o.y,o.width,o.height,fill="black", width=2)
                        elif objectType == "barrier":
                                self.canvas.create_line(o.x,o.y,o.width,o.height, fill="black", width=4)


                for o in self.waypointList():
                        objectType = o.oType
                        if objectType == "waypoint":
                                self.canvas.create_oval(o.x-2, o.y-2, o.x+2, o.y+2,fill="red")
                        
                #Rotate and paint the chariot
                
                self.canvas.create_polygon(self.getChariotPoints(), fill="#FFFF00", outline="black")
                self.canvas.create_text(50,520, text="{0:.2f}".format(self.chariotBearing))
                self.canvas.create_text(50,550, text="{},{}".format(self.chariotx,self.charioty))
                
                
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


