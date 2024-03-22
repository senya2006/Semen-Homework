#names = ['Maryna', 'Ivan', 'Olga', 14, 78, True, True, False, 'Maryna', ['test']]   # list
#second = ['test', 'autotest']
#names.extend(second)  добавляет друг к другу два списка
#names.append(second)  тоже добавляет но со скобочками
#names.pop()           выдает последний елемент в списке или по индексу
#names.remove()        нельзя писать в принте и не удаляет елемент которого нету в списке
#names.count()         нельзя писать в принте и в скобочках надо вписать елемент который хочешь посчитать
#names.reverse()       нельзя писать в принте и переворачивает список
# print(names.index('Maryna'))    показывает на каком индексе элемент

# names = ('Maryna', 'Ivan', 'Olga', 'Olga')  #  кортеж/tuple не изменяемый тип данных
# new_tuple = tuple()     # <class 'tuple'>
# new_tuple_2 = 1, 2, 3, 4   # <class 'tuple'>

#names = ['Hillel', 'IT', 'school']
#print(names.split())   # преобразовывает стрингу в список
#print(''.join(names))   # соеденяет все в одну строку тоесть в стринг
# если в скобках поставить запятую или пробел оно этим способом разделит елементы

# if names:
#     print(f'{type(names)} {names} is not empty')
# else:
#     print(f'{type(names)} {names} is empty')

#if 'Maryna' in names:
#    print('True')
#else:
#    print('False')

# new_tuple_3 = ('abc',)      # <class 'tuple'>
# test = names + new_tuple_2
# print(test)
# print(1 in names)       # True/False


#test = sorted(names)     сортирует, заглавная буква важнее
# age = [5, -674, 90, 1, 0, 10]
# age.sort()
#names.sort(key=str.upper)
#new_list = names.copy()    копирует лист что бы потом со скопируемым можно было делать операции

