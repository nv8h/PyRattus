import math
from OpenGL.GL import *

class vector:
    x = 0.0
    y = 0.0
    z = 0.0
    
    def __init__(self):
        pass
    
    def __init__(self,x,y,z):
        self.add3f(x,y,z)
        return
    
    def add(self,f):
        self.add3f(f,f,f)
        pass
    
    def add2f(self,x,y):
        self.add3f(x,y,0)
        pass
    
    def add3f(self,x,y,z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        pass
    
    def mul(self,f):
        self.mul3f(f,f,f)
        pass
    
    def mul2f(self,x,y,z):
        self.mul3f(x,y,1.0)
        pass
    
    def mul3f(self,x,y,z):
        self.x = self.x * x
        self.y = self.y * y
        self.z = self.z * z
        pass
    
    def vmul3f(self,x,y,z):
        self.x = (y * self.z) - (z * self.y)
        self.y = (z * self.x) - (x * self.z)
        self.z = (x * self.y) - (y * self.x)
        pass
    
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
    
    def addVector2f(self, x, y):
        self.vectors.append(vector(x, y, 0.))
    
    def addVector3f(self, x, y, z):
        self.vectors.append(vector(x, y, z))
    
    def addVectorv(self, vec):
        self.vectors.append(vec)
    
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
    
    def add2f(self,x,y):
        for v in self.vectors:
            v.add2f(x,y)
    
    def add3f(self,x,y,z):
        for v in self.vectors:
            v.add3f(x,y,z)
    
    def toArray(self):
        result = []
        for v in self.vectors:
            result.append(v.toArray())
        return result
    
