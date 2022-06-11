import math


def solve_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        return 'Уравнение не имеет решений'
    elif a == 0:
        return 'При a = 0, уравнение принимает линейный вид и имеет одно решение: ' + str(-c/b) if b != 0 else ''
    elif D < 0:
        return 'Уравнение не имеет корней'
    elif D == 0:
        return -b / (2 * a)
    elif D > 0:
        return (-b - math.sqrt(D)) / (2 * a), (-b + math.sqrt(D)) / (2 * a)

