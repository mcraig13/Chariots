
### Superclass for various course types.
class Course:

    ### Empty constructor.
    def __init__(self, filename):
        self.objects = []
        self.filename = filename
        self.readCsv(filename)
        

    ### (Stub) Read obstacles in from a csv file.
    ### returns => a list of obstacles.
    def readCsv(self, filename):
        with open(filename,'r') as cFile:
            for line in cFile:
                tokens = line.split(',')
                if 'course' in tokens[0]:
                    self.objects.append(Arena('course',eval(tokens[1])/10,eval(tokens[2])/10,eval(tokens[3])/10,eval(tokens[4])/10))
                elif 'pole' in tokens[0]:
                    self.objects.append(Pole('pole',eval(tokens[1])/10,eval(tokens[2])/10))
                elif 'wall' in tokens[0]:
                    self.objects.append(Wall('wall',eval(tokens[1])/10,eval(tokens[2])/10,\
                                               eval(tokens[3])/10,eval(tokens[4])/10))
                elif 'waypoint' in tokens[0]:
                    self.objects.append(Waypoint('waypoint',eval(tokens[1])/10,eval(tokens[2])/10))
                elif 'ramp' in tokens[0]:
                    self.objects.append(Ramp('ramp',eval(tokens[1])/10,eval(tokens[2])/10,\
                                                eval(tokens[3])/10,eval(tokens[4])/10))
                elif 'barrel' in tokens[0]:
                    self.objects.append(Barrel('barrel',eval(tokens[1])/10,eval(tokens[2])/10))
                elif 'ball' in tokens[0]:
                    self.objects.append(Ball('ball',eval(tokens[1])/10,eval(tokens[2])/10))
                elif 'net' in tokens[0]:
                    self.objects.append(Net('net',eval(tokens[1])/10,eval(tokens[2])/10))
                elif 'door' in tokens[0]:
                    self.objects.append(Door('door',eval(tokens[1])/10,eval(tokens[2])/10))
                                
### Superclass for all obstacles.
### x -> the x axis position of the obstacle in mm.
### y -> the y axis position of the obstacle in mm.
class Obstacle(object):
    def __init__(self,oType,x,y,width=0,height=0,a0=0,a1=0):
        self.oType = oType
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.passable = False

### The arena.
### width -> width of the arena in mm.
### height -> height of the arena in mm.
class Arena(Obstacle):
    def __init__(self,oType,x,y,width,height):
        super(Arena, self).__init__(oType,x,y)
        self.width = width
        self.height = height

### A pole of diameter 50mm.
class Pole(Obstacle):
    def __init__(self,oType,x,y, width=5, height=5):
        super(Pole, self).__init__(oType,x,y)
        self.oType = oType
        self.width = width
        self.height = height

### An impassible wall.
### x -> x position of one end in mm.
### y -> y position in one end mm.
### x1 -> x position of the other end in mm.
### y1 -> y position of the other end in mm.
class Wall(Obstacle):
    def __init__(self,oType,x,y,x1,y1):
        super(Wall, self).__init__(oType,x,y)
        self.x1 = x1
        self.y1 = y1
        
### A point on the arena where the chariot should travel to.
### x -> x position of the point
### y -> y position of the point
class Waypoint(Obstacle):
    def __init__(self,oType,x,y):
        super(Waypoint, self).__init__(oType,x,y)
        
### A ramp of size 50x150mm.
### x -> the x axis position in mm.
### y -> the y axis position in mm.
class Ramp(Obstacle):
    def __init__(self,oType,x,y):
        super(Ramp, self).__init__(oType,x,y)
        self.width = 50
        self.length = 150
        self.passable = True

### A barrel.
### x -> the x axis position in mm.
### y -> the y axis position in mm.
class Barrel(Obstacle):
    def __init__(self,oType,x,y):
        super(Barrel,self).__init__(oType,x,y)
        self.passable = True

### A ball.
### x -> the x axis position in mm.
### y -> the y axis position in mm.
class Ball(Obstacle):
    def __init__(self,oType,x,y):
        super(Ball,self).__init__(oType,x,y)
        self.passable = True

### A net.
### x -> the x axis position in mm.
### y -> the y axis position in mm.
class Net(Obstacle):
    def __init__(self,oType,x,y):
        super(Net, self).__init__(oType,x,y)
        self.passable = True

### A door.
### x -> the x axis position in mm.
### y -> the y axis position in mm.
class Door(Obstacle):
    def __init__(self,oType,x,y):
        super(Door, self).__init__(oType,x,y)
