from math import atan
from math import sqrt

x = float(input("enter argument x: "))
print type(x)

y=atan(x)
print "atan(%.2f) = %.2f"%(x,y)
#--------------------------------------------------------------
count = 0
sum = 0
while count <= 500:
	count2 = 1
	sum2 = 1
	c2 = 2*count
	while count2 < c2+1:
		sum2 = sum2 * count2
		count2+=1
	count3 = 1
	sum3 = 1
	c3 = count
	while count3 < c3+1:
		sum3 = sum3 * count3
		count3+=1
	a = (sum2/((sum3**2)*(2**(2*count))*((2*count)+1)))*(((x**2)/(1+(x**2)))**count)
	sum = sum + a
	count += 1
y=(x/(sqrt(1+(x**2))))*sum
print "atan(x) = %.2f"%(y)
