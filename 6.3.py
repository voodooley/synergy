a = int(input('Введите число A => '))
b = int(input('Введите число B => '))


for num in range(a, b + 1):
    if num % 2 == 0:
        print(num, end=' ')