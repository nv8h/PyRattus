# import sys
from rat import application,registry
import gtk



# set programname
__PROGRAMNAME__ = "programname"
registry.setValue("programname", __PROGRAMNAME__)

class application(application.bgtk):

    def initParams(self):
        self.params['filename'] = registry.getValue("path")["data"] + "/window/mainwindow0.glade"
        return

    def initElements(self):
        self.__builder__.get_object("MainWindow").show_all()
        self.__builder__.get_object("MainWindow").connect('destroy', self.on_MainWindow_destroy)
        self.__builder__.get_object("btnHelloWorld").connect('clicked', self.on_btnHelloWorld_clicked)
        return

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

    def on_btnHelloWorld_clicked(self, widget):
        self.quit()
        return

    def on_MainWindow_destroy(self, widget, data=None):
        self.quit()
        return