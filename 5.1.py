digit = int(input())

sign = ''
parity = ''

if digit != 0:
    if digit % 2 == 0:
        parity += 'четное'
    else:
        parity += 'нечетное'
    if digit > 0:
        sign += 'Положительное'
    else:
        sign += 'Отрицательное'
else:
    sign += 'Нулевое'

print(sign, parity, 'число')
