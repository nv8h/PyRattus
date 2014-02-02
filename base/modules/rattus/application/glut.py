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
        glutTimerFunc(self.params['timeout'], self.timer, 0);
        
        self.init()
        pass
    
    def activate(self):
        glutSetWindow(self.windowId)
        pass
    
    def destroy(self):
        glutDisplayWindow(self.windowId)
        del self
        pass
    
    def redisplay(self):
        self.activate()
        glutPostRedisplay()
        pass
    
    def run(self):
        self.activate()
        glutPostRedisplay()
        glutMainLoop()
        pass