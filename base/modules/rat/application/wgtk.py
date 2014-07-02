


import sys
from rat import logger, registry


try:
 	import pygtk
  	pygtk.require("2.0")
except:
    logger.logWarning("pygtk 2.0 not available")
    logger.logInfo("try to install python-gtk package")

try:
	import gtk
  	import gtk.glade
except:
    logger.logException("gtk or gtk.glade not available")
    logger.logInfo("try to install python-gtk2, python-glade2 packages")
    sys.exit(1)



import abstract

class wgtk(abstract.abstract):

    __element__ = {}
    wTree = None
    
    def run(self):
        gtk.main()
        return

    def __init__(self):
        self.params['gladeFilename'] = None
        self.params['actionDictionay'] = {}
        
        self.initParams()

        # Initalize Window
        self.initWindow()
        self.initElements()

        self.init()
        return

    def initWindow(self):
        try:
            self.wTree = gtk.glade.XML(self.params['gladeFilename'])
            self.wTree.signal_autoconnect(self.params['actionDictionay'])
        except:
            logger.logException("Error has occurred while glade try to load \"" + self.params['gladeFilename'] + "\" XML file")
            logger.logInfo("More info: " + str(sys.exc_info()))
            sys.exit(1)
        return

    def initElements(self):
        #window = self.wTree.get_widget("MainWindow")
		#window.connect("destroy", gtk.main_quit)
        pass

    def hide(self):
        window = self.wTree.get_widget("MainWindow")
        window.hide()
        return

    def show(self):
        window = self.wTree.get_widget("MainWindow")
        window.show()
        return

    def quit(self):
        gtk.main_quit()
        return

    def getWTree(self):
        return self.wTree



