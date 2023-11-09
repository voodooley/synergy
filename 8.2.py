num = int(input('Введите количество элементов списка => '))

array = list(map(int, input('Введите числа через пробел => ').split()))

array.insert(0, array.pop())

print(array)
