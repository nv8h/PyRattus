from rattus import registry
import abstract
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class glut(abstract.abstract):
    
    def __init__(self):
        self.params['mode'] = GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH
        self.params['timeout'] = 20
        self.params['x'] = -1
        self.params['y'] = -1
        self.params['width'] = 640
        self.params['height'] = 400
        self.params['title'] = registry.getValue('programname')
        
        self.initParams()
        glutInit(sys.argv)
        glutInitWindowPosition(self.params['x'],self.params['y'])
        glutInitWindowSize(self.params['width'],self.params['height'])
        glutInitDisplayMode(self.params['mode'])
        self.windowId =  glutCreateWindow(self.params['title'])
        glutSetWindow(self.windowId)
        glutDisplayFunc(self.render)
        glutIdleFunc(self.idle)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.mouseMotion)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboardSpecial)
        glutTimerFunc(self.params['timeout'], self.timer, 0)
        glutReshapeFunc(self.reshape)
        
        self.init()
        return
    
    def activate(self):
        glutSetWindow(self.windowId)
        return self
    
    def destroy(self):
        glutDisplayWindow(self.windowId)
        del self
        return
    
    def redisplay(self):
        self.activate()
        glutPostRedisplay()
        return self
    
    def run(self):
        self.activate()
        glutPostRedisplay()
        glutMainLoop()
        return self
    
    def hide(self):
        self.activate()
        glutHideWindow()
        return self
    
    def show(self):
        self.activate()
        glutShowWindow()
        return self
    
    def setPosition(self, x, y):
        self.activate()
        self.params['x'] = x
        self.params['y'] = y
        glutPositionWindow(x,y)
        return self
    
    def setResolution(self, width, height):
        self.activate()
        self.params['width'] = width
        self.params['height'] = height
        glutReshapeWindow(width, height)
        return self
    
    def title(self, title):
        self.activate()
        self.params['title'] = title
        glutSetWindowTitle(title)
        return self
    