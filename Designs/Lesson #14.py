import sys

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def list_print():
    print(my_list[0])
    my_list.pop(0)
    if len(my_list) == 0:
        print('Конец списка')
        return 0
    list_print()


list_print()

print(sys.stdin.readline())