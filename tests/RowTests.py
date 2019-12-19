from components.points import RowComponent
from components.entity.PointEntity import Point
from tests.helpers.testHelper import test

"""
    Question: 
    Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the
    x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5)
    and (6,8).
"""

""" Question A Unity Tests """

classInstance = RowComponent(1,5)
secondInstance = RowComponent(7,1)

def notOverlapT():
    assert classInstance.isBetween(Point(2,6))
    assert classInstance.isBetween(Point(6,8)) == False

def overlapT(): assert classInstance.isBetween(secondInstance.getPoint())

def comparePointsT():
    assert secondInstance.getPoint().first == 1
    assert secondInstance.getPoint().second == 7

def newInstanceT():
    localInstance = RowComponent(2,5)
    assert localInstance.isBetween(Point(1,5))
    assert localInstance.isBetween(Point(6,7)) == False

test("must not overlap", notOverlapT)
test("must overlap", overlapT)
test("must compare points", comparePointsT)
test("must compare differents points", newInstanceT)


