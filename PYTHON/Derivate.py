from math import sqrt, atan
import numpy as np
import matplotlib.pyplot as plt

def mans_atan (x):
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
        return y

a = -3.
b = 3.
x = np.arange(a,b,0.5)
y = mans_atan(x)
plt.plot(x,y)
plt.grid()
#plt.show()

n = len(x)
y_prim = []
for i in range (n-1):
        print i, x[i], y[i]
        delta_y = y[i+1]-y[i]
        delta_x = x[i+1]-x[i]
        #y_prim = delta_y/delta_x
        #print y_prim
        y_prim.append(delta_y/delta_x)

plt.plot(x[:n-1],y_prim)
plt.show()

