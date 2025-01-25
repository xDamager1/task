import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sin, cos, diff, lambdify
from scipy.integrate import quad

# Определение переменной и функции
x = symbols("x")
fx = cos(x) * sin(x**2 + 8)

# Вычисление первой и второй производной
fx1 = diff(fx, x)
fx2 = diff(fx1, x)

# Создание функций для численного вычисления
fx_func = lambdify(x, fx, 'numpy')
fx1_func = lambdify(x, fx1, 'numpy')
fx2_func = lambdify(x, fx2, 'numpy')

# Генерация значений для графиков
x_vals = np.linspace(0, 5, 100)
fx_vals = fx_func(x_vals)
fx1_vals = fx1_func(x_vals)
fx2_vals = fx2_func(x_vals)

# Построение графиков функции и ее производных
plt.figure(figsize=(12, 10))
plt.subplot(3, 1, 1)
plt.plot(x_vals, fx_vals, label='f(x) = cos(x) * sin(x^2 + 8)')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(x_vals, fx1_vals, label="f'(x)", color='orange')
plt.title('Первая производная')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(x_vals, fx2_vals, label="f''(x)", color='green')
plt.title('Вторая производная')
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Наибольшее и наименьшее значение функции
max_value = np.max(fx_vals)
min_value = np.min(fx_vals)
max_index = np.argmax(fx_vals)
min_index = np.argmin(fx_vals)

# Построение графика с максимумом и минимумом
plt.figure(figsize=(8, 6))
plt.plot(x_vals, fx_vals, label='f(x)')
plt.plot([x_vals[max_index]], [max_value], 'o', color='b', label='Максимум')
plt.plot([x_vals[min_index]], [min_value], 'o', color='r', label='Минимум')
plt.title('График функции с максимумом и минимумом')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

print(f"Наибольшее значение: {max_value} при x = {x_vals[max_index]}")
print(f"Наименьшее значение: {min_value} при x = {x_vals[min_index]}")

# Построение касательной и нормали
x0 = x_vals[max_index]
slope = fx1_func(x0)
tangent_eq = lambda x: slope * (x - x0) + max_value
normal_eq = lambda x: -1/slope * (x - x0) + max_value

plt.figure(figsize=(8, 6))
plt.plot(x_vals, fx_vals, label='f(x)')
plt.plot([x0], [max_value], 'o', color='b', label='Максимум')
plt.plot(x_vals, tangent_eq(x_vals), '--', color='orange', label='Касательная')
plt.plot(x_vals, normal_eq(x_vals), '--', color='green', label='Нормаль')
plt.title('Касательная и нормаль к функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

# Касательное расслоение 
plt.figure(figsize=(8, 6))
for xi in np.linspace(0, 5, 10):
    slope = fx1_func(xi)
    plt.plot(x_vals, fx_func(xi) + slope * (x_vals - xi), '--', color='gray', alpha=0.5)
plt.plot(x_vals, fx_vals, label='f(x)')
plt.title('Касательное расслоение')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

# Длина кривой через интеграл
dx = 0.01  # Шаг интегрирования
length_integral_func = lambda x: np.sqrt(1 + (fx1_func(x))**2)
length, _ = quad(length_integral_func, 0, 5)

print(f"Длина кривой: {length}")
