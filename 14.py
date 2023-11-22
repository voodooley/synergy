my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def recursion(lst: list):
    if len(lst) > 0:
        print(lst[0], end=' ')
        lst.pop(0)
        recursion(lst)
    else:
        print('Конец списка')
        return


recursion(my_list)
