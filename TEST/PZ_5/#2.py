# Описать функцию TrianglePS(параметры), вычисляющую по стороне a
# равностороннего треугольника его периметр P = 3*a и площадь S = a2 √3/4. С
# помощью этой функции найти периметры и площади трех равносторонних
# треугольников с данными сторонами.


import math

def TrianglePS(a):
    P = 3 * a
    S = (a ** 2) * math.sqrt(3) / 4
    return P, S

sides = [3, 5, 10]

for side in sides:
    perimeter, area = TrianglePS(side)
    print(f"Сторона: {side} - Периметр P = {perimeter}, Площадь S = {area:.2f}")
