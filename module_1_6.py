my_dict = {'Linar': 1993, 'Dima': 1990, 'Ruslan': 1995}
print(my_dict)
print(my_dict['Dima'])
my_dict['Daniel'] = 2020
print(my_dict['Daniel'])
my_dict.update({'Misha': 1984,
                'Sergey': 1967})
del my_dict['Sergey']
print(my_dict.update())
print(my_dict)

my_set = {1,2,3,4,5,1,3,5,'Рука', 'Нога', 'Рука'}
print(my_set)
my_set.add('Голова')
my_set.add((15, 17,19))
my_set.discard('Нога')
print(my_set)