import math

from math import e

from math import sqrt

eps = 0.5 * math.pow(10, -5)


def f(x):
    return math.pow(e, -x) - 1.7 + x * x


def f1(x):
    return - math.pow(e, -x) + 2 * x  # первая производная


def f2(x):
    return math.pow(e, -x) + 2  # вторая производная


def find_x0():
    fx = pow(e, -1.5) - 1.7 + pow(1.5, 2)
    f2x = pow(e, -1.5) + 2

    print('\nНайдем произведение f(x) и f\'\'(x): {}'.format(fx*f2x) + "\n")


def one():
    print('\nМетод половинного деления:\n')

    a = 1.0
    b = 1.5

    def x_n(a, b):
        return (a + b) / 2

    count = math.floor(math.log2((b - a) / eps))

    for i in range(count + 1):
        x = x_n(a, b)
        if f(a) * f(x) < 0:
            b = x
        if f(x) * f(b) < 0:
            a = x

    print('\tРезультат: {}'.format(x_n(a, b)))
    print('\tКол-во итераций: {}'.format(count))


def two():
    print('\nМетод неподвижных хорд:\n')

    a = 1.0
    b = 1.5

    def x_n(x, x_0):
        return x - f(x) / (f(x) - f(x_0)) * (x - x_0)

    # начинается с х2
    x = a

    m = f1(a)
    count = 1
    while abs(f(x)) >= eps * m:
        count += 1
        x = x_n(x, b)

    print('\tРезультат: {}'.format(x))
    print('\tКол-во итераций: {}'.format(count))


def three():
    print('\nМетод подвижных хорд:\n')

    a = 1.0
    b = 1.5

    def x_n(x, x_prev):
        return x - f(x) / (f(x) - f(x_prev)) * (x - x_prev)

    # начинается с х2
    x = x_n(a, b)
    x_prev = b

    m = f1(a)
    count = 2
    while abs(f(x)) >= eps * m:
        count += 1
        x1 = x
        x = x_n(x, x_prev)
        x_prev = x1

    print('\tРезультат: {}'.format(x))
    print('\tКол-во итераций: {}'.format(count))


def four():
    print('\nМетод Ньютона:\n')

    a = 1.0
    b = 1.5

    def x_n(x):
        df = f1(x)
        return x - f(x) / df

    M = abs(f2(a))
    m = abs(f1(a))

    # начинается с х2
    x = a
    xn = b

    count = 0
    while abs(x - xn) > eps:
        count += 1
        xn = x
        x = x_n(x)

    print('\tРезультат: {}'.format(x))
    print('\tКол-во итераций: {}'.format(count))


def five():
    print('\nМетод Ньютона 2:\n')

    a = 1.0
    b = 1.5
    M = abs(f2(a))

    def x_n(x):
        df1 = f1(x)
        delta_x = (-df1 + sqrt(pow(df1, 2) + 2 * M * f(x))) / -M
        return x + delta_x

    # начинается с х2
    x = b
    xn = a
    count = 0
    while abs(x - xn) >= eps:
        xn = x
        x = x_n(x)
        count += 1

    print('\tРезультат: {}'.format(x))
    print('\tКол-во итераций: {}'.format(count))


def six():
    print('\nМетод простой итерации:\n')

    a = 1.0
    b = 1.5
    x = a
    count = 0

    def x_n(x):
        return sqrt(-pow(e, -x) + 1.7)

    while True:
        count += 1
        new_x_n = x_n(x)
        if abs(new_x_n - x) <= eps:
            print('\tРезультат: {}'.format(x))
            print('\tКол-во итераций: {}'.format(count))
            break
        x = new_x_n


find_x0()
one()
two()
three()
four()
five()
six()
