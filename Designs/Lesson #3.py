import sys

# Задача 1
print("Вид питомца")
animal = input()
print("Возраст")
age = input()
print("Кличка")
name = input()
print("\n")
text = ("Это {0} "
        "по кличке {2}. "
        "Возраст: {1} года".format(animal, age, name))
print(text)

# Задача 2

print("Напишите по порядку этапы развития человека")
a1 = input()
a2 = input()
a3 = input()
a4 = input()
a5 = input()
print("\n")
print(a1, a2, a3, a4, a5, sep=' => ')
print(sys.stdin.readline())