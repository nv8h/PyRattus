import pygtk
pygtk.require('2.0')
import gtk
import abstract
from rat import registry


class wgtk(abstract.abstract):

    __wnd__ = None
    
    def run(self):
        gtk.main()
        return

    def __init__(self):
        self.params['timeout'] = 20
        self.params['border'] = {}
        self.params['border']['width'] = 10
        self.params['x'] = -1
        self.params['y'] = -1
        self.params['width'] = 640
        self.params['height'] = 400
        self.params['title'] = registry.getValue('programname')
        
        self.initParams()

        # Initalize Window
        self.initWindow()
        self.initElements()

        self.init()
        return

    def initWindow(self):
        self.__wnd__ = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.__wnd__.set_size_request(self.params['width'], self.params['height'])
        self.__wnd__.set_border_width(self.params['border']['width'])
        self.__wnd__.set_title(self.params['title'])
        self.__wnd__.connect("delete_event", lambda w,e: gtk.main_quit())
        self.show()
        return

    def initElements(self):
        return

    def hide(self):
        self.__wnd__.hide()
        return

    def show(self):
        self.__wnd__.show()
        return
