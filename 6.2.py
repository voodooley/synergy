num = int(input('Введите число => '))

count = 2

sqr = int(num ** 0.5)

for digit in range(2, sqr + 1):
    if num % digit == 0:
        count += 2

if num ** 0.5 % 1 == 0:
    count -= 1

print(count)
