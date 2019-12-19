from components.entity.PointEntity import Point 

""" Question A Answer to Unity Tests """

class RowComponent:
    def __init__(self, x1 = None, x2 = None) :
        points = Point(None, None)
        if(x1 > x2):
            points.first = x2
            points.second = x1
        else:
            points.first = x1
            points.second = x2
        
        self.points = points

    def isBetween(self, component: Point):
        return (self.points.first > component.first and self.points.first < component.second) or (self.points.second > component.first and self.points.second < component.second)

    def getPoint(self): return self.points
