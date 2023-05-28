import sys

# Задача 1
'''
print("Напишите количество повторений")
N = int(input())
S = []
print("Напишите числа")
for i in range(N):
    while True:
        a = int(input())
        if 1 <= a <= 10000:
            S.append(a)
            break
        else:
            print("Напишите число 1 <= N <= 10000")

S.reverse()
for i in S:
    print(i)

'''
# Задача 2

print("Напишите количество повторений 1 ≤ N ≤ 100 000")
N1 = 0
lis = []
while True:
    N1 += int(input())
    if 1 <= N1 <= 100000:
        break
    else:
        print("Напишите число 1 ≤ N ≤ 100 000")
        N1 = 0

while True:
    lis = list(map(int, input("Введите список из {0} чисел из 1 ≤ Ai ≤ 10e9, разделенных пробелом: ".format(N1)).split()))
    if len(lis) > N1:
        print("Чисел должно быть {0}".format(N1))
    else:
        break

index = 0
while True:
    if lis[index] < 1 or lis[index] > 10e9:
        print("Замените число {0}, число должно быть 1 ≤ Ai ≤ 10e9".format(lis[index]))
        i2 = int(input("Введите корректное число: "))
        if 1 <= i2 <= 10e9:
            lis.pop(index)
            lis.insert(index, i2)

    else:
        index += 1
        if index == N1:
            break


def cycle(ls):
    ls.insert(0, ls.pop())
    return ls


L = list(cycle(lis))
print(*L)


# Задача 3
'''
print("Грузоподъемность лодки:")
while True:
    m = int(input())
    if 1 <= m <= 100000:
        break
    else:
        print("Напишите число 1 ≤ m ≤ 10e6")

print("Число рыбаков:")
while True:
    n = int(input())
    if 1 <= n <= 100:
        break
    else:
        print("Напишите число 1 ≤ n ≤ 100")

fisherman = 1
weight = 0
for j in range(n):
    print("Вес рыбака №{0}:".format(fisherman))
    weight += int(input())
    fisherman += 1

numberOfBoats = 0
if weight % 100 != 0:
    numberOfBoats += int(weight/100)
    print("Необходимо {0} лодки".format(numberOfBoats + 1))
else:
    print("Необходимо {0} лодки".format(numberOfBoats))
'''
print(sys.stdin.readline())
