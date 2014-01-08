from ConfigParser import ConfigParser
import json
import os

def xdgOpen(link):
    return os.system("xdg-open '" + link + "'")
    
def playMPG(filepath, flags=""):
    return os.system("mpg123 " + flags + " '" + filepath + "'")

def terminal(cmd=""):
    if (cmd == ""):
        return os.system("xterm")
    else:
        return os.system("xterm -e '" + cmd + "'")
    #end if

def checkDir(dir=""):
    homedir = os.path.expanduser("~")
    dir = "/" + dir
    
    if (os.path.isdir(homedir + "/.local") == False):
        os.mkdir(homedir + "/.local")
        if (os.path.isdir(homedir + "/.local/share") == False):
            os.mkdir(homedir + "/.local/share")
            if (os.path.isdir(homedir + "/.local/share" + dir) == False):
                os.mkdir(homedir + "/.local/share" + dir)
            # end if
        # end if
    # end if
    return os.path.isdir(homedir + "/.local/share" + dir)

def putContents(filepath, content):
    if (os.path.isfile(filepath) == False):
        return None
    # end if
    f = open(filepath, "w")
    content = f.write(content)
    f.close()
    return content

def getContents(filepath):
    if (os.path.isfile(filepath) == False):
        return None
    # end if
    f = open(filepath, "r")
    content = f.read()
    f.close()
    return content
    
def loadINIFile(filepath):
    if (os.path.isfile(filepath) == False):
        return None
    # end if
    cfgp = ConfigParser()
    cfgp.read(filepath)
    return cfgp
    

