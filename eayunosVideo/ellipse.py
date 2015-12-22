from TurtleWorld import *
from math import *

def circle(t, r):
   c = 2 * pi * r
   n = int(c / 3) + 1
   l = c / n
   angle = 360.0 * l / c
   for i in range(n):
      fd(t, l)
      lt(t, angle)
"""
world = TurtleWorld()
Bob = Turtle()
Bob.delay = 0.01
circle(Bob, 50)
wait_for_user()
"""
