import sys

# Задача 1


def age_year(age):
    if 10 <= age <= 14:
        return "лет"
    else:
        tmp = age/10
        y = int(age/10)
        year = int((tmp - y + 0.01) * 10)
        if year == 1:
            return "год"
        if 5 > year > 1:
            return "года"
        if 4 < year < 10:
            return "лет"


pets = {}

while True:
    NAME = input('Кличка питомца: ')
    KIND = input('Вид питомца: ')
    AGE = int(input('Возраст: '))
    OWNER = input('Имя владельца: ')
    pets[NAME] = {'Kind': KIND, 'Age': AGE, 'Owner': OWNER}
    y_n = input("Добавить нового питомца Да/Нет: ").lower()
    if y_n == "нет":
        break


for pet, name in pets.items():
    print('\nЭто {1} по кличке "{0}". Возраст питомца: {2} {3}.'
          ' Имя владельца: {4}'.format(pet, name['Kind'], name['Age'],
                                       age_year(name['Age']), name['Owner']))

# Задача 2

dictionary = {}
i = 10
while i != -6:
    dictionary[i] = i ** i
    i -= 1

for j, k in dictionary.items():
    print(j, "\t", k)
print(sys.stdin.readline())
