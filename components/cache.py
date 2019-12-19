from components.entity.ConfigEntity import Config
from components.entity.RegisterEntity import CacheRegister
from datetime import datetime
import asyncio
import time

class GeoCache:

    def __init__(self, conf: Config = Config()):
        self.c = conf
        self.__cached = {}
        self.__history = []
        self.__started = False
        self.__logLevel = 'all'

    def __logger(self, message, level: str):
        if(self.__logLevel == 'all' or level == self.__logLevel):
            print(message)

    def __sysLog(self, message): self.__logger(message, "sys")
    def __debugLog(self, message): self.__logger(message, "debug")
    def __warnLog(self, message): self.__logger(message, "warn")
    def __errLog(self, message): self.__logger(message, "err")
    def __infoLog(self, message): self.__logger(message, "info")

    def __getnow(self):
        return datetime.timestamp(datetime.now())

    def __calcTtl(self, ttl: int = None):
        ttl = self.c.ttl if ttl is None else ttl
        return self.__getnow() + ttl

    def __saveHistory(self, key: str):
        if(self.c.historyEnabled): 
            self.__debugLog("Saving history {} to {}".format(key, self.__cached[key]))
            self.__history.append(self.__cached[key])
        if(len(self.__history) > self.c.maxLength): 
            self.__debugLog("History length overflow, removing first inserted key: {}".format(self.__history[0]))
            self.__history.pop(0)

    def __checkIfTurnedOn(self): 
        if(not self.__started): 
            self.__debugLog("Turning On Cache Service")
            self.start()

    async def __flush(self):
        self.__sysLog("Automatic Flush Started")
        while(True):
            if(not self.__started): 
                self.__sysLog("Automatic Flush Stoped")
                break
            self.__flushInvalids()
            time.sleep(5)

    def __flushInvalids(self):
        removed = 0
        for key, value in self.__cached.items():
            if(value.ttl < self.__getnow()): 
                self.__cached.pop(key)
                removed += 1
        self.__sysLog("Removed {} invalid caches".format(removed))

    def start(self):
        if(not self.__started):
            self.__infoLog("Cache System Started")
            asyncio.run(self.__flush())
            self.__started = True
        else:
            self.__infoLog("Cache System already started")

    def stop(self):
        if(self.__started):
            self.__started = False
            self.flushAll()
            self.__infoLog("Cache System Stoped")

    def add(self, key: str, value: str, ttl: int = None):
        self.__checkIfTurnedOn()
        self.__debugLog("Saving data to cache")
        self.__cached[key] = CacheRegister(value, self.__calcTtl(ttl))
        self.__debugLog("Data saved to cache")
        self.__saveHistory(key)

    def get(self, key: str):
        self.__checkIfTurnedOn()
        self.__debugLog("Get key {} from cache".format(key))
        return None if key not in self.__cached or (self.__cached[key] is None or self.__cached[key].ttl <= datetime.timestamp(datetime.now())) else self.__cached[key]

    def flushAll(self): 
        self.__sysLog("Flushed all data in cache")
        self.__cached = {}

    def validate(self, key: str):
        return key in self.__cached and self.__cached[key] is not None or self.__cached[key].ttl > datetime.timestamp(datetime.now())

    def extendsTime(self, key: str, ttl: int = None):
        self.__checkIfTurnedOn()
        if(key not in self.__cached):
            self.__sysLog("Key {} does not exists. Raise exception".format(key))
            raise Exception("Key {} does not exists!".format(key))
        
        self.__cached[key].ttl = self.__calcTtl(ttl)
        self.__saveHistory(key)

    def reRun(self, lastTimestamp: int, cb):
        self.__checkIfTurnedOn()
        if(not self.c.historyEnabled):
            raise Exception("Your history need to be enabled to use that feature")

        for history in self.__history:
            if(history.ttl > lastTimestamp):
                cb(history)
    
    def getStatus(self):
        return self.__started
    
    def setLogLevel(self, logLevel):
        self.__logLevel = logLevel