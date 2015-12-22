from TurtleWorld import *
from math import *

def n_arc(t, R, r):
   a = atan(2 / 3.0)
   angle = 360.0 * a / (2 * pi)
   arc_angle = 2 * angle
   c = 2.0 * pi * r
   n = int(c / 3.0) + 1
   arc_length = arc_angle * c / 360.0
   step_length = arc_length / n
   step_angle = arc_angle / n
   fd(t, R)
   bk(t, r * (1 - sqrt(2) / 2.0))
   rt(t, 90 - angle)
   for i in range(n):
      fd(t, step_length)
      rt(t, step_angle)
   rt(t, 90 - angle)
   fd(t, R - r * (1 - sqrt(2) / 2.0))
