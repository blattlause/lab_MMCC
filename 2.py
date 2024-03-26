import numpy as np
import matplotlib.pyplot as plt

f1 = 1.7
f2 = 3.2
f3 = 5.3
a1 = 0.86
a2 = 0.58
w0 = 1.256
v = 0.675

b1 = 2 * np.pi / f1
b2 = 2 * np.pi / (f3 - f2)
t1 = 2 * np.pi / (b1 * w0)
t2 = f2 / w0
t3 = t2 + 2 * np.pi / (b2 * w0)
t = np.arange(0, 2 * np.pi / w0, 0.01)

#Функция аналога ускорения роликового толкателя 
def S11(t):
    if 0 <= t < t1:
        return a1 * np.sin(b1 * w0 * t)
    elif t1 <= t < t2:
        return 0
    elif t2 <= t < t3:
        return a2 * np.sin(b2 * w0 * t)
    else:
        return 0
    
#Функция скорости  роликового толкателя 
def S1(t):
    return w0**2 * t

def R1(s1):
    return s1 / np.tan(v)

#Вычисление радиуса-вектора центрового профиля кулачкового механизма
def R(s):
    return R0 + s

#Центровой профиль кулачка
def XY():
    X = []
    Y = []
    i = 0
    for j in t:
        X.append((R0 + s_s1_s11[0][i]) * np.sin(w0 * j))
        Y.append((R0 + s_s1_s11[0][i]) * np.cos(w0 * j))
        i += 1
    return X, Y

#Вычисление функций
def S_S1_S11():
    s11 = []
    s1 = []
    s = []
    time = []
    for i in t:
        time.append(i)
        s11.append(S11(i))
        s1.append(np.trapz(list(map(S1, s11)), time))
        s.append(np.trapz(s1, time))
    return s, s1, s11


def graphic(x, y):
    plt.plot(x, y)
    plt.grid()
    plt.show()
#за счет чего происходит накопление значений площедей интеграла когда используем map

s_s1_s11 = S_S1_S11()

R0 = min(list(map(R1, s_s1_s11[1])))

xy = XY()
#Траектория движения толкателя
graphic(xy[0], xy[1])
#График перемещения
graphic(t, s_s1_s11[0])
#График скорости
graphic(t, s_s1_s11[1])
#График ускорения
graphic(t, s_s1_s11[2])
