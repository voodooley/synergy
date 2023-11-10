nums = [int(i) for i in input('Введите список чисел через пробел => ').split()]
sets = set()
for num in nums:
    if num in sets:
        print('YES')
    else:
        print('NO')
        sets.add(num)
