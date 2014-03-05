from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
#===============================================================================
#  this code is working fine
# def arc(t, length, n, angle):
#     for i in range(n):
#      fd(t, length)
#      lt(t, angle)
#      
# arc(bob, 5, 38, 10)
#===============================================================================
   
def arc (t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = flaot(angle) / n
    
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)
        
    
arc (bob, 5, 10)
     
wait_for_user()