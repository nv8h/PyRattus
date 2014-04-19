from rat import registry
import abstract
import pygame


class game(abstract.abstract):
    
    clock = None
    surface = None
    
    def __init__(self):
        self.params['timeout'] = 20
        self.params['sleeptime'] = 1
        self.params['x'] = -1
        self.params['y'] = -1
        self.params['width'] = 640
        self.params['height'] = 400
        self.params['title'] = registry.getValue('programname')
        
        self.initParams()
        self.surface = pygame.display.set_mode((self.params['width'], self.params['height']))
        pygame.display.set_caption(self.params['title'])
        
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
    