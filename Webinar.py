# print(abs(-5))
#
# # Побитовые операции (расчет идет в 2-битной системе)
# print(5 & 3)  # умножение
# print(5 | 3)  # сложение
# print(5 ^ 3)  # логическое или для 0 и 1 (где различаются - 1, если одинаковы - 0)
# print(5 << 3)  # Битовый сдвиг влево умножение 5 на 2 в степени 3 (5 / 2 ** 3)
# print(5 >> 3)  # Битовый сдвиг вправо деление 5 на 2 в степени 3 (5 / 2 ** 3)
#
# print(int('111', 2))  # перевод в инт из двоичной системы
# print(bin(7))  # в двоичную
# print(oct(7))  # в восьмиричную
# print(hex(7))  # в шестнадцатиричную
#
#
#
## строки
#
my_str = 'Konstantin Petrovich'
# print(my_str[2])  # 3 буква
# print(my_str + my_str)  # Конкатенация
# print(my_str[1:6:2])  # срез [start:stop:step] stop не включается в срез
# print(my_str[1:])  # от 1 и до конца
# print(my_str[:5])  # до 5 символа
# print(my_str[1::2])  # от 1 и до конца c шагом 2
# print(my_str[-2])  # обращение с конца (нумерация с -1)
# print(my_str[::-1])  # реверс
# print(my_str[:-1])  # без последнего символа
# print(len(my_str))  # пробел учитывается

# print((my_str.split()))  # разбивает по пробелу
# print((my_str.split('tantin Pe')))
# val = ['Kons', 'trovich', '1', 'joke']
# print((', '.join(val)))  # соединяет символы разделяя , (можно указать люб символ)
# print(my_str.capitalize())  # первая буква заглавная, а все последующие маленькие
# print(my_str.title())  # каждое слово с большой буквы
# print(my_str.lower())  # все буквы в нижнем регистре
# print(my_str.upper())  # все буквы в верхнем регистре
# print(my_str.istitle())  #отвечает ли канону title (каждое слово с большой буквы)
# my_str = my_str.replace('K', 'q')  # замена символа
# print(my_str)
# print(my_str.count('o'))  # подсчитывает количество символов 'o'
# print(my_str.find('o'))  # выводит индекс первой буквы 'o'
# print(my_str.find('o', 7))  # выводит индекс первой буквы 'o' начиная с 7 символа
# print(my_str.find('o', 16))  # если не находит, то выводит -1
# print(my_str.rfind('o'))  # выводит индекс первой буквы 'o' начиная с 7 символа справа-налево


## ТИП ДАННЫХ: СПИСОК

my_list = ['Artyom', 50000, True, 12.3]
# print(my_list[0])
# my_list[2] = False
# my_list.append(100)  # добавляет в конец списка
# my_list.insert(1, 100) # добавляет в 1 индекс списка НЕ ЗАМЕНЯЕТ!
# # my_list.pop()  # удаляет последний символ
# # qwe = my_list.pop(0)  # удаляет определенный символ и задает его в переменную
# # print(my_list, qwe)
# my_list.reverse()
# print(my_list.count(50000))  # сколько раз встретился элемент списка (5000 = 0)
# my_list.index(50000)

# print(12.3 in my_list)  # проверяет наличие объекта в списке
# print(my_list)


# КОРТЕЖ - не изменяем

my_tuple = ('Artyom', 50000, True, 12.3, 'Ab')
# print(type(my_tuple))
# qwe = list(my_tuple)
# qwe[0] = 'qwe'
# print(qwe)

# МНОЖЕСТВО

# my_set = {1, 1, 1, 1, 2, 2, 2, 10, 2, 1001}
# print(my_set)  # схлопывает до уникальных значений 1, 2, 10, 1001
# qwe = [1, 1, 1, 1, 2, 2, 2, 10, 2, 1001]
# print(len(set(qwe)))  # подсчитывает количество уникальных значение
# a = {2, 3, 4}
# b = {4, 5, 6}
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)
# a.remove(100)  # выдает ошибку если объекта нет во множестве
# a.discard(100)  # продолжает работать если нет элемента
# print(a)


# СЛОВАРЬ

human = {'name': 'Ivan', 'age': 80, True: 'admin'}
# print(type(human))
# print(human)
# print(human['age'])
# human['data'] = [1, 11, 1]
# print(human)

# print(human.keys())
# print(human.values())
# print(human.items())
# print(human.get('zxc'))  # Если ключ отсутствует, то возвращает значение None и продолжает выполнение программы
# print(human.get('name'))
# print(human.get('zxc', 'default'))  # Если ключ отсутствует, то возвращает значение default и продолжает выполнение
# программы
# print(human.get('name', 'default'))
# human.pop('age')
# print(human)

# ИСКЛЮЧЕНИЯ

# try:
#     a = int(input('chislo'))
#     print(100 / a)
# except ValueError:
#     print('ne chislo')
# except ZeroDivisionError:
#     print(0)

# ЦИКЛ FOR

# for qwe in my_tuple:
#     print(qwe)

# for key, val in human.items():  # если вылетает кортеж, то можно его сразу записать в переменные
#     print(key, val)
#
# for i in range(10):
#     print(i, 'Hello')

# ТЕРНАРНЫЙ ОПЕРАТОР

# age = 50
# if age >= 18:
#     print('Hello')
# else:
#     print('Bye')
#
# print('hello' if age >= 18 else 'bye')
# access = True if age >= 18 else False
# print(access)

# ОПЕРАТОР IS

# a = [5]
# b = [5]
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)  # сравнивает по id кортеж будет тру, т.к. неизменяем. для Int при сравнении одинаковых цифр True будет
# выдаваться только в диапазоне [-5 .. 256], но при работе в PyCharm этого диапазона нет! ВАЖНО!!! Программа работает в
# консоли!!! следовательно необходимо учитывать и помнить про диапазон!

# a = [1, 2, 3]
# b = a
# b.append(100)
# print(a is b)
# print(a)
#
# c = [1, 2, 3]
# d = c.copy()
# d.append(100)
# print(c is d)
# print(c)
# print(d)

a = [1, 2, 3, [100, 200]]
b = a.copy()
b[3].append(300)
print(a is b)
print(a)
print(b)

import copy
a = [1, 2, 3, [100, 200]]  # для вложенных листо необх импорт copy, т.к. .copy отвяжет ссылки только от внешнего листа,
# но не от внутреннего

b = copy.deepcopy(a)
b[3].append(300)
print(a is b)
print(a)
print(b)
