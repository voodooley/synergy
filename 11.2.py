import collections

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}


def get_suffix(age):
    if age % 10 == 1 and age != 11 and age % 100 != 11:
        return 'год'
    elif age % 10 in (2, 3, 4) and age not in (12, 13, 14) and age % 100 not in (12, 13, 14):
        return 'года'
    else:
        return 'лет'


def create():
    print("### Команда create")

    key = input("Кличка питомца: ")
    fields = ["Вид питомца", "Возраст питомца", "Имя владельца"]
    temp = {key: dict()}

    for field in fields:
        res = input(f"{field}: ")

        temp[key][field] = int(res) if res.isnumeric() else res

    last = collections.deque(pets, maxlen=1)[0]

    pets[last + 1] = temp


def read():
    print("### Команда read")
    pet_id = int(input("Введите Id: "))
    pet = get_pet(pet_id)

    if not pet:
        print(f"Нет питомца с таким ID:{pet_id}")
        return

    key = [x for x in pet.keys()][0]

    string = f'Это {pet[key]["Вид питомца"]} по кличке "{key}". ' \
 \
             f'Возраст питомца: {pet[key]["Возраст питомца"]} {get_suffix(pet[key]["Возраст питомца"])}. ' \
 \
             f'Имя владельца: {pet[key]["Имя владельца"]}'

    print(string)


def update():

    print("### Команда update")
    pet_id = int(input("Введите Id: "))
    pet = get_pet(pet_id)

    if not pet:
        print(f"Питомца с Id({pet_id}) не существует")
        return

    keys = [x for x in pet.keys()][0]

    print("Введите данные или оставьте поле пустым. Нажмите Enter")

    temp = dict()

    for key, value in pet[keys].items():

        res = input(f"{key}: ")

        if res:
            temp[key] = int(res) if res.isnumeric() else res
            pet[keys].update(temp)


def delete():
    print("### Команда delete")
    pet_id = int(input("Введите ID: "))
    pets.pop(pet_id, None)


def get_pet(pet_id):
    return pets.get(pet_id, False)


def pets_list():
    for key, val in pets.items():
        print(f"{key}", val)


commands = {
    "create": create,
    "read": read,
    "update": update,
    "delete": delete,
    "list": pets_list,
    "stop": 0
}


def print_commands():
    print("Список доступных команд:")

    for key in commands:
        print("> ", key)


if __name__ == '__main__':
    while True:
        print_commands()
        command = input("Введите команду: ")

        if command not in commands.keys():
            print('Такой команды нет. Попробуйте еще раз')
            continue

        if command == "stop":
            break

        commands[command]()
        input("Далее...")
