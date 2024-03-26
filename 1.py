import numpy as np
from numpy.linalg import inv

# Число факторов
num_factors = 3
levels_per_factor = 2

# Матрица планирования
num_experiments = levels_per_factor ** num_factors
planning_matrix = np.zeros((num_experiments, num_factors), dtype=int)

for i in range(num_experiments):
    for j in range(num_factors):
        planning_matrix[i][j] = ((i // (levels_per_factor ** j)) % levels_per_factor) * 2 - 1


# Функция отклика
response_function = np.array([
    3.651, 3.605, 3.653, 3.592, 3.627,
    6.547, 6.514, 6.535, 6.562, 6.581,
    4.761, 4.793, 4.816, 4.792, 4.801,
    9.515, 9.566, 9.534, 9.552, 9.528,
    5.828, 5.847, 5.842, 5.905, 5.886,
    13.041, 13.081, 13.051, 13.089, 13.063,
    8.364, 8.371, 8.338, 8.365, 8.366,
    25.575, 25.563, 25.611, 25.578, 25.534
])

# Среднее значение функции отклика для пяти повторов опытов
average_response = np.mean(response_function.reshape(-1, 5), axis=1)

# Матрица планирования без учета взаимодействия факторов
X_matrix = np.column_stack((np.ones(len(planning_matrix)), planning_matrix))

# Вычисление коэффициентов регрессии
coefficients = inv(X_matrix.T @ X_matrix) @ X_matrix.T @ average_response

# Значения факторов для расчета вектора Q 
# np.ones создает массив из единиц длиной, равной количеству строк в planning_matrix. Этот массив представляет собой столбец, состоящий из единиц.
X_values = np.column_stack((np.ones(len(planning_matrix)), planning_matrix)) #np.column_stack(), которая объединяет массив из единиц (первый столбец) с planning_matrix (остальные столбцы).

# Расчет вектора Q по регрессионной модели
Q_vector = X_values @ coefficients

# Расчет абсолютной ошибки модели
W = np.max(np.abs(average_response - Q_vector))

# Расчет относительной ошибки модели в процентах
w = (W / np.max(np.abs(average_response))) * 100

print("Матрица ПФЭ:\n", planning_matrix)
print("\nСреднее значение функции отклика для пяти повторов опытов:")
print(average_response)

print("\nКоэффициенты регрессии:")
print("b0 =", coefficients[0])
print("b1 =", coefficients[1])
print("b2 =", coefficients[2])
print("b3 =", coefficients[3])

print("\nВектор Q по регрессионной модели:", Q_vector)

print("\nАбсолютная ошибка модели (W):", W)
print("Относительная ошибка модели в процентах (w):", w)

# Добавление столбцов для взаимодействия всех трех факторов
interaction_columns_extended = np.column_stack((
    planning_matrix[:, 0] * planning_matrix[:, 1],
    planning_matrix[:, 0] * planning_matrix[:, 2],
    planning_matrix[:, 1] * planning_matrix[:, 2],
    planning_matrix[:, 0] * planning_matrix[:, 1] * planning_matrix[:, 2]
))

# Расширенная матрица планирования с учетом взаимодействия всех трех факторов
extended_X_matrix_extended = np.column_stack((X_matrix, interaction_columns_extended))

# Вычисление коэффициентов расширенной регрессионной модели
extended_coefficients_extended = inv(extended_X_matrix_extended.T @ extended_X_matrix_extended) @ extended_X_matrix_extended.T @ average_response

# Вывод коэффициентов расширенной регрессионной модели с учетом взаимодействия всех трех факторов
print("\nКоэффициенты расширенной регрессионной модели (с учетом взаимодействия всех трех факторов):")
print("b0 =", extended_coefficients_extended[0])
print("b1 =", extended_coefficients_extended[1])
print("b2 =", extended_coefficients_extended[2])
print("b3 =", extended_coefficients_extended[3])
print("b4 =", extended_coefficients_extended[4])
print("b5 =", extended_coefficients_extended[5])
print("b6 =", extended_coefficients_extended[6])
print("b7 =", extended_coefficients_extended[7])

# Значения факторов для расчета расширенного вектора Q с учетом взаимодействия всех трех факторов
extended_X_values_extended = np.column_stack((np.ones(len(planning_matrix)), planning_matrix, interaction_columns_extended))

# Расчет расширенного вектора Q по расширенной регрессионной модели с учетом взаимодействия всех трех факторов
extended_Q_vector_extended = extended_X_values_extended @ extended_coefficients_extended

print("\nСреднее значение функции отклика для пяти повторов опытов:\n", average_response)

# Вывод расчетных значений функции отклика по расширенной регрессионной модели с учетом взаимодействия всех трех факторов
print("\nРасчетные значения функции отклика по расширенной регрессионной модели (с учетом взаимодействия всех трех факторов)\n:", extended_Q_vector_extended)

# Расчет абсолютной ошибки модели с учетом взаимодействия всех трех факторов
extended_W_extended = np.max(np.abs(average_response - extended_Q_vector_extended))

# Расчет относительной ошибки модели в процентах с учетом взаимодействия всех трех факторов
extended_w_extended = (extended_W_extended / np.max(np.abs(average_response))) * 100

# Вывод результатов с учетом взаимодействия всех трех факторов
print("\nАбсолютная ошибка модели (расширенная, с учетом взаимодействия всех трех факторов):", extended_W_extended)
print("Относительная ошибка модели в процентах (расширенная, с учетом взаимодействия всех трех факторов):", extended_w_extended)
