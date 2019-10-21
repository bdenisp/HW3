"""
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
"""

set_numbers1 = []
set_numbers2 = []

numbers1 = input('Введите элементы 1-го списка через разделитель (, или ; или /):')
numbers2 = input('Введите элементы 2-го списка через разделитель (, или ; или /):')

# получение разделителя из 1-ой введенной строки
for i in range(len(numbers1)):
    if not (numbers1[i].isdigit()):
        separator1 = numbers1[i]

# получение разделителя из 2-ой введенной строки
for i in range(len(numbers2)):
    if not (numbers2[i].isdigit()):
        separator2 = numbers2[i]

# разделение 1-ой строки на элементы и запись в 1-ый список
set_numbers1 = numbers1.split(separator1)
set_numbers1 = set(set_numbers1)

# разделение 2-ой строки на элементы и запись во 2-ой список
set_numbers2 = numbers2.split(separator2)
set_numbers2 = set(set_numbers2)

set_numbers1.difference_update(set_numbers2)
set_numbers1 = list(set_numbers1)
set_numbers1.sort()

print ('Результат:', set_numbers1)
