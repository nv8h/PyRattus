

from datetime import datetime
import registry
import logger
import main
import ftool
from cache import *
from service import *

def init():
    logger.debug("Initializing...")
    
    error = main.main()
    
    if (error is not None):
        logger.logException(error)
        
    return False