
registry_data = {}
        
def setValue(key, value):
    registry_data[key] = value
    return
    
def getValue(key):
    if (key in registry_data):
        return registry_data[key]
    # end if
    return None
    
def testKey(key):
    return (key in registry_data)
    
    