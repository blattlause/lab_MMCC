import numpy as np
import matplotlib.pyplot as plt

G = 0.015
r_values = [0.01, 0.0125, 0.015, 0.0175, 0.02]
h = 1.2
R_target = 12

def calculate_R(L, r):
    return (np.log((L**2)/(2*r*h)) + 4.95) / (2 * np.pi * L * G)

L_values = np.linspace(10, 15, 100) 

plt.figure(figsize=(10, 6))

for r in r_values:
    R_values = calculate_R(L_values, r)
    plt.plot(L_values, R_values, label=f'R(L) для r={r}')
    
plt.axhline(y=R_target, color='r', linestyle='--', label='Искомая R')

for r in r_values:
    R_values = calculate_R(L_values, r)
    index = np.argwhere(np.diff(np.sign(R_values - R_target))).flatten()
    if len(index) > 0:
        intersection_L = L_values[index[0]]
        intersection_R = R_values[index[0]]
        plt.plot(intersection_L, intersection_R, 'ro') 
        print(f"Пересечение найдено в точке L = {intersection_L:.2f} для r = {r}")
    else:
        print(f"Не найдено пересечения для r = {r}.")
        
plt.xlabel('Длина (L)') 
plt.ylabel('R')
plt.title('Функция R(L) для различных значений')
plt.legend()
plt.grid(True)
plt.show()
