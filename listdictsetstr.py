"""
1. Из всех методов списка (list) выбрать 5 тех, которые по вашему мнению используются чаще всего
2. Написать их через запятую с параметрами
3. Повторить процедуру для словарей (dict), множеств (set), строк (str)
"""

# списки

friends = ['anton', 'maxim', 'denis']

friends.append('diana')
friends.insert(1, 'olga')
friends.sort()
friends.reverse()
friends.remove('anton')

# словари

friends_work = {
    'anton': 'work1',
    'maxim': 'work2',
    'denis': 'work3'
}

friends_work.items()
friends_work.keys()
friends_work.values()
friends_work.get('anton')
friends_work.pop('anton')

# множества

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {2, 4, 6, 8, 10}
set3 = {1, 3, 5, 7, 9}

set1.add(0)
set1.remove(1)
set2.update(set3)
set1.difference(set2)
set1.intersection(set2)

# строки

tongue_twister = 'Ехал Грека через реку'

tongue_twister.upper()
tongue_twister.lower()
tongue_twister.replace(' ', ';')
tongue_twister.split(' ')
tongue_twister.title()
