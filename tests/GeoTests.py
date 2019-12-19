from components.cache import GeoCache
from tests.helpers.testHelper import test
from components.entity.PointEntity import Point
import time

"""
    Question: 
    At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new
    library that can be integrated to the Ormuco stack. Dealing with network issues everyday,
    latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least
    Recently Used) cache with time expiration. This library will be used extensively by many of our
    services so it needs to meet the following criteria:
 
    1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema
    7 - Cache can expire
"""

instance = GeoCache()
instance.setLogLevel(None)
instance.start()

def beforeEachTest():
    instance.start()
    instance.flushAll()

def afterEachTest():
    instance.stop()

def insertT():
    instance.add("test", "ok!")
    assert instance.get("test").value == "ok!"

def timeoutT():
    instance.add("timeoutTest", "must return none", 1)
    time.sleep(2)
    assert instance.get("timeoutTest") is None

def flushT():
    instance.add("timeoutTest", "must return none", 1)
    instance.flushAll()
    assert instance.get("timeoutTest") is None

def autoTurnOnT():
    instance.stop()
    assert instance.getStatus() == False
    insertT()

def extendTimeT():
    instance.add("timeoutTest", "must return none", 1)
    time.sleep(2)
    instance.extendsTime("timeoutTest", 5)
    assert instance.get("timeoutTest").value == "must return none"

def saveObjectT():
    point = Point(2,6)
    differentPoint = Point(1,2)
    instance.add("pt", point)
    assert instance.get("pt").value == point
    assert instance.get("pt").value != differentPoint
    

test("Must get saved value from cache",insertT, beforeEachTest, afterEachTest)
test("Must return none when saved item expires", timeoutT, beforeEachTest, afterEachTest)
test("Must return none when saved item was flush", flushT, beforeEachTest, afterEachTest)
test("Must auto start cache when get/set with status off", autoTurnOnT, beforeEachTest, afterEachTest)
test("Must extends time and return value", extendTimeT, beforeEachTest, afterEachTest)
test("Must saves a Object", saveObjectT, beforeEachTest, afterEachTest)