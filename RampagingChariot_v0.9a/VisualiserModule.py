# -*- coding: utf-8 -*-
from Tkinter import *
from LoggerModule import *
import math, time, threading
import Queue



class Visualiser(LocationObserverAbstract):


    def __init__(self, chariotcf, course, waypoints):
            
        self.queue = Queue.Queue()    
        self.xoffset, self.yoffset = chariotcf.xoffset, chariotcf.yoffset 
        self.chariotBearing = 0
        self.chariotWidth, self.chariotLength = chariotcf.width, chariotcf.length
        self.chariot, self.course = chariotcf, course
        self.chariotx, self.charioty = 130, 15
        self.waypoints, self.waypointList = waypoints, course.getWaypointList
        self.objectList, self.wallList = course.getObjectList, course.getWallList
        self.root = Tk()
        self.root.wm_title("Rampyge Visualiser")
        self.courseWidth, self.courseHeight  = course.getCourseDimensions()[0], course.getCourseDimensions()[1]
        self.canvas = Canvas(self.root, width=self.courseWidth,height=self.courseHeight)
        self.root.geometry = ('%dx%d+%d+%d' % (self.courseWidth, self.courseHeight, 0, 0))
        
        self.root.resizable(False,False)
        self.canvas.pack()
        self.root.after_idle(self.paint)
        self.root.update_idletasks()
        self.root.update()       
      
        
    def startMainLoop(self):
        self.root.mainloop()
        
        
    def locationUpdated(self, x, y, bearing):
    
        temp = (x,y,bearing)
        
        self.queue.put(temp)
        
        time.sleep(0.02)

        
    ### Redraw the contents of the window.
    def paint(self):
           
       try:
            while(True):
                
                temp = self.queue.get_nowait()
                                    
                self.chariotx = temp[0]
                self.charioty = temp[1]
                self.chariotBearing = temp[2]                  
                
                self.canvas.delete("all")
                self.canvas.create_rectangle(0,0,self.courseWidth,self.courseHeight,fill="white")
                points = []
                for o in self.wallList():
                        objectType = o.oType
                        if objectType == "wall":
                                points += o.x,o.y
                                self.canvas.create_line(o.x, o.y, o.width, o.height)
                self.canvas.create_polygon(points, fill="#408040", outline='black', width=2)
                self.canvas.create_line(32,32,468,468, fill="#DDDDDD", width=1) #diagonal marking
                self.canvas.create_oval(200,200,300,300, outline="#DDDDDD", width=1) #circle marking
                #self.canvas.create_oval(-20,self.courseHeight - (-20),20,self.courseHeight - 20, outline="black", width=2) #corner circle
                #self.canvas.create_line(15,self.courseHeight - 15,30,self.courseHeight - 30, fill="black", width=2)   #corner line
                self.canvas.create_line(190, 740, 190, 690, fill="#DDDDDD", width=4) #garage left
                self.canvas.create_line(310, 740, 310, 690, fill="#DDDDDD", width=4) #garage right
                
                for w in self.waypoints:
                    self.canvas.create_oval(w[0] ,self.courseHeight - w[1] , w[0] + 5, self.courseHeight - w[1] -5 ,fill="RED",outline="black", width=1 )
                   
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
                                self.canvas.create_line(o.x,    self.courseHeight - o.y,    o.width,   self.courseHeight - o.height, fill="grey", width=4)
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
                
                #Information Panel
                self.canvas.create_text(60,515, font="Sans 10 underline", text="Information Panel")
                self.canvas.create_text(48,545, font="Sans 9", text="\n Bearing:\n degrees= {0}\n radians= {1:.3}".format(((self.chariotBearing+90)%360),(((self.chariotBearing+90)%360)*0.0174533)))
                self.canvas.create_text(43,595, font="Sans 9", text="\n Position:\n x= {0}mm\n y= {1}mm".format(round(self.chariotx),round(self.charioty)))

                
                self.root.update_idletasks()

                
       except Queue.Empty:
            pass 
       self.root.after(10, self.paint)
             
    ### Finds the points required to draw a distance sensor
    
    def getChariotPoints(self):
        v = [self.chariotx - self.chariotWidth/2, self.chariotx+self.chariotWidth/2,\
                  self.charioty - self.chariotLength/2, self.charioty+self.chariotLength/2]
        points = [(v[0],v[2]),(v[1],v[2]),(v[1],v[3]),(v[0],v[3])]
        angle = -math.radians(self.chariotBearing)
        cx = self.chariotx
        cy = self.charioty
        
        for i in range (0,4): #rotational transform on each vertex
            x0 = points[i][0] - cx
            y0 = points[i][1] - cy
            tx= math.cos(angle)*x0-math.sin(angle)*y0      
            ty= math.sin(angle)*x0+math.cos(angle)*y0
            points[i] = (int(tx + cx),self.courseHeight - (int(ty+cy)))
        return points