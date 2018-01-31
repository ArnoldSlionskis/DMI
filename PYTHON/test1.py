from math import cos
from math import sqrt
#---------------------------------------------------------------
print " ---"
print "/        2k"
print "\       x"
print " >   --------"
print "/      (2k)!"
print "\ "
print " ---"
print " "
print "      2k+2"
print "     x"
print "---------------"
print " (2k+2)*(2k+4)"
#--------------------------------------------------------------
x = float(input("ievadiet x: "))
print type(x)

y=cos(x)
print "cos(%.2f) = %.2f"%(x,y)

c = 0
a = 1.
summa = a
while c < 500:
        c+=1
        k1 = 1.*(1/((2*c+2)*(2*c+4)))
        k2 = x**2
        k3 = k2*k1
        k4 = k3**(c+1)
        a = a * k4
        summa = summa + a
        if c == 499:
                print "summa(499) = %.2f"%(summa)
print "mans_cos(%.2f) = %.2f"%(x,y)
print "summa = %.2f"%(summa)
print "a = %.2f"%(a)
