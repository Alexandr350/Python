import sys

# Задача 1

A = int(input('Напишите число: '))
ls = []


def factorial(number):
    fac = 1
    for i in range(1, number+1):
        fac *= i
    fac2 = 1
    for j in range(1, fac+1):
        fac2 *= j
        ls.append(fac2)
    return fac2


factorial(A)
print(*ls)

print(sys.stdin.readline())