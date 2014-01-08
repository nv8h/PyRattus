import sys
import time
import os
import rattus

class cache:
    enabled = 0
    path = ""
    lifetime = 0
    files = []
    
    def __init__(self, enabled = 0, path = "", lifetime = 0):
        self.enabled = enabled
        if (path == ""):
            path = rattus.registry.getValue("path")["cache"]
        self.path = path
        self.lifetime = lifetime
    
    def clearAll(self):
        for filepath in self.files:
            os.system("rm '" + self.path + "/" + filepath + "'")
        self.files = []
    
    def clear(self, cacheid):
        if (cacheid in self.files):
            os.system("rm '" + self.path + "/" + cacheid + "'")
    
    def testCache(self, cacheid):
        if (not cacheid in self.files):
            return False
        filepath = self.path + "/" + cacheid
        if (not os.path.is_file(filepath)):
            return False
        mtime = time.ctime(os.path.getmtime(filepath))
        ctime = time.ctime(os.path.getctime(filepath))
        if (ctime > mtime):
            mtime = ctime
        mtime = mtime - time.time()
        if (mtime >= self.lifetime):
            return False
        return True
    
    def save(self, cacheid, content=""):
        filepath = self.path + "/" + cacheid
        if (os.path.is_dir(filepath)):
            return
        rattus.fttol.putContents(filepath, content)
        self.files.append(cacheid)
    
    def load(self, cachid):
        if (not self.testCache(cacheid)):
            return None
        filepath = self.path + "/" + cacheid
        return rattus.ftool.getContents(filepath)


class cacheManager:
    
    caches = {}
    
    def getCache(self, name):
        if (name in self.caches):
            return self.caches[name]
        return None

    def setCache(self, name, cache):
        self.caches[name] = cache
    
    def testCache(self, name):
        return (name in self.caches)