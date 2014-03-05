from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t):
    for i in range(4):
     fd(bob, 100)
     lt(bob)
     
square(bob)
     
wait_for_user()