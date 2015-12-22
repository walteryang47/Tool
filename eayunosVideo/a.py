# _*_ coding:utf-8 _*_

from swampy.TurtleWorld import *
from math import *
from ellipse import *
from u import *
from n import *
from s import *

def drawEayun(t):
   # print E
   bk(t, 50)
   rt(t, 90)
   fd(t, 25)
   lt(t, 90)
   fd(t, 50)
   bk(t, 50)
   rt(t, 90)
   fd(t, 25)
   lt(t, 90) 
   fd(t, 50)
   
   # print a
   pu(t)
   fd(t, 25 / 2.0)
   pd(t)
   circle(t, 50 / 4.0)
   pu(t)
   lt(t, 45)
   fd(t, sqrt(2) * 50 / 4.0)
   pd(t)
   rt(t, 180 - 45)
   fd(t, 50 / 4.0)

   # print y
   pu(t)
   bk(t, 25)
   a = atan(1.0 / 2) * 360.0 / (2 * pi)
   lt(t, a)
   Yl = sqrt(25 ** 2 + 50 ** 2)
   pd(t)
   fd(t, Yl)
   pu(t)
   rt(t, 2 * a)
   fd(t, Yl)
   pd(t)
   bk(t, 2 * Yl)

   # print u
   lt(t, a)
   u_arc(t, 100 / 3.0, 25)

   # print n
   pu(t)
   rt(t, 90)
   fd(t, 5)
   lt(t, 90)
   pd(t)
   n_arc(t, 100 / 3.0, 25)
 
   # print o
   fd(t, 25)
   rr = 50 / 2.5
   circle(t, rr)

   # print s
   c = 2 * pi * rr
   length = c / 4.0
   n = int(length / 3) + 1
   step_length = length / n
   step_angle = 90.0 / n
   for i in range(n):
      fd(t, step_length)
      lt(t, step_angle)
   fd(t, 50 / 3.0 + rr)
   s_arc(t, rr)

world = TurtleWorld()
Bob = Turtle()
Bob.delay = 0.01
drawEayun(Bob)
wait_for_user()
