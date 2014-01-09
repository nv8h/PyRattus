import sys
from rattus import ftool, service
from rattus import *

__PROGRAMNAME__ = "programname"

class application:
    
    def __init__(self):
        # set programname
        registry.setValue("programname", __PROGRAMNAME__)
        
        # Create and Check Local Share Directory
        ftool.checkDir(__PROGRAMNAME__)
        return
    
    def main(self):
        # to run this file "launcher.sh"
        print("Welcome to the 'normal' mode")

        # Return with Error Message
        return None

    def service(self):
        # to run this file "service.sh"
        print("Welcome to the 'service' mode")

        # Return with Error Message
        return None