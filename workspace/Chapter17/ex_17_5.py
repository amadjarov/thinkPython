class Point(object):
    def __add__(self,other):
        if isinstance(other,Point):
            return self.add_point(other)
        else:
            return self.print_point(other)

    def add_point(self,other):
        totalx = self.x + other.x
        totaly = self.y + other.y
        total = ('%d, %d') % (totalx, totaly)
        return total

    def print_point(self):
        print "(%d, %d)" % (self.x, self.y)

blank = Point()
blank.x = 3
blank.y = 5
blank1 = Point()
blank1.x = 5
blank1.y = 6