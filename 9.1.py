num = int(input('Введите количество элементов списка => '))

i = 0
array = []

while i < num:
    array.append(int(input('Введите число => ')))
    i += 1

numbers = set(array)

print(len(numbers))
