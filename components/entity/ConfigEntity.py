class Config:
    def __init__(self, 
        ttl: int = 60, 
        namespace: str = "default", 
        reconnectOnError: bool = True, 
        maxLength: int = 256,
        historyEnabled: bool = False):
        self.ttl = ttl
        self.namespace = namespace
        self.maxLength = maxLength
        self.historyEnabled = historyEnabled
