import sys

# Задача 1

print("Количество чисел:")
while True:
    N = int(input())
    if 1 <= N <= 100000:
        break
    else:
        print("Напишите число 1 ≤ N ≤ 100000")

while True:
    lis = list(map(int, input("Введите список из {0} чисел до 2*10e9 по модулю, разделенных пробелом: ".format(N)).split()))
    if len(lis) > N:
        print("Чисел должно быть {0}".format(N))
    else:
        break

LS = len(lis)

index = 0
while True:
    if lis[index] < 0 or lis[index] > (2*10e9):
        print("Замените число {0}, число должно быть до 2*10e9 по модулю".format(lis[index]))
        i2 = int(input("Введите корректное число: "))
        if 0 <= i2 <= (2*10e9):
            lis.pop(index)
            lis.insert(index, i2)
    else:
        index += 1
        if index == N:
            break

LS = len(lis)
MN = set(lis)
print("Различных чисел: {0}".format(len(MN)))

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


YES = []
for j in range(len(lst)):
    for i in range(j + 1, len(lst)):
        if lst[i] == lst[j]:
            print("YES = {0}".format(lst[j]))
            YES.append(lst[j])

mLst = list(set(lst))
NO = list(set(YES) ^ set(mLst))
for k in NO:
    print("NO = {0}".format(k))

print(sys.stdin.readline())