# -*- coding: utf-8 -*-
"""
Particle Swarm Optimization

"""

import numpy as np

def f(x):
      x = np.array(x)
      L = 1
      K = 1e3
      p = np.array([[2,0],[5,1.5],[2.5,3],[0,2],[0,1]])
      
      U = 0
      for coor in p:
            l = np.linalg.norm(x-coor)
            U += K*(l-L)**2/2
      
      return U



n = 20
vmax = 10
xmin = np.array([0,0])
xmax = np.array([5,3])
d = xmin.shape[0]

x = (xmax-xmin)*np.random.rand(n,d) + xmin
v = (vmax/3+vmax/3)*np.random.rand(n,d) - vmax/3

pb = np.zeros([n,d])

for i,pos in enumerate(x):
      pb[i] = pos
      if i == 0:
            gb = pb[i]
      
      if f(pb[i]) < f(gb):
            gb = pb[i]


iters = 0;
C1 = 0.72984*2.05
C2 = 0.72984*2.05
while 1:
      iters += 1
      
      for i in range(n):
            if f(x[i]) < f(pb[i]):
                  pb[i] = x[i]
            elif f(pb[i]) < f(gb):
                  gb = pb[i]
            
      for i in range(n):
            for j in range(d):
                  v[i,j] = v[i,j] + C1*np.random.rand()*(pb[i,j] - x[i,j]) + \
                  C2*np.random.rand()*(gb[j]-x[i,j])
                  
                  x[i,j] = x[i,j] + v[i,j]
                  if x[i,j] > xmax[j]:
                        x[i,j] = xmax[j]
                  elif x[i,j] < xmin[j]:
                        x[i,j] = xmin[j]
                        
      if iters == 1000:
            break


print(gb)    