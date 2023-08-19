import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

#Вершины треугольника
A=[0,0]
B=[0.5,np.sqrt(3)/2]
C=[1,0]
ABC=[A,B,C]

#Случайная точка внутри треугольника
fx=np.random.randint(1,100)/100
if fx<=0.5:
    fy=np.random.randint(1,fx*np.tan(np.pi/3)*100)/100
else:
    fy=np.random.randint(1,(1-fx)*np.tan(np.pi/3)*100)/100
p=[[fx,fy]]

#Генерирую остальные точки согласно правилу: каждая точка располагается на середине
#отрезка, соединяющего любую имеющуюся точку с любой вершиной треугольника.

for _ in range(99):
    U=ABC[np.random.randint(0,len(ABC))]
    G=p[np.random.randint(0,len(p))]
    dx=np.absolute(U[0]-G[0])/2
    dy=np.absolute(U[1]-G[1])/2
    if U[0]>G[0]:
        nx=G[0]+dx
    else:
        nx=G[0]-dx
    if U[1]>G[1]:
        ny=G[1]+dy
    else:
        ny=G[1]-dy
    p.append([nx,ny])


plt.figure(figsize = (10,10))
plt.xlim(0,1)
plt.ylim(0,1)
for i in range(len(p)):
    plt.plot(p[i][0], p[i][1], 'bo')
plt.show()