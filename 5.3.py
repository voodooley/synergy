amount = int(input('Введите минимальную сумму инвестиций => '))
mike = int(input('Введите сумму Майкла => '))
ivan = int(input('Введите сумму Ивана => '))

if mike > amount and ivan > amount:
    print(2)
else:
    if mike > amount or ivan > amount:
        if mike > amount:
            print('Mike')
        else:
            print('Ivan')
    else:
        if mike + ivan >= amount:
            print(1)
        else:
            print(0)

