import random
import numpy as np

def ranges(b_r,b_local,x_local):
    for i in range(len(x_local)):
        for j in range(len(b_r)-1):
            if x_local[i] > b_r[j] and x_local[i] < b_r[j+1]:
                b_local[j] = b_local[j] + 1
                #print x_local[i]
                #print b_local
        if x_local[i] > b_r[j+1]:
            b_local[j+1] = b_local[j+1] + 1
    return b_local

N = 100000
x = []
a = 0
b = np.pi
delta = 0.5
for i in range(N):
    x.append(random.uniform(a,b))
    #x.append(random.triangular(a,b))
    #print x

bars_ranges = np.arange(a,b,delta)
bars = np.zeros(len(bars_ranges))
print bars
bars = ranges(bars_ranges,bars,x)
print bars
s = 0
for z in range(len(bars)):
    s = s + bars[z]
print s
