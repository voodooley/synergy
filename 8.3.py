capacity = int(input('Введите грузоподъемность одной лодки => '))
fman = int(input('Введите количество рыбаков => '))
weight = []

for i in range(fman):
    weight.append(int(input(f'Введите вес {i + 1} рыбака не больше {capacity} => ')))

count = 0
st = 0

while len(weight) > 1:
    if max(weight) + min(weight) <= capacity:
        weight.remove(max(weight))
        weight.remove(min(weight))
        count += 1
    else:
        weight.remove(max(weight))
        count += 1

if len(weight) == 1:
    count += 1

print(f'Минимальное количество лодок - {count}')
