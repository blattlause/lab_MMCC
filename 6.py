from scipy.optimize import minimize_scalar
import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt

# Заданные параметры
l = 0.3
D = 0.0020
d = 0.0002
i = 6
alpha = 75
phi_0 = 0.05

F0 = 10
G = 80
w = 10

# Массив масс
m_values = [8, 10, 12, 16, 19, 22, 25, 28, 30]
minima = []

# Функция для решения дифференциального уравнения
def func(y, t, m):
    n = alpha / (2 * m * l)
    c = (G * d**4) / (8 * D**3 * i)
    p = np.sqrt((c * l + m * G) / (2 * m * l))
    return [y[1], -n * y[1] - p**2 * y[0]]

t = np.linspace(0, 3, 1000)

# Расчет минимума для каждой массы
for m in m_values:
    y_0 = [phi_0, 0]
    Y = odeint(func, y_0, t, args=(m,))
    minima.append(min(Y[:, 0]))

# Аппроксимация кривой
degree = 3  # Степень полинома для аппроксимации

# Построение полиномиальной аппроксимации
coefficients = np.polyfit(m_values, minima, degree)
polynomial = np.poly1d(coefficients)

m_values_smooth = np.linspace(min(m_values), max(m_values), 100)
minima_smooth = polynomial(m_values_smooth)

# Построение графика минимумов и аппроксимационной кривой
plt.figure(figsize=(10, 6))
plt.plot(m_values, minima, marker='o', linestyle='None', label='Исходные данные')
plt.plot(m_values_smooth, minima_smooth, label='Аппроксимация', color='red')
plt.title('Минимумы углового смещения для разных масс')
plt.xlabel('Масса')
plt.ylabel('Минимум')
plt.legend()
plt.grid(True)
plt.show()
