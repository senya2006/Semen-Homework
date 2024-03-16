#names = ['Maryna', 'Ivan', 'Olga', 14, 78, True, True, False, 'Maryna', ['test']]   # list
#second = ['test', 'autotest']
#names.extend(second)  добавляет два списка
#names.append(second)  тоже добавляет но со скобочками
#ages = [31, 45, 15]
#names.append('Nastya')
#names.pop()
#names.remove()
#names.count()
#names.reverse()  переворачивает список
#print(names)

# names = ('Maryna', 'Ivan', 'Olga', 'Olga')  #   не изменяемый тип данных
# new_tuple = tuple()     # <class 'tuple'>
# new_tuple_2 = 1, 2, 3, 4   # <class 'tuple'>

#names = ['Hillel', 'IT', 'school']
#print(names.split())   # преобразовывает стрингу в список
#print(''.join(names))   # соеденяет все в одну строку тоесть в стринг,
# если в скобках поставить запятую или пробел оно сделает

# if names:
#     print(f'{type(names)} {names} is not empty')
# else:
#     print(f'{type(names)} {names} is empty')

#if 'Maryna' in names:
#    print('True')
#else:
#    print('False')

# new_tuple_3 = ('abc',)      # <class 'tuple'>
# print(type(new_tuple_3))
# print(names.index('maryna'))    # показывает на каком индексе элемент
# print(names.count('Olga'))      # показывает сколько
# test = names + new_tuple_2
# print(test)
# print(1 in names)       # True/False


#test = sorted(names)  сортирует, заглавная буква важнее
# age = [5, -674, 90, 1, 0, 10]
# age.sort()
#names.sort(key=str.upper)
#new_list = names.copy()  копирует лист
