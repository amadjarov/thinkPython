class Rectangle(object):
    pass

class Point (object):
    pass

box = Rectangle()
box.width = 2
box.hight = 3
box.corner = Point()
box.corner.x = 6
box.corner.y = 7

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    print rect.corner.x, rect.corner.y

print box.corner.x, box.corner.y
move_rectangle(box, 10, 10)