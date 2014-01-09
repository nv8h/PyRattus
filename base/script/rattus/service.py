import os, urllib2, httplib, rattus

class webserviceGET:
    
    config = {
        "host": "127.0.0.1",
        "href": "",
        "protocol": "http",
        "port": 80,
        "username": "",
        "password": ""
    }
    
    request = ""
    response = ""
    
    def __init__(self, config = {}):
        for i in config:
            self.config[i] = config[i]
        return
    
    def getHref(self):
        return self.config["href"]
    
    def setHref(self, href):
        self.config["href"] = href
    
    def getProtocol(self):
        return self.config["protocol"]
    
    def setProtocol(self, protocol):
        self.config["protocol"] = protocol
    
    def getPort(self):
        return self.config["port"]
    
    def setPort(self, port):
        self.config["port"] = port
    
    def getUsername(self):
        return self.config["username"]
    
    def setUsername(self, username):
        self.config["username"] = username
    
    def setPassword(self, password):
        self.config["password"] = password
    
    def getHost(self):
        return self.config["host"]
    
    def setHost(self, host):
        self.config["host"] = host
    
    def getUrl(self):
        host = ""
        if (len(self.config["username"]) > 0):
            host = str(self.config["username"])
            if (len(self.config["password"]) > 0):
                host = host + ":" + str(self.config["password"])
            host = host + "@"
        host = host + self.config["host"]
        url = self.config["protocol"] + "://" + host + ":" + str(self.config["port"]) + "/" + str(self.config["href"])
        return url
    
    def getRequest(self):
        return self.request
    
    def getResponse(self):
        return self.response
    
    def send(self, args = {}):
        url = self.getUrl()
        if (len(args) > 0):
            url = url + "?"
            cfg = []
            for i in args:
                cfg.append(str(i) + "=" + str(args[i]))
            url = url + "&".join(cfg)
        self.request = urllib2.Request(url)
        self.response = urllib2.urlopen(self.request)
        return
    
    








