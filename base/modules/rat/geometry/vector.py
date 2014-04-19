import math
from OpenGL.GL import *

class vector:
    x = 0.0
    y = 0.0
    z = 0.0
    
    def __init__(self):
        return
    
    def __init__(self,x,y):
        self.add2f(x,y)
    
    def __init__(self,x,y,z):
        self.add3f(x,y,z)
    
    def isBefore2f(self,x,y):
        return (self.x < x and self.y < y)
    
    def isBefore3f(self,x,y,z):
        return (self.x < x and self.y < y and self.z < z)
    
    def isAfter2f(self,x,y):
        return (self.x > x and self.y > y)
    
    def isAfter3f(self,x,y,z):
        return (self.x > x and self.y > y and self.z > z)
    
    def isBeforeAbs2f(self,x,y):
        return (abs(self.x) < abs(x) and abs(self.y) < abs(y))
    
    def isBeforeAbs3f(self,x,y,z):
        return (abs(self.x) < abs(x) and abs(self.y) < abs(y) and abs(self.z) < abs(z))
    
    def isAfterAbs2f(self,x,y):
        return (abs(self.x) > abs(x) and abs(self.y) > abs(y))
    
    def isAfterAbs3f(self,x,y,z):
        return (abs(self.x) > abs(x) and abs(self.y) > abs(y) and abs(self.z) > abs(z))
    
    def equal2f(self,x,y):
        return (self.x == x and self.y == y)
    
    def equal3f(self,x,y,z):
        return (self.x == x and self.y == y and self.z == z)
    
    def add(self,f):
        self.add3f(f,f,f)
        return self
    
    def add2f(self,x,y):
        self.add3f(x,y,0)
        return self
    
    def add3f(self,x,y,z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        return self
    
    def mul(self,f):
        self.mul3f(f,f,f)
        return
    
    def mul2f(self,x,y,z):
        self.mul3f(x,y,1.0)
        return self
    
    def mul3f(self,x,y,z):
        self.x = self.x * x
        self.y = self.y * y
        self.z = self.z * z
        return self
    
    def vmul3f(self,x,y,z):
        self.x = (y * self.z) - (z * self.y)
        self.y = (z * self.x) - (x * self.z)
        self.z = (x * self.y) - (y * self.x)
        return self
    
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def toArray(self):
        return [self.x, self.y, self.z]

class vertexManager:
    vectors = []
    
    def clear(self):
        for v in self.vectors:
            del v
        self.vectors = []
        return self
    
    def addVector2f(self, x, y):
        self.vectors.append(vector(x, y, 0.))
        return self
    
    def addVector3f(self, x, y, z):
        self.vectors.append(vector(x, y, z))
        return self
    
    def addVectorv(self, vec):
        self.vectors.append(vec)
        return self
    
    def getVector(self, num):
        if (self.vectors in num):
            return self.vectors[num]
        else:
            return None
    
    def render(self, mode):
        glBegin(mode)
        for v in self.vectors:
            vec = v.toArray()
            glVertex3f(vec[0], vec[1], vec[2])
        glEnd()
        return self
    
    def add2f(self,x,y):
        for v in self.vectors:
            v.add2f(x,y)
        return self
    
    def add3f(self,x,y,z):
        for v in self.vectors:
            v.add3f(x,y,z)
        return self
    
    def mul2f(self,x,y):
        for v in self.vectors:
            v.mul2f(x,y)
        return self
    
    def mul3f(self,x,y,z):
        for v in self.vectors:
            v.mul3f(x,y,z)
        return self
    
    def vmul3f(self,x,y,z):
        for v in self.vectors:
            v.vmul3f(x,y,z)
        return self
    
    def toArray(self):
        result = []
        for v in self.vectors:
            result.append(v.toArray())
        return result
    
    def isOver2f(self, x, y):
        after = False
        before = False
        for v in self.vectors:
            if (v.x < x and v.y < y):
                before = True
            if (v.x >= x and v.y >= y):
                after = True
        return (after and before)
    
    def isOver3f(self, x, y, z):
        after = False
        before = False
        for v in self.vectors:
            if (v.x < x and v.y < y and v.z < z):
                before = True
            if (v.x >= x and v.y >= y and v.z >= z):
                after = True
        return (after and before)
    
    def isOut2f(self, x, y):
        after = False
        before = False
        for v in self.vectors:
            if (v.x < x and v.y < y):
                before = True
            if (v.x >= x and v.y >= y):
                after = True
        return not (after and before)
    
    def isOut3f(self, x, y, z):
        after = False
        before = False
        for v in self.vectors:
            if (v.x < x and v.y < y and v.z < z):
                before = True
            if (v.x >= x and v.y >= y and v.z >= z):
                after = True
        return not (after and before)
        