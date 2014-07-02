# import sys
from rat import application,registry
import gtk



# set programname
__PROGRAMNAME__ = "programname"
registry.setValue("programname", __PROGRAMNAME__)

class application(application.wgtk):

    def initParams(self):
        self.params['gladeFilename'] = registry.getValue("path")["data"] + "/window/mainwindow-libglade.glade"
        self.params['actionDictionay']['on_btnHelloWorld_clicked'] = self.hwButtonClicked
        self.params['actionDictionay']['on_MainWindow_destroy'] = gtk.main_quit
        return

    def initElements(self):
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

    def hwButtonClicked(self, widget, data=None):
        self.quit()
        return