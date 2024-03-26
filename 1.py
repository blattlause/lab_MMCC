import numpy as np
import matplotlib.pyplot as plt
import math as mt

f1 = mt.radians(50)
f2 = mt.radians(40)
f3 = mt.radians(30)
S1 = 0.57
S2 = 0.63
S3 = 0.68
a4 = 0.05
B = mt.radians(110)

#функция K
def K_calculate():
    #матрица коэффициентов
    A = np.array([[S1* np.cos(f1), np.sin(f1), -1], [S2* np.cos(f2), np.sin(f2), -1], [S3* np.cos(f3), np.sin(f3), -1]])
    #вектор свободных членов
    B = np.array([[S1**2], [S2**2], [S3**2]])
    #вектор решения
    X = np.linalg.solve(A, B)
    return X

K_values = K_calculate()

print("K:", K_values[0], K_values[1], K_values[2])

#длины звеньев
a1 = K_values[0]/2
a3 = K_values[1]/(2*a1)
a2 = np.sqrt(a1**2 + a3**2 -K_values[2])

print("Длины звеньев:", a1, a2, a3)

#проверить условие существования
if a1 < a2 - a3:
    if a3 > 0:
        H = 1
    else: H = -1

    #координаты
    xc = a1 * np.cos(f1) + np.sqrt(a2**2 - (a3*H - a1* np.sin(f1))**2)
    yc = a3*H

    xb = a1 * np.cos(f1)
    yb = a1 * np.sin(f1)

    f6 = f2 + B

    xn = a1 * np.cos(f1) + a4 * np.cos(f6)
    yn = a1 * np.sin(f1) + a4 * np.sin(f6)

    print("Координаты: ", xc, yc, xb, yb, xn, yn)
    f2 = np.arccos((xc - a1 * np.cos(f1)/a2))
    
    #ход ползуна
    S = a1 * np.cos(f1) + np.sqrt(a2**2 - (a3 * H - a1*np.sin(f1))**2)
    print("Функция: ", S)
    
    s_values = np.linspace(0, 6, 100)
    s_result = []

    dot = 0.7
    crossings = []
    
    for element in s_values:
        y = a1 * np.cos(element) + np.sqrt(a2**2 - (a3 * H - a1 * np.sin(element))**2)
        s_result.append(y)
        if abs(y - dot) < 0.015:
            crossings.append(element)

    plt.plot(np.array([xc, xb]), np.array([yc, yb]), color='black')  
    plt.plot(np.array([xn, xb]), np.array([yn, yb]), color='black') 
    plt.plot([0, xb[0]], [0, yb[0]], color='black')
    plt.show()

    plt.plot(s_values, s_result)
    
    for x in crossings:
        plt.plot(x, dot, 'ro')
    plt.show()
    
else: print("Механизм не существует")
