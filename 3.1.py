animal = input('Введите животное => ')
name = input('Введите кличку животного => ')
age = int(input('Введите возраст животного => '))

end = ''
if age in (11, 12, 13, 14):
    end = 'лет'
elif age % 10 == 1:
    end = 'год'
elif age % 10 in (2, 3, 4):
    end = 'года'
else:
    end = 'лет'

print(f'Это {animal} по кличке "{name}". Возраст: {age} {end}.')
