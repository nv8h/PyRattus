# import sys
from rat import application,ftool,geometry,registry
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


# set programname
__PROGRAMNAME__ = "programname"
registry.setValue("programname", __PROGRAMNAME__)

class application(application.glut):
    
    vecmove = [0.01, 0.005]
    vec = None
    
    def initParams(self):
        self.params['width'] = 400
        self.params['height'] = 400
        return self
    
    def init(self):
        # Create and Check Local Share Directory
        ftool.checkDir(__PROGRAMNAME__)
        self.vec = geometry.vertexManager()
        self.vec.addVector2f(-0.5, 0.).addVector2f( 0.,-0.5).addVector2f( 0.5, 0.).addVector2f( 0., 0.5)
        return
    
    def render(self):
        glClearColor(0.,0.,0.,1.)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        
        glColor3f(1,0,0)
        self.vec.render(GL_QUADS)
        
        glPopMatrix()
        glutSwapBuffers()
        return
    
    def timer(self,value):
        vecs = self.vec.toArray()
        
        if (abs(vecs[0][0]) >= 1.0):
            self.vecmove[0] = self.vecmove[0] * -1
        if (abs(vecs[0][1]) >= 1.0):
            self.vecmove[1] = self.vecmove[1] * -1
        if (abs(vecs[1][0]) >= 1.0):
            self.vecmove[0] = self.vecmove[0] * -1
        if (abs(vecs[1][1]) >= 1.0):
            self.vecmove[1] = self.vecmove[1] * -1
        if (abs(vecs[2][0]) >= 1.0):
            self.vecmove[0] = self.vecmove[0] * -1
        if (abs(vecs[2][1]) >= 1.0):
            self.vecmove[1] = self.vecmove[1] * -1
        if (abs(vecs[3][0]) >= 1.0):
            self.vecmove[0] = self.vecmove[0] * -1
        if (abs(vecs[3][1]) >= 1.0):
            self.vecmove[1] = self.vecmove[1] * -1


        self.vec.add2f(self.vecmove[0],self.vecmove[1])
        self.redisplay()
        glutTimerFunc(self.params['timeout'], self.timer, value)
        return
    
    def mainAction(self):
        # to run this file "launcher.sh"
        print("Welcome to the 'normal' mode")
        self.title('PyRattus DEMO')
        self.run()
        # Return with Error Message
        return None

    def serviceAction(self):
        # to run this file "service.sh"
        print("Welcome to the 'service' mode")

        # Return with Error Message
        return None
