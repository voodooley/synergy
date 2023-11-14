pets = {}

name = input('Введите кличку животного => ')

if name:
    animal = input('Введите вид животного => ')
    age = int(input('Введите возраст животного => '))
    master = input('Введите хозяина животного => ')

    pet = dict()
    pet['Вид питомца'] = animal
    pet['Возраст питомца'] = age
    pet['Имя владельца'] = master

    pets[name] = pet

    end = ''
    if age % 10 == 1 and age != 11 and age % 100 != 11:
        end = 'год'
    elif age % 10 in (2, 3, 4) and age not in (12, 13, 14) and age % 100 not in (12, 13, 14):
        end = 'года'
    else:
        end = 'лет'

    print(f'Это {pets[name]["Вид питомца"]} по кличке "{name}". Возраст: {pets[name]["Возраст питомца"]} {end}. Имя '
          f'владельца: {pets[name]["Имя владельца"]}')
else:
    print('Имя не должно быть пустым. Попробуйте снова')
