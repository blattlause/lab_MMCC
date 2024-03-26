import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

AB = 0.98
OA = 0.82
AC = 0.52
Tk = 1.21
S0 = 1.15
Vb = 0.8
psy0 = 0.561
w = 2.2

t = np.linspace(0, Tk, 500)
S1 = S0 - Vb * t #ползунок
psy = psy0 + w * t # движение руки

f = np.arccos((-AB**2 + S1**2 + OA**2)/(2 * OA * S1))

XA = OA * np.cos(f)
YA = OA * np.sin(f)

XC = XA - AC * np.cos(f - psy)
YC = YA - AC * np.sin(f - psy)

threshold_value = 1.12 
index_threshold = np.where(YC >= threshold_value)[0][0]  

#время и координата X при пересечении порогового значения
time_threshold = t[index_threshold]
x_threshold = XC[index_threshold]

print("Время пересечения порогового значения координаты Y:", time_threshold)
print("Координата X при пересечении порогового значения координаты Y:", x_threshold)

fig = plt.figure(facecolor='white')
plt.xlim(-1.5, 1)
plt.ylim(0, 1.5)
plt.plot(XC, YC)

lin1, = plt.plot([ ], [ ])
lin2, = plt.plot([ ], [ ])
lin3, = plt.plot([ ], [ ])



def redraw(i):
    x = XC[i]
    y = YC[i]
    x1=XA[i]
    y1=YA[i]
    x2=S1[i]
    lin1.set_data([x,x1], [y,y1])
    lin2.set_data( [0, x1], [0, y1])
    lin3.set_data([x2, x1], [0, y1])
    return lin1,lin2,lin3

anim=animation.FuncAnimation(fig,redraw,
frames=200,interval=50)

plt.show()
