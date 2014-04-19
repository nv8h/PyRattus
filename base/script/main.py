# import sys
from rat import application,registry
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


# set programname
__PROGRAMNAME__ = "programname"
registry.setValue("programname", __PROGRAMNAME__)

class application(application.wgtk):

    def initParams(self):
        return self

    def mainAction(self):
        # to run this file "launcher.sh"
        print("Welcome to the 'normal' mode")
        #self.title('PyRattus DEMO')
        self.run()
        # Return with Error Message
        return None

    def serviceAction(self):
        # to run this file "service.sh"
        print("Welcome to the 'service' mode")

        # Return with Error Message
        return None
