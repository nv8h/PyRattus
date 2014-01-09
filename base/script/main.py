from rattus import ftool, service
from rattus import *

__PROGRAMNAME__ = "programname"

def main():
    # set programname
    registry.setValue("programname", __PROGRAMNAME__)
    
    # Create and Check Local Share Directory
    ftool.checkDir(__PROGRAMNAME__)
    
    # Return with Error Message
    return None