from TurtleWorld import *
from math import *

def u_arc(t, R, r):
   a = atan(2 / 3.0)
   angle = 360.0 * a / (2 * pi)
   arc_angle = 2 * angle
   c = 2.0 * pi * r
   n = int(c / 3.0) + 1
   arc_length = arc_angle * c / 360.0
   step_length = arc_length / n
   step_angle = arc_angle / n
   fd(t, R - r * (1 - sqrt(2) / 2.0))
   lt(t, 90 - angle)
   for i in range(n):
      fd(t, step_length)
      lt(t, step_angle)
   lt(t, 90 - angle)
   fd(t, R - r * (1 - sqrt(2) / 2.0))
   bk(t, R) 
