# import sys
from rat import application,registry
import gtk



# set programname
__PROGRAMNAME__ = "programname"
registry.setValue("programname", __PROGRAMNAME__)

class application(application.wgtk):

    def initParams(self):
        return self

    def initElements(self):
        self.addButton('hwButton', {'title':'Click To Exit','action': [
            # name: name, action: function, data: self.__wnd__|None|...
            {'name': 'clicked', 'action': self.hwButtonClicked}
        ]})
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