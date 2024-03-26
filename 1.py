import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
y1 = np.array([-1.761, -2.039, -1.492, -0.255, 1.31, 2.743, 3.642, 3.804])
y2 = np.array([-2.725, -2.588, -2.345, -1.963, -1.409, -0.647, 0.358, 1.644])
XF = 1.1

def func1(x, A, B, C):
    return A * np.sqrt(x**3) + B * np.sin(6*x + 3.5) + C*(x**2)

def func2(x, P, Q, H):    
    return P*x**3 + Q*np.sqrt(x**3) + H*np.cos(x/2)

#от 0.1 до 0.8, потом расширяем до 1.1
popt1, _ = curve_fit(func1, x, y1)
popt2, _ = curve_fit(func2, x, y2)

print("Oптимальные параметры для функции:")
print(popt1)
print(popt2)

#создать новый массив
X_fit = np.linspace(0.1, XF, 100)
y1_new = func1(X_fit, *popt1)
y2_new = func2(X_fit, *popt2)

#точка
idx = np.argwhere(np.diff(np.sign(y1_new - y2_new))).flatten()
x_cross, y_cross = X_fit[idx], y1_new[idx]

def integrand1(x):
    return np.sqrt(1 + (func1(x, *popt1))**2)

def integrand2(x):
    return np.sqrt(1 + (func2(x, *popt2))**2)

#длина кривых
length1, _ = quad(integrand1, 0.1, XF)
length2, _ = quad(integrand2, 0.1, XF)

print("Длина кривой для функции 1:", length1)
print("Длина кривой для функции 2:", length2)

plt.plot(x, y1, 'ro', label='Robot 1 Points')
plt.plot(x, y2, 'bo', label='Robot 2 Points')
plt.plot(X_fit, func1(X_fit, *popt1), 'r-', label='Robot 1 Fit')
plt.plot(X_fit, func2(X_fit, *popt2), 'b-', label='Robot 2 Fit')
plt.plot(x_cross, y_cross, 'go')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()


