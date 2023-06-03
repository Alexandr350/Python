import sys
import random


X = []


def user_input():
    global X
    X = input('Укажите размерность матрицы, например 4x3: ').split('x')


def create_matrix():
    matrix = []
    for z in range(int(X[0])):
        matrix.append([0] * int(X[1]))
    return matrix


def matrix_summa(matrix1, matrix2):
    summa_two_matrix = create_matrix()
    for i in range(len(matrix1)):
        for j in range(len(matrix2[i])):
            summa_two_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return summa_two_matrix


def matrix_print(matrix):
    for m in range(len(matrix)):
        print(*matrix[m])


def matrix_random(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(random.random()*100)
    matrix_print(matrix)
    print('\n')
    return matrix


user_input()
matrix_print(matrix_summa(matrix_random(create_matrix()), matrix_random(create_matrix())))


print(sys.stdin.readline())