# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:43:56 2026

@author: X
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1.0
b = 2.0
k = 100

dt = 0.01
t = np.arange(0, 10, dt)

x = np.zeros(len(t))
v = np.zeros(len(t))

x[0] = 0
v[0] = 0

for i in range(len(t)-1):
    
    f = 10  # external force
    
    a = (f - b*v[i] - k*x[i]) / m
    
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i]*dt

plt.plot(t, x)
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Mass-Spring-Damper with Force")
plt.grid()
plt.show()


