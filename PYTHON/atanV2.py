from math import atan
from math import sqrt

x = float(input("enter argument x: "))
print type(x)

y=atan(x)
print "atan(%.2f) = %.2f"%(x,y)
#--------------------------------------------------------------
count = 0
a = 1.
sum = a
while count < 500:
	count+=1
	k = 1.*((2*count-1)**2)/(2*count*(2*count+1))*(x**2)/(1+(x**2))
	a = a * k
	sum = sum + a
z = (x/(sqrt(1+(x**2))))
y = z * sum
print "my_atan(%.2f) = %.2f"%(x,y)
