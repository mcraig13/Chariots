from Tkinter import *
from LoggerModule import *
import math, time


class Visualiser(LocationObserverAbstract):

    def __init__(self, chariotcf, course):
    
        self.xoffset = chariotcf.xoffset
        self.yoffset = chariotcf.yoffset
        self.chariotBearing = 90
        self.chariotWidth = chariotcf.width
        self.chariotLength = chariotcf.length
        self.chariot = chariotcf
        self.course = course
        self.chariotx = 130
        self.charioty = 15
        self.objectList = course.getObjectList
        self.wallList = course.getWallList
        self.waypointList = course.getWaypointList
        self.root = Tk()
        self.root.wm_title("Rampyge Visualiser")
        self.courseWidth = course.getCourseDimensions()[0]
        self.courseHeight = course.getCourseDimensions()[1]
        self.canvas = Canvas(self.root, width=self.courseWidth,height=self.courseHeight)
        self.root.geometry = ('%dx%d+%d+%d' % (self.courseWidth, self.courseHeight, 0, 0))
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
                self.canvas.create_line(32,32,468,468, fill="#DDDDDD", width=1) #diagonal marking
                self.canvas.create_oval(200,200,300,300, outline="#DDDDDD", width=1) #circle marking
                self.canvas.create_oval(-10,self.courseHeight - (-10),10,self.courseHeight - 10, outline="black", width=1) #corner circle
                self.canvas.create_line(8,self.courseHeight - 8,20,self.courseHeight - 20, fill="black", width=1)   #corner line
                self.canvas.create_line(190, 740, 190, 690, fill="#DDDDDD", width=4) #garage left
                self.canvas.create_line(310, 740, 310, 690, fill="#DDDDDD", width=4) #garage right
                for o in self.objectList():
                        objectType = o.oType
                        if objectType == "pole":
                                self.canvas.create_oval(o.x-(o.width)/2, self.courseHeight - o.y-(o.width)/2+5, o.x+(o.width)/2,self.courseHeight - o.y+(o.width)/2+5, fill="white")
                        elif objectType == "ramp":
                                self.canvas.create_rectangle(o.x,self.courseHeight - o.y,o.x+o.width,self.courseHeight - (o.y+o.height),fill="#222222")
                                self.canvas.create_line((o.x+o.x+o.width)/2,self.courseHeight - (o.y+8),(o.x+o.x+o.width)/2,self.courseHeight - (o.y+o.height-2),fill="white", dash=(10,5))
                        elif objectType == "barrel":
                                self.canvas.create_rectangle(o.x,self.courseHeight - o.y,o.x+o.width,self.courseHeight - (o.y+o.height), fill="brown")
                        elif objectType == "ball":
                                self.canvas.create_oval(o.x-o.width, self.courseHeight - (o.y-o.width), o.x+o.width,self.courseHeight -(o.y+o.width), fill="orange")
                        elif objectType == "net":
                                self.canvas.create_line(o.x,self.courseHeight - o.y,o.width,self.courseHeight - o.height, fill="grey", width=4)
                                self.canvas.create_line(0,self.courseHeight - o.y,31.875,self.courseHeight - o.y, fill="black", width=1)
                                self.canvas.create_line(468.175,self.courseHeight - o.y,500,self.courseHeight - o.y, fill="black", width=1)
                                self.canvas.create_line(o.width,self.courseHeight - o.y + 95.625,o.width,self.courseHeight - o.y + 63.75, fill="black", width=1)
                        elif objectType == "door":
                                self.canvas.create_line(o.x,self.courseHeight - o.y,o.width,self.courseHeight - o.height,fill="grey", width=1)
                                self.canvas.create_line(o.x,self.courseHeight - (o.y-20),o.x,self.courseHeight - (o.height+20), fill="black", width=4)
                                self.canvas.create_line(o.width,self.courseHeight - (o.y-20),o.width,self.courseHeight - (o.height+20), fill="black", width=4)
                        elif objectType == "barrier":
                                self.canvas.create_line(o.x,self.courseHeight - o.y,o.width,self.courseHeight - o.height, fill="black", width=4)

                for o in self.waypointList():
                        objectType = o.oType
                        if objectType == "waypoint":
                                self.canvas.create_oval(o.x-2, o.y-2, o.x+2, o.y+2,fill="red")
                        
                #Rotate and paint the chariot
                self.canvas.create_polygon(self.getChariotPoints(), fill="#FFFF00", outline="black")
                self.canvas.create_text(60,515, font="Sans 10 underline", text="Information Panel")
                self.canvas.create_text(48,540, font="Sans 9", text="\n Bearing:\n degrees= {0}\n radians= {1:.3}".format(self.chariotBearing,(self.chariotBearing*0.0174533)))
                self.canvas.create_text(40,585, font="Sans 9", text="\n Position:\n x= {0}mm\n y= {1}mm".format(self.chariotx,self.charioty))
                
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
            points[i] = (int(tx + cx)+self.xoffset,self.courseHeight - (int(ty+cy)+self.yoffset))
        #print(points)
        return points


