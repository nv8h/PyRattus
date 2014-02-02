import sys
import os
import rattus

def log(msg, desc=""):
    
    now   = rattus.datetime.now()
    files = rattus.registry.getValue("file")
    
    if (files is not None and "log" in files):
        os.system("echo '[" + str(now) + "] " + desc + ": " + msg + "' >> " + files["log"])
        return True
    # end if
    
    print ("Warning: \"log\" key does not exists")
    print (msg)
    return False

def logException(msg):
    return log(msg, "Exception")
    
def logInfo(msg):
    return log(msg, "Info")

def logWarning(msg):
    return log(msg, "Warning")

def debug(msg):
    return log(msg, "Debug")