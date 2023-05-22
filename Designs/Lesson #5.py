import sys
import re

# Задача 1

print("Введите число")
number = int(input())
if number > 0:
    str1 = "положительное"
elif number == 0:
    str1 = "нулевое"
elif number < 0:
    str1 = "отрицательное"


if number == 0:
    str2 = ""
elif number % 2 == 0:
    str2 = "четное"
else:
    str2 = "нечетное"
print("{0} {1} число.".format(str1, str2))

# Задача 2

print("Напишите текст на английском")
slovo = input().lower().replace(' ', '')
slovo = re.sub(r'[^\w\s]', '', slovo)
slovo = re.sub(r'[\d+]', '', slovo)
indexA = 0
indexI = 0
indexY = 0
indexO = 0
indexE = 0
indexU = 0
indexOfVowels = 0
indexOfConsonants = 0
const = len(slovo)
for ABC in slovo:
    if ABC == 'a':
        indexOfVowels += 1
        indexA += 1
    elif ABC == 'e':
        indexOfVowels += 1
        indexE += 1
    elif ABC == 'y':
        indexOfVowels += 1
        indexY += 1
    elif ABC == 'o':
        indexOfVowels += 1
        indexO += 1
    elif ABC == 'u':
        indexOfVowels += 1
        indexU += 1
    elif ABC == 'i':
        indexOfVowels += 1
        indexI += 1
indexOfConsonants = const - indexOfVowels

print("Гласные = {0} \nСогласные = {1} \nA = {2} \nE = {3} \nI = {4} \nU = {5} \nO = {6} \nY = {7}".format(indexOfVowels, indexOfConsonants, indexA, indexE, indexI, indexU, indexO, indexY))

# Задача 3

print('Минимальная сумма стартапа')
minCashStartap = int(input())
print('Кэш Иван')
cashIvan = int(input())
print('Кэш Майк')
cashMike = int(input())

if minCashStartap <= cashMike and cashIvan >= minCashStartap:
    print(2)
elif cashIvan >= minCashStartap >= cashMike:
    print('Ivan')
elif cashIvan <= minCashStartap <= cashMike:
    print('Mike')
elif (minCashStartap >= cashMike and minCashStartap >= cashIvan) and minCashStartap <= (cashIvan + cashMike):
    print(1)
elif (minCashStartap >= cashMike and minCashStartap >= cashIvan) or minCashStartap >= (cashIvan + cashMike):
    print(0)

print(sys.stdin.readline())