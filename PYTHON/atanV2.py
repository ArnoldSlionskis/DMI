from math import atan
from math import sqrt

x = float(input("enter argument x: "))
print type(x)

y=atan(x)
print "atan(%.2f) = %.2f"%(x,y)
#--------------------------------------------------------------
print "          500"
print "          ---                               K"
print "         /                        /    2   \ "
print "  X      |          (2*K)!        |   x    | "
print "------- * >  ------------------ * |--------| "
print "   ----  |       2   2K           |     2  | "
print "  /   2  \   (K!) * 2  *(2*K+1)   \  1+X   / "
print " \/1+X    ---"
print "      "
print "      "
print "        2        2 "
print "  (2K-1)        x  "
print "----------- * ----- "
print " 2K*(2K+1)       2"
print "              1+x "
#--------------------------------------------------------------
count = 0
a = 1.
sum = a
while count < 500:
	count+=1
	k = 1.*((2*count-1)**2)/(2*count*(2*count+1))*(x**2)/(1+(x**2))
	a = a * k
	sum = sum + a
	if count == 499:
		print "sum(499) = %.2f"%(sum)
z = (x/(sqrt(1+(x**2))))
y = z * sum
print "my_atan(%.2f) = %.2f"%(x,y)
print "sum = %.2f"%(sum)
print "a = %.2f"%(a)
