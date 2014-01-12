

from datetime import datetime
import registry
import logger
import main
import ftool
from cache import *
from service import *

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
        error = eval("app." + mode + "Action()")
    else:
        error = app.main()
    
    if (error is not None):
        logger.logException(error)
        
    return False