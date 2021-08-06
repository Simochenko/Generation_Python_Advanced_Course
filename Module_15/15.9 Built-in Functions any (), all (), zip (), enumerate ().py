'''Тема урока: функции any(), all(), zip(), enumerate()
Функция all()
Функция any()
Функция enumerate()
Функция zip()
Аннотация. Урок посвящен встроенным функциям all(), any(), zip(), enumerate().

Функции all() и any()
При работе с коллекциями часто приходится определять, выполняется ли некоторое условие одновременно для всех элементов
последовательности или хотя бы для одного. Для этого существуют две встроенные функции all() и any().

Функция all()
Встроенная функция all() возвращает значение True, если все элементы переданной ей последовательности (итерируемого
объекта) истинны (приводятся к значению True), и False в противном случае.

Сигнатура функции следующая: all(iterable). В качестве iterable может выступать любой итерируемый объект:

список;
кортеж;
строка;
множество;
словарь и т.д.
Приведенный ниже код:

print(all([True, True, True]))     #  возвращает True, так как все значения списка равны True
print(all([True, True, False]))    #  возвращает False, так как не все значения списка равны True
выводит:

True
False
Напомним, что в Python все следующие значения приводятся к значению False:

константы None и False;
нули всех числовых типов данных: 0, 0.0, 0j, Decimal(0), Fraction(0, 1);
пустые коллекции: '', (), [], {}, set(), range(0).
Приведенный ниже код:

print(all([1, 2, 3]))
print(all([1, 2, 3, 0, 5]))
print(all([True, 0, 1]))
print(all(('', 'red', 'green')))
print(all({0j, 3+4j}))
выводит:

True
False
False
False
False
При работе со словарями функция all() проверяет на соответствие параметрам True ключи словаря, а не их значения.

Приведенный ниже код:

dict1 = {0: 'Zero', 1: 'One', 2: 'Two'}
dict2 = {'Zero': 0, 'One': 1, 'Two': 2}

print(all(dict1))
print(all(dict2))
выводит:

False
True
Обратите внимание: если переданный итерируемый объект пустой, то функция all() возвращает значение True.

Приведенный ниже код:

print(all([]))          #  передаем пустой список
print(all(()))          #  передаем пустой кортеж
print(all(''))          #  передаем пустую строку
print(all([[], []]))    #  передаем список, содержащий пустые списки
выводит:

True
True
True
False
Функция any()
Встроенная функция any() возвращает значение True, если хотя бы один элемент переданной ей последовательности
(итерируемого объекта) является истинным (приводится к значению True), и False в противном случае.

Сигнатура функции следующая: any(iterable). В качестве iterable может выступать любой итерируемый объект:

список;
кортеж;
строка;
множество;
словарь и т.д.
Приведенный ниже код:

print(any([False, True, False]))       #  возвращает True, так как есть хотя бы один элемент, равный True
print(any([False, False, False]))      #  возвращает False, так как нет элементов, равных True
выводит:

True
False
Приведенный ниже код:

print(any([0, 0, 0]))
print(any([0, 1, 0]))
print(any([False, 0, 1]))
print(any(['', [], 'green']))
print(any({0j, 3+4j, 0.0}))
выводит:

False
True
True
True
True
При работе со словарями функция any() проверяет на соответствие True ключи словаря, а не их значения.

Приведенный ниже код:

dict1 = {0: 'Zero'}
dict2 = {'Zero': 0, 'One': 1}

print(any(dict1))
print(any(dict2))
выводит:

False
True
Обратите внимание: если переданный объект пуст, то функция any() возвращает значение False.

Приведенный ниже код:

print(any([]))          #  передаем пустой список
print(any(()))          #  передаем пустой кортеж
print(any(''))          #  передаем пустую строку
print(any([[], []]))    #  передаем список, содержащий пустые списки
выводит:

False
False
False
False
Функции all() и any() в связке с функцией map()
Функции all() и any() могут быть полезны в комбинации с функцией map(), которая может преобразовывать элементы

 последовательности (итерируемого объекта) к значению True/False в соответствии с неким условием.

Приведенный ниже код, проверяет, все ли элементы списка numbers больше 1010:

numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

result = all(map(lambda x: True if x > 10 else False, numbers))

if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')
и выводит:

Хотя бы одно число меньше или равно 10
так как список numbers содержит число 55, которое не больше чем 1010.

Лямбда функцию, которая преобразует элементы списка numbers в значения True/False можно упростить следующим образом:

result = all(map(lambda x: x > 10, numbers))
Приведенный ниже код, проверяет, что хотя бы один элемент списка четное число:

numbers = [17, 91, 78, 55, 231, 45, 5, 89, 99, 11, 19]

result = any(map(lambda x: x % 2 == 0, numbers))

if result:
    print('Хотя бы одно число четное')
else:
    print('Все числа нечетные')
и выводит:

Хотя бы одно число четное
так как список numbers содержит четное число 7878.

Функция enumerate()
Встроенная функция enumerate() возвращает кортеж из индекса элемента и самого элемента переданной ей
последовательности (итерируемого объекта).

Сигнатура функции следующая: enumerate(iterable, start). В качестве iterable может выступать любой итерируемый объект:

список;
кортеж;
строка;
множество;
словарь и т.д.
С помощью необязательного параметра start можно задать начальное значение индекса. По умолчанию значение параметра
start = 0, то есть счет начинается с нуля.

Приведенный ниже код:

colors = ['red', 'green', 'blue']

for pair in enumerate(colors):
    print(pair)
выводит:

(0, 'red')
(1, 'green')
(2, 'blue')
Если счет нужно начать с отличного от нуля числа, то нужно передать значение аргумента start.

Приведенный ниже код:

colors = ['red', 'green', 'blue']

for pair in enumerate(colors, 100):
    print(pair)
выводит:

(100, 'red')
(101, 'green')
(102, 'blue')
Обратите внимание, функция enumerate() возвращает не список, а специальный объект, который называется итератором.
Такой объект похож на список тем, что его можно перебирать циклом for, то есть итерировать. Итератор можно
преобразовать в список с помощью функции list().

Приведенный ниже код:

colors = ['red', 'green', 'blue']

pairs = enumerate(colors)

print(pairs)
print(list(pairs))
выводит:

<enumerate object at 0x...>
[(0, 'red'), (1, 'green'), (2, 'blue')]
Мы также можем использовать распаковку кортежей при итерировании с помощью цикла for.

Приведенный ниже код:

colors = ['red', 'green', 'blue']
for index, item in enumerate(colors):
    print(index, item)
выводит:

0 red
1 green
2 blue
Такой код является альтернативой коду:

colors = ['red', 'green', 'blue']
for i in range(len(colors)):
    print(i, colors[i])
Функция zip()
Встроенная функция zip() объединяет отдельные элементы из каждой переданной ей последовательности (итерируемого
объекта) в кортежи.

Сигнатура функции следующая: zip(*iterables). В качестве iterable может выступать любой итерируемый объект:

список;
кортеж;
строка;
множество;
словарь и т.д.


Приведенный ниже код:

numbers = [1, 2, 3]
words = ['one', 'two', 'three']

for pair in zip(numbers, words):
    print(pair)
выводит:

(1, 'one')
(2, 'two')
(3, 'three')
Функция zip(), как и функция enumerate() возвращает не список, а специальный объект, который называется итератором.
 Такой объект похож на список тем, что его можно перебирать циклом for, то есть итерировать. Итератор можно
 преобразовать в список с помощью функции list().

Приведенный ниже код:

numbers = [1, 2, 3]
words = ['one', 'two', 'three']

result = zip(numbers, words)

print(result)
print(list(result))
выводит:

<zip object at 0x...>
[(1, 'one'), (2, 'two'), (3, 'three')]
Мы можем передавать функции zip() сколько угодно итерируемых объектов.

Приведенный ниже код:

numbers = [1, 2, 3]
words = ['one', 'two', 'three']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result))
выводит:

[(1, 'one', 'I'), (2, 'two', 'II'), (3, 'three', 'III')]
Мы можем передать функции zip() даже один итерируемый объект.

Приведенный ниже код:

numbers = [1, 2, 3]
result = zip(numbers)
print(list(result))
выводит:

[(1,), (2,), (3,)]
Если функции zip() передать итерируемые объекты, имеющие разную длину, то объект с наименьшим количеством элементов
определяет итоговую длину.

Приведенный ниже код:

numbers = [1, 2, 3, 4]
words = ['one', 'two']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result))
выводит:

[(1, 'one', 'I'), (2, 'two', 'II')]
Частые сценарии использования функции zip()
Сценарий 1. Функция zip() удобна для создания словарей, когда ключи и значения находятся в разных списках.

Приведенный ниже код:

keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

info = dict(zip(keys, values))
print(info)
выводит:

{'name': 'Timur', 'age': 28, 'gender': 'male'}
Сценарий 2. Функция zip() удобна для одновременного (параллельного) итерирования сразу по нескольким коллекциям.

Приведенный ниже код:

name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]

for x, y in zip(name, age):
    print(x, y)
выводит:

Timur 28
Ruslan 21
Rustam 19
Примечания
Примечание 1. Итераторы – важная концепция языка Python. Нужно помнить:

итераторы можно обойти циклом for;
итератор можно преобразовать в список или кортеж, с помощью функций list() и tuple();
итератор можно распаковать с помощью *.
Примечание 2. Реализация встроенных функций all() и any() выглядит примерно так:

def all(iterable):
    for item in iterable:
       if not item:
           return False
    return True

def any(iterable):
    for item in iterable:
        if item:
            return True
    return False
Примечание 3. Мы можем использовать одновременно функции zip() и enumerate():

Приведенный ниже код:

list1 = ['a1', 'a2', 'a3']
list2 = ['b1', 'b2', 'b3']

for index, (item1, item2) in enumerate(zip(list1, list2)):
    print(index, item1, item2)
выводит:

0 a1 b1
1 a2 b2
2 a3 b3'''

# numbers = [1, 2, 3, 4, 5, 6]
#
# for index, elem in enumerate(numbers):
#     if elem % 2 == 0:
#         numbers[index] *= 2
#
#
# print(numbers)

# numbers = [10, 30, 20, 50, 40, 60, 70, 80]
#
# total = 0
# for index, number in enumerate(numbers, 1):
#     if index % 2 == 0:
#         total += number
# print(total)

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
#
# result = 0
# for x, y in zip(list1, list2):
#     result += x*y
# print(result)


# words1 = ['яблоко', 'ананас', 'апельсин', 'хурма', 'гранат', 'мандарин', 'айва']
# words2 = ['林檎', 'パイナップル', 'オレンジ', '柿']
# words3 = ['apple', 'pineapple', 'orange', 'persimmon', 'pomegranate']
#
# print(len(list(zip(words1, words2, words3))))


'''Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,

и возвращает значение True, если в команде содержится слово из списка ignore и False – если нет.

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False
Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any() сохранив при этом ее 
функционал.

Примечание 1. Следующий программный код:

print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))
должен выводить:

True
True
True
False
Примечание 2. Вызывать функцию ignore_command() не нужно, требуется только реализовать.'''



# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(word in command for word in ignore)
#
# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: x in command, ignore))


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     s = []
#     for word in ignore:
#         if word in command:
#             s.append(1)
#         s.append(0)
#     return any(s)

'''Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о 
стране в формате:

<capital> is the capital of <country>, population equal <population> people.


Moscow is the capital of Russia, population equal 145934462 people.
New York is the capital of USA, population equal 331002651 people.
...
Для каждой страны информацию выводить на отдельной строке. '''


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# result = zip(countries, capitals, population)
# for i in result:
#     print(f'{i[1]} is the capital of {i[0]}, population equal {i[2]} people.')


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for country, capital, people in zip(countries, capitals, population):
#     print(f'{capital} is the capital of {country}, population equal {people} people.')
#
#

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for data in zip(countries, capitals, population):
#     print('{1} is the capital of {0}, population equal {2} people.'.format(*data))


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for country, capital, people in zip(countries, capitals, population):
#     print(f'{capital} is the capital of {country}, population equal {people} people.')


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# for x in zip(capitals,countries,population):
#     print(f'{x[0]} is the capital of {x[1]}, population equal {x[2]} people.')


'''Корректный IP-адрес
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.

В 44-й версии IP-адрес представляет собой 3232-битное число. Адрес записывается в виде четырёх десятичных чисел 
(октетов) со значением от 00 до 255255 (включительно), разделённых точками, например, 192.168.1.2192.168.1.2.

Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в
 IP-адресе – числа со значением от 00 до 255255.

Формат входных данных
На вход программе подается строка в формате x.x.x.x, где x – непустой набор символов 0-9, a-z.

Формат выходных данных
Программа должна вывести True если введенная строка – корректный IP-адрес и False в противном случае.

Примечание. Ведущие нули следует игнорировать:

0001 = 1
006 = 6
0213 = 213
0000 = 0
00345 = 345
...
Sample Input 1:

10.0.1.1
Sample Output 1:

True
Sample Input 2:

10.1.1.a
Sample Output 2:

False
Sample Input 3:

10.1.1.260
Sample Output 3:

False'''

# def validate_ip(s):
#     a = s.split('.')
#     if len(a) != 4:
#         return False
#     for x in a:
#         if not x.isdigit():
#             return False
#         i = int(x)
#         if i < 0 or i > 255:
#             return False
#     return True
#
#
# print(validate_ip(input()))

# print(all(map(lambda n: n.isdigit() and 0 <= int(n) <= 255, input().split('.'))))

# print(all(list(map(lambda x:x.isdigit() and int(x)<=255,input().split('.')))))


# octets = [int(i) if set(i) <= set('0987654321') else -1 for i in input().split('.')]
# print(all(0 <= x <= 255 for x in octets))

# print(all(list(map(lambda x:x.isdigit() and int(x)<=255,input().split('.')))))


# print(all([True if i.isdigit() and 0<=int(i)<=255 else False for i in input().split('.')]))

'''Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из 77 символов, содержит хотя бы одну цифру, заглавную и 
строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.

Sample Input 1:

abcABC9
Sample Output 1:

YES
Sample Input 2:

abAB34
Sample Output 2:

NO'''


# def password_level(password):
#     C = "0123456789"
#     f1 = f2 = f3 = False
#
#     if len(password) < 7:
#         s = "NO"
#         return s
#
#     elif password.isdigit():
#         s = "NO"
#         return s
#
#     for i in password:
#         if i.isupper():
#             f1 = True
#
#         elif i.islower():
#             f2 = True
#
#         elif i in C:
#             f3 = True
#
#     if f1 * f2 * f3:
#         s = "YES"
#
#     elif f1 ^ f2 and not f3:
#         s = "NO"
#
#     else:
#         s = "NO"
#
#     return s
# print(password_level(input()))


# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')

# s = input()
# digits = any(map(lambda char: char.isdigit(), s))
# small = any(map(lambda cha: cha.isalpha() and cha == cha.lower(), s))
# big = any(map(lambda ch: ch.isalpha() and ch == ch.upper(), s))
# dl = len(s)
#
# print('YES' if all((digits, small, big, dl >= 7)) else 'NO')


# (lambda p: print(('NO','YES')[len(p)>6 and all(map(lambda f: any(map(f, p)), (str.isdigit, str.islower, str.isupper)))]))(input())

# def low(s):
#     return any(map(lambda x: x.islower(), s))
#
# def up(s):
#     return any(map(lambda x: x.isupper(), s))
#
# def digit(s):
#     return any(map(lambda x: x.isdigit(), s))
#
# s = input()
# print('YES' if low(s) and up(s) and digit(s) and len(s) > 6 else 'NO')


# from string import ascii_lowercase, ascii_uppercase, digits
# p = input()
# if len(p) >= 7 and any([True if i in p else False for i in digits]) and any([True if i in p else False for i in ascii_lowercase]) and any([True if i in p else False for i in ascii_uppercase]):
#     print('YES')
# else:
#     print('NO')


# password = input()
#
# passwords_errors = (
#     len(password) < 7,
#     password.lower() == password,
#     password.upper() == password,
#     password.isalpha(),
#     password.isnumeric()
# )
#
# if any(passwords_errors):
#     print('NO')
# else:
#      print('YES')

'''Отличники
Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться, 
что в каждом классе есть хотя бы один отличник – ученик с оценкой 55 по контрольной работе. Напишите программу с 
использованием встроенных функций all(), any() для помощи Тимуру в проверке.

Формат входных данных
На вход программе подается натуральное число nn – количество классов. Затем для каждого класса вводится блок 
информации вида:

натуральное число kk – количество учеников в классе;
далее вводится kk строк вида: фамилия оценка.
Формат выходных данных
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае.

Sample Input 1:

4
3
Васечкин 4
Илюшин 5
Кривцов 3
2
Боталов 5
Петров 5
3
Лебеда 4
Ивлев 4
Суворов 5
2
Ласкер 4
Козлов 5
Sample Output 1:

YES'''


# n = int(input())
# res = []
# for _ in range(n):
#     tmp = any([int(input()[-1]) == 5 for _ in range(int(input()))])
#     res.append(tmp)
#
# if all(res):
#     print('YES')
# else:
#     print('NO')


# print(["NO", "YES"][all([any([int(input().split()[1]) > 4 for _ in range(int(input()))]) for _ in range(int(input()))])])


# n = int(input())
# res = 0
# for i in range(n):
#     k = int(input())
#     pupils = []
#     for j in range(k):
#         pupils.append(tuple(input().split()))
#     res += any(map(lambda x: x[1] == '5', pupils))
# print('YES' if res == n else 'NO')

#
# print("YES" if all([any(map(lambda x: int(x[1])==5,
#                             [input().split() for i in range(int(input()))])) for _ in range(int(input()))]) else "NO")


# x = []
# for i in range(int(input())):
#     x.append(any(map(lambda x: x[1] == '5', [input().split() for _ in range(int(input()))])))
#     if x[i] == False: break
# print('YES' if all(x) else 'NO')

'''Внутри шара
На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (xx), ординат (yy) и
 аппликат (zz) точек трехмерной плоскости. Напишите программу для проверки расположения всех точек с введенными 
 координатами внутри либо на поверхности шара с центром в начале координат и радиусом R = 2R =2.

Формат входных данных
На вход программе подаются три строки текста с вещественными числами, разделенными символом пробела – абсциссы, 
ординаты и аппликаты точек в трехмерной системе координат.

Формат выходных данных
Программа должна вывести True если все точки с введенными координатами находятся внутри или на границе шара и
 False, если вне.

Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.

Примечание 2. Уравнение шара имеет вид x^2+y^2+z^2 = R^2x 
2
 +y 
2
 +z 
2
 =R 
2
 .

Примечание 3. Для решения задачи используйте встроенные функции all() и zip().

Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков.

Примечание 5. Указанный шар имеет вид:



Sample Input 1:

0.0 1.0 2.0
0.0 0.0 1.1
0.0 1.0 1.5
Sample Output 1:

False
Sample Input 2:

0.0 0.0
1.5 0.0
1.1 1.1
Sample Output 2:

True
Sample Input 3:

0.637 -0.411 -0.247 1.658 0.061
-0.78 -1.374 0.762 0.306 -0.614
-1.317 -0.444 -0.572 -0.341 0.295
Sample Output 3:

True'''

# abscissas = [float(el) for el in input().split()]
# ordinates = [float(el) for el in input().split()]
# applicates = [float(el) for el in input().split()]
# print(all([bool(el[0] ** 2 + el[1] ** 2 + el[2] ** 2 <= 4) for el in zip(abscissas, ordinates, applicates)]))


# abscissas, ordinates, applicates=(map(float, input().split()) for _ in range(3))
# # print(all(map(lambda x, y, z: (x**2+y**2+z**2)**0.5 <=2, abscissas,ordinates,applicates)))
# print(all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))\

# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
#
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))


# def is_inside(x, y, z):
#     abscissas = [*map(float, x.split())]
#     ordinates = [*map(float, y.split())]
#     applicates = [*map(float, z.split())]
#     l = list(zip(abscissas, ordinates, applicates))
#     res = all(map(lambda el: True if el[0]**2+el[1]**2+el[2]**2<=4 else False, l))
#     if res:
#         return True
#     else:
#         return False
#
# a=input()
# b=input()
# c=input()
# print(is_inside(a, b, c))

'''Интересные числа
На вход программе подаются два натуральных числа aa и bb. Напишите программу с использованием встроенной функции 
all() для обнаружения всех чисел в диапазоне [a; \, b][a;b], которые делятся на каждую содержащуюся в них цифру.

Формат входных данных
На вход программе подаются два натуральных числа aa и bb на отдельных строках.

Формат выходных данных
Программа должна вывести все числа из диапазона [a; \, b][a;b], удовлетворяющие условию задачи, на одной строке, 
разделяя их символом пробела.

Примечание. Числа, содержащие нули, неинтересны, их выводить не нужно.

Sample Input 1:

1
25
Sample Output 1:

1 2 3 4 5 6 7 8 9 11 12 15 22 24
Sample Input 2:

20
30
Sample Output 2:

22 24'''

# a,b = int(input()),int(input())
# print(*[i for i in range(a, b + 1) if all(int(j) and not i % int(j) for j in str(i))])


# def check(num):
#     return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))
#
# a, b = int(input()), int(input())
# seq = range(a, b + 1)
# print(*list(filter(lambda x: check(x), seq)))


# print(*[i for i in range(int(input()), int(input())+1) if all([j!="0" and i%int(j)==0 for j in str(i) ]) and i %10!=0 ])


# a,b = int(input()),int(input())
# print(*[i for i in range(a,b+1) if all(int(j) and not i%int(j)  for j in str(i))])
