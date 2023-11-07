digit = int(input('Введите количество чисел => '))
if digit > 0:
    count = 0
    while digit > 0:
        num = int(input('Введите число => '))
        if num == 0:
            count += 1

        digit -= 1
    print(f'Количество чисел равных нулю равно {count}')
else:
    print('Число должно быть больше нуля')
