import sys

# Задача 1

print("Напишите слово")
s1 = input().lower()
L = len(s1)
D = int(L/2)

Li = L - 1
i = 0
YES = 0
NO = 0
while L > D:
    if s1[i] == s1[Li]:
        YES += 1
    else:
        NO += 1
    i += 1
    Li -= 1
    L -= 1

if NO == 0:
    print("YES")
else:
    print("NO")


# Задача 2

print("Напишите текст")
text = input()
SText = text.split(" ")
LL = len(SText) - 1
newText = ''
while LL >= 0:
    if SText[LL].isalpha():
        newText += SText[LL] + " "
    LL -= 1
print(newText)
print(sys.stdin.readline())