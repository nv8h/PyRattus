

from datetime import datetime
import registry
import logger
import main
from cache import cache
import ftool
import service

def init():
    logger.debug("Initializing...")
    
    error = main.main()
    
    if (error is not None):
        logger.logException(error)
        
    return False