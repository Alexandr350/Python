import sys
from collections import Counter

# Задача 1

print("Количество повторений")
N = int(input())
counter = 0

while N > 0:
    print("Введите число")
    A = int(input())
    if A == 0:
        counter += 1
    N -= 1
print("\n")
print(counter)


# Задача 2

def change(t):
    tmp_change = t
    return tmp_change


X = int(input("Введите число: "))
div = []
i = 2
while i <= 2000000000:
    if X % i == 0:
        X = int(change(X/i))
        div.append(i)
        i = int(change(2))
    if X % i != 0:
        i += 1
    if X == 1:
        break

count = Counter(div)
dict(count)

tmp = []
for i in count.values():
    i_tmp = i + 1
    tmp.append(i_tmp)

result = 1
for i in tmp:
    result *= i
print("Количество натуральных делителей = {0}".format(result))


# Задача 3

print("Введите число А")
A = int(input())
print("Введите число B которое А < В")
B = int(input())
if A > B:
    print("Некорректный ввод")
else:
    st = ""
    while B >= A:
        if B % 2 == 0:
            st += (str(B) + " ")
        B -= 1
    print(st)


print(sys.stdin.readline())