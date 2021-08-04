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