
from datetime import datetime
import registry
import logger
import ftool
import application
import geometry
from cache import *
from service import *
import main

def init(mode = ""):
    logger.debug("Initializing...")
    app = main.application()
    registry.setValue("application", app)
    
    error = None
    try:
        isfunc = eval("type(app." + mode + "Action)")
    except:
        isfunc = ""
        pass
    
    if (mode != "" and str(isfunc) == "<type 'instancemethod'>"):
        registry.setValue("mode", mode)
        error = eval("app." + mode + "Action()")
    else:
        registry.setValue("mode", "main")
        error = app.mainAction()
    
    if (error is not None):
        logger.logException(error)
    
    # Destroy window event
    try:
        eval("app.destroy()")
    except:
        pass
    
    return False
