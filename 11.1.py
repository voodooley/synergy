num = int(input('Введите натуральное целое число => '))


def factorial(number: int):
    fact = 1
    for n in range(1, number + 1):
        fact *= n
    return fact


my_list = []
for i in range(factorial(num), 0, -1):
    my_list.append(factorial(i))

print(my_list)
