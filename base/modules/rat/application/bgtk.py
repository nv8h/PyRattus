"""
GtkBuilder
"""


import sys
from rat import logger, registry

try:
	import gtk
except:
    logger.logException("gtk not available")
    logger.logInfo("try to install python-gtk2 package")
    sys.exit(1)

import abstract

class bgtk(abstract.abstract):

    __element__ = {}
    __builder__ = None
    
    def run(self):
        gtk.main()
        return

    def __init__(self):
        self.params['filename'] = None
        
        self.initParams()

        # Initalize Window
        self.initWindow()
        self.initElements()

        self.init()
        return

    def initWindow(self):
        try:
            self.__builder__ = gtk.Builder()
            self.__builder__.add_from_file(self.params['filename'])
            self.__builder__.connect_signals(self)
        except:
            logger.logException("Error has occurred while GtkBuilder try to load \"" + self.params['gladeFilename'] + "\" XML file")
            logger.logInfo("More info: " + str(sys.exc_info()))
            sys.exit(1)
        return

    def initElements(self):
        return

    def quit(self):
        gtk.main_quit()
        return

    def getBuilder(self):
        return self.__builder__



