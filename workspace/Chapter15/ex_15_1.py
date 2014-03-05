import math
class Point(object):
    pass

def distance_between_points( p1, p2):
    distance = math.sqrt((p2.x-p2.x)**2 + (p2.y - p1.y)**2)
    print distance
    
    
p1 = Point()
p2 = Point()
p1.x = 1
p2.y = 4
p1.y = 2
p2.x = 3

distance_between_points(p1, p2)