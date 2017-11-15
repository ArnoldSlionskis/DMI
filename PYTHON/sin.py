# -*- coding: utf-8 -*-

from math import sin
from math import factorial

x = float(input("ievadiet argumentu x: "))
print type(x)

y = sin(x)
print "sin(%.2f) = %.2f"%(x,y)
#------------------------------------------
count = 0
sum = 0
while count <= 3:
	count2 = 1
	sum2 = 1
	c2 = 2*count+1
	while count2 <= c2:
		sum2 = sum2 * count2
		count2 += 1
	a = (-1)**count*x**c2/sum2
	sum = sum + a
	count += 1
print "sin = %.2f"%(sum)

