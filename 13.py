import random

size = input('Размеры матрицы, через пробел => ')

row, col = map(int, size.split())

print(f'{row}x{col}')

matrix_1 = [[random.randint(-100, 100) for _ in range(col)] for _ in range(row)]
matrix_2 = [[random.randint(-100, 100) for _ in range(col)] for _ in range(row)]


def print_list(matrix):
    print('*' * 30)
    for r in matrix:
        print(*r)


print_list(matrix_1)
print_list(matrix_2)


res = [[matrix_1[r][c] + matrix_2[r][c] for c in range(col)] for r in range(row)]

print_list(res)
