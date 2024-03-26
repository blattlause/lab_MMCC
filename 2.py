import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Часть 2
# Данные, предоставленные в задании
X = np.array([18.99, 1.92, 15.60, 19.01, 6.44, 14.181, 18.23, 19.18, 20.07, 9.68, 7.78, 9.40, 0.01, 17.01, 1.97, 15.04, 3.38, 1.06, 0.40])
Y = np.array([9.71, 2.61, 4.12, 12.58, 5.56, 3.48, 3.474, 14.56, 0.34, 2.27, 0.13, 9.65, 6.21, 1.36, 10.48, 9.86, 8.03, 0.80, 3.89])

# Вычисляем среднее значение X и 
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Вычисляем отклонения от среднего значения
dev_X = X - mean_X
dev_Y = Y - mean_Y

# Вычисляем коэффициент корреляции
R = np.sum(dev_X * dev_Y) / np.sqrt(np.sum(dev_X**2) * np.sum(dev_Y**2))

print(f"Коэффициент корреляции R равен {R}")

# Интерпретируем корреляцию
if R <= 0.3:
    print("Корреляция слабая.")
elif R <= 0.5:
    print("Корреляция умеренная.")
elif R <= 0.7:
    print("Корреляция существенная.")
elif R <= 0.9:
    print("Корреляция сильная.")
else:
    print("Корреляция очень сильная.")

# Диаграмма рассеивания
plt.scatter(X, Y)
plt.title('Диаграмма рассеивания X и Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
