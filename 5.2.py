word = input('Введите слово: ')

a = word.count('a')
e = word.count('e')
i = word.count('i')
o = word.count('o')
u = word.count('u')

count = a + e + i + o + u

print(f'Всего согласных букв: {len(word) - count}. Всего гласных букв: {count}')

print('Количеcтво букв "a": ', end='')
print(a) if a != 0 else print('False')

print('Количеcтво букв "e": ', end='')
print(e) if e != 0 else print('False')

print('Количеcтво букв "i": ', end='')
print(i) if i != 0 else print('False')

print('Количеcтво букв "o": ', end='')
print(o) if o != 0 else print('False')

print('Количеcтво букв "u": ', end='')
print(u) if u != 0 else print('False')
