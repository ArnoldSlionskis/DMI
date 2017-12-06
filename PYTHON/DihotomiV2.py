from math import sqrt, atan
import numpy as np
import matplotlib.pyplot as plt

def mans_atan (x,tar):
        count = 0
        a = 1.
        sum = a
        while count < 500:
                count+=1
                k = 1.*((2*count-1)**2)/(2*count*(2*count+1))*(x**2)/(1+(x**2))
                a = a * k
                sum = sum + a
                z = (x/(np.sqrt(1+(x**2))))
        y = z * sum
        return y - tar
tar = input("What number are you looking for?")
tar = 1. * tar
print tar

a = -3.
b = 3.
x = np.arange(a,b,0.01)
y = mans_atan(x, 0)
plt.plot(x,y)
plt.grid()
plt.show()

delta_x = 1.e-3 # =0,001
funa = mans_atan (a, tar)
funb = mans_atan (b, tar)
if funa * funb > 0:
        print "[%.2f,%.2f] intervala saknu nav"%(a,b)
        print "vai saja intervala ir paru saknu skaits"
        exit()
print "turpinajums, kad sakne ir:"
print "vertibas intervala galapunktos - ",
print "f(%.2f)=%.2f un f(%.2f)=%.2f"%(a,funa,b,funb)

k=0
while b-a > delta_x:
        k = k + 1
        x = (a+b)/2
        funx = mans_atan(x, tar)
        print "%3d. a=%.5f f(%.5f)=%8.5f b=%.5f"%(k,a,x,funx,b)
        if funa * funx > 0:
                a = x
        else:
                b = x
print "rezultats: "
print "a=%.9f f(%.9f)=%8.9f b=%.9f"%(a,x,funx,b)
print "apreikins veikts ar %d iteraciju"%(k)
