import math

# Кубическая функция
def f(x):
    return x**3 - 2*x - 5

# Метод хорд
a = 2.0    # левая граница
b = 3.0    # правая граница
eps = 0.01 # точность (погрешность)

while True:

    c = (a*f(b) - b*f(a)) / (f(b) - f(a))


    error = abs(c - a) if f(a)*f(c) < 0 else abs(b - c)

    # Условие выхода
    if abs(f(c)) < eps or error < eps:
        print(f"x = {c:.6f} ± {error:.6f}")
        break

    # Обновляем границы
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
