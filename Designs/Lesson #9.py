import sys

# Задача 1

lis = []
print("Количество чисел:")
while True:
    N = int(input())
    if 1 <= N <= 100000:
        break
    else:
        print("Напишите число 1 ≤ N ≤ 100000")

lis = list(map(abs, map(int, input("Введите список из {0} чисел до 2*10e9 по модулю, разделенных пробелом: ".format(N))
                        .split())))

while N != len(lis):
    if N < len(lis):
        difference = len(lis) - N
        delete = list(map(int, input("Чисел больше чем нужно на {0}, удалите числа:  ".format(difference)).split()))
        if len(delete) <= difference:
            for x in delete:
                if x in lis:
                    lis.remove(x)
                else:
                    print("Такого числа нет в списке.")
                    continue
    if N > len(lis):
        difference = N - len(lis)
        app = list(map(int, input("Чисел меньше чем нужно на {0}, допишите числа:  ".format(difference)).split()))
        if len(app) < difference:
            print("Количество чисел которое нужно добавить {0}".format(difference))
            lis = lis + app
            continue
        elif len(app) > difference:
            print("Чисел должно быть: {0} ".format(difference))
            continue
        lis = lis + app
i = 0
while i < len(lis)-1:
    if lis[i] <= (2*10e9):
        i += 1
        continue
    else:
        lis.append(int(input("Замените число {0} на число из диапазона до 2*10e9 по модулю ".format(lis[i]))))
        lis.pop(i)
        continue
print("Различных чисел: {0}".format(len(set(lis))))

# Задача 2

L1 = []
L2 = []
while True:
    L1 = list(map(int, input("Введите список из чисел до 100000, разделенных пробелом: ").split()))
    if len(L1) > 100000:
        print("Чисел должно быть 100000")
    else:
        break

while True:
    L2 = list(map(int, input("Введите второй список из чисел до 100000, разделенных пробелом: ").split()))
    if len(L2) > 100000:
        print("Чисел должно быть 100000")
    else:
        break

ML1 = set(L1)
ML2 = set(L2)

print("Чисел содержится одновременно как в первом списке, так и во втором = {0}".format(len(ML2)+len(ML1) - len(ML2.union(ML1))))


# Задача 3

lst = list(map(int, input("Введите список из чисел через пробел: ").split()))

lst.sort()
j = 0
while j < len(lst):
    if lst[j - 1] == lst[j] and j > 0:
        print("YES = {0}".format(lst[j]))
    else:
        print("NO = {0}".format(lst[j]))
    j += 1
print(sys.stdin.readline())