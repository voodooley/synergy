num = int(input('Введите количество элементов списка 1 => '))
num2 = int(input('Введите количество элементов списка 2 => '))

i = 0
array = []
array2 = []

while i < num:
    array.append(int(input(f'Введите число {i + 1} для списка 1 => ')))
    i += 1

i = 0

while i < num:
    array2.append(int(input(f'Введите число {i + 1} для списка 2 => ')))
    i += 1

nums = set(array).intersection(set(array2))

print(len(nums))
