import sys
#from OpenGL.GLUT import *
#from OpenGL.GLU import *
#from OpenGL.GL import *

class abstract:
    
    params = {}
    windowId = None
    
    def initParams(self):
        pass
    
    def __init__(self):
        self.initParams()
        self.init()
        pass
    
    def init(self):
        pass
    
    def mouse(self, button, state, x, y):
        pass
    
    def mouseMotion(self, x, y):
        pass
    
    def keyboard(self, asciiCode, x, y):
        pass
    
    def keyboardSpecial(self, key, x, y):
        pass
    
    def idle(self):
        pass
    
    def timer(self, value):
        pass
    
    def render(self):
        pass
    
    def run(self):
        pass
    
    def destroy(self):
        del self
        pass
    
    def redisplay(self):
        pass
    