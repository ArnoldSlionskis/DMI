from math import sin
from math import factorial

x = float(input("ievadiet argumentu x: "))
print type(x)

y = sin(x)
print "sin(%.2f) = %.2f"%(x,y)
#------------------------------------------

count = 0
a = (-1)**0*x**1/(1)
sum = a
while count < 3:
	count+=1
	a = a * (-1)*(x**2)/((count*2)*(count*2+1))
	sum = sum + a
print"sin(%.2f) = %.2f"%(x,sum)
