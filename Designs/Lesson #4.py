# Задача 1
print("Введите параметры прямоугольника:\nA = ")
a = float(input())
print("B = ")
b = float(input())
sq = a * b
pr = a * 2 + b * 2
print('Площадь = {0:.2f} \nПериметр = {1:.2f}'.format(sq, pr))


# Задача 2
print("\n")
a = 46275
ed = float(a%10)
dec = ((a%100)-ed)/10
hun = ((a%1000)-(a%100))/100
th = ((a%10000)-(a%1000))/1000
dec_th = ((a%100000)-(a%10000))/10000
result = ((dec ** ed) * hun)/(dec_th - th)
print(result)