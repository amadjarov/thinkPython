from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0015

def circle(t, length, n):
    for i in range(n):
     fd(t, length)
     lt(t, 10)
     
circle(bob, 5, 38)
     
wait_for_user()