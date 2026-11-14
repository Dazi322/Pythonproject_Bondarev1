import math

def TrianglePS(a):
    P = 3 * a
    S = (a ** 2) * math.sqrt(3) / 4
    return P, S

# Исходные стороны для трех треугольников
sides = [3, 5, 10]

# Вычисляем и выводим результат для каждого треугольника
for side in sides:
    perimeter, area = TrianglePS(side)
    print(f"Сторона: {side} -> Периметр P = {perimeter}, Площадь S = {area:.2f}")
