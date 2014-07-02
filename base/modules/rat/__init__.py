
from datetime import datetime
import part
import registry
import logger

if (part.config['ftool'] == 1):
    import ftool
if (part.config['application'] == 1):
    import application
if (part.config['geometry'] == 1):
    import geometry
if (part.config['cache'] == 1):
    from cache import *
if (part.config['service'] == 1):
    from service import *
import main

def unload(code):
    part.config[code] = 0

def load(code):
    part.config[code] = 1

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
