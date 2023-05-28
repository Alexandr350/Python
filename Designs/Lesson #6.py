import sys
import decimal
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

print("Введите число")
X = decimal.Decimal(int(input()))
coun = decimal.Decimal(0)
index = decimal.Decimal(1)
while index != X:
    if X % index == 0:
        coun += decimal.Decimal(1)
    index += decimal.Decimal(1)
print("Количество натуральных делителей = {0}".format(coun))


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