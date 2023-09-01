
# Задача 1

N = 0
while True:
    N = int(input("Напишите количество повторений 1 ≤ N ≤ 10000: "))
    if 1 <= N <= 10000:
        break
    else:
        print("Необходимо ввести число в диапазоне 1 ≤ N ≤ 10000 ")
S = []


for i in range(N):
    while True:
        a = int(input("Напишите числа: "))
        if abs(a) <= 10e5:
            S.append(a)
            break
        else:
            print("Напишите число по модулю не превышающее 10e5")


S.reverse()
for i in S:
    print(i)


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

massaOneBoat = 0
print("Грузоподъемность лодки:")
while True:
    massaOneBoat = int(input())
    if 1 <= massaOneBoat <= 10e6:
        break
    else:
        print("Напишите число 1 ≤ m ≤ 10e6")

print("Число рыбаков:")
while True:
    fisherman = int(input())
    if 1 <= fisherman <= 100:
        break
    else:
        print("Напишите число 1 ≤ n ≤ 100")


weightAllFisherman = []
Ai = 0
i = 1
while i < fisherman + 1:
    Ai = int(input("Вес рыбака №{0}: ".format(i)))
    if 1 <= Ai <= massaOneBoat:
        weightAllFisherman.append(Ai)
    else:
        print("Вес рыбака должен быть 1 ≤ Ai ≤ m ")
        i -= 1
    i += 1

boats = []
z = 1
weightAllFisherman.sort()
weightAllFisherman.reverse()

while True:
    while z < len(weightAllFisherman):
        if len(weightAllFisherman) == 1:
            boats.append(weightAllFisherman[0])
            weightAllFisherman.pop(0)
            break
        weightTwoFisherman = weightAllFisherman[0] + weightAllFisherman[z]
        if weightTwoFisherman <= massaOneBoat:
            boats.append(weightTwoFisherman)
            weightAllFisherman.pop(z)
            weightAllFisherman.pop(0)
            break
        elif z == len(weightAllFisherman) - 1:
            boats.append(weightAllFisherman[0])
            weightAllFisherman.pop(0)
            break
        z += 1

    if len(weightAllFisherman) == 0:
        break

    if len(weightAllFisherman) == 1:
        z = 0
    else:
        z = 1
print("\nНеобходимо лодок: {0}".format(len(boats)))


