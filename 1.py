from scipy.integrate import *
import matplotlib.pyplot as plt
import numpy as np
#m – масса груза
#l – длина стержня
#D – диаметр пружины
#d – диаметр проволоки пружины
#G – модуль упругости материала пружины
#i – число витков пружины
#α – коэффициент вязкого сопротивления.

#угловое в радианах перемещение

#добавить возмущающую силу в диффур

l = 0.3
D = 0.0020
d = 0.0002
i = 6
m = 40
alpha = 75
phi_0 = 0.05
tk = 1

F0 = 10
G= 80
w = 10
#m = [5, 8, 10, 12, 16, 19, 22, 25, 28]

n = alpha/(2*m*l)
c = (G*d**4)/(8*D**3*i)
p = np.sqrt((c*l + m*G)/(2*m*l))


def func(y,t):
    return[y[1],-n*y[1]-p**2*y[0]]

t = np.linspace(0, 3, 1000)
y_0=[phi_0,0]
Y= odeint(func, y_0, t)

# График углового смещения от времени
plt.figure(1)
plt.plot(t,Y[:,0])
plt.grid();
plt.figure(2)

# График скорости от времени
plt.plot(t,Y[:,1])
plt.grid();
plt.show()
