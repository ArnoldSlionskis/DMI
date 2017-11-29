from math import sqrt, atan
import numpy as np
import matplotlib.pyplot as plt

def mans_atan (x,n):
        count = 0
        a = 1.
        sum = a
        while count < n:
                count+=1
                k = 1.*((2*count-1)**2)/(2*count*(2*count+1))*(x**2)/(1+(x**2))
                a = a * k
                sum = sum + a
                z = (x/(np.sqrt(1+(x**2))))
        y = z * sum
        return y

x = np.arange(0.0, 6.28, 0.01)
y = np.arctan(x)
yy = mans_atan(x,500)
plt.plot(x,y)
plt.plot(x,yy)
plt.show()
