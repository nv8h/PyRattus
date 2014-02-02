import sys
#from OpenGL.GLUT import *
#from OpenGL.GLU import *
#from OpenGL.GL import *

class abstract:
    
    params = {}
    windowId = None
    
    def initParams(self):
        return self
    
    def __init__(self):
        self.initParams().init()
        return
    
    def init(self):
        return
    
    def mouse(self, button, state, x, y):
        return
    
    def mouseMotion(self, x, y):
        return
    
    def keyboard(self, asciiCode, x, y):
        return
    
    def keyboardSpecial(self, key, x, y):
        return
    
    def idle(self):
        return
    
    def timer(self, value):
        return
    
    def render(self):
        return
    
    def run(self):
        return self
    
    def destroy(self):
        del self
        return
    
    def redisplay(self):
        return self
    