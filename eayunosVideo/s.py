from swampy.TurtleWorld import *
from math import *

def s_arc(t, r):
   arc_angle = 180.0
   c = 2.0 * pi * r
   n = int(c / 3.0) + 1
   arc_length = c / 2.0
   step_length = arc_length / n
   step_angle = arc_angle / n
   for i in range(n):
      fd(t, step_length)
      lt(t, step_angle)
   for i in range(n):
      fd(t, step_length)
      rt(t, step_angle)
   fd(t, r)
