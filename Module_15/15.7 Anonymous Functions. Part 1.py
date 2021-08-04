'''Тема урока: анонимные функции
Определение анонимных функций
Условный оператор в теле анонимной функции
Передача аргументов в анонимную функцию
Ограничения анонимных функций
Аннотация. Урок посвящен работе с анонимными функциями.

В языке Python можно создавать функции с уникальными именами, но иногда имя не требуется. Например, функциям,
 использующимся единственный раз. В таких случаях применяют анонимные функции.

Анонимные функции
Помимо стандартного определения функции, состоящего из ее заголовка с ключевым словом def и блока кода – тела
 функции, в Python можно создавать короткие однострочные функции с использованием оператора lambda. Это анонимные
  функции или лямбда-функции.

   Анонимные функции – функции с телом, но без имени.

Общий формат определения анонимной функции: lambda список_параметров: выражение.

Тут список_параметров – список параметров через запятую, выражение – значение, либо код, дающий значение.

   Параметры анонимных функций, в отличие от обычных, не нужно заключать в скобки.

Следующие два определения функций эквивалентны:

def standard_function(x):            #  стандартное объявление функции
    return x*2

lambda_function = lambda x: x*2      #  объявление анонимной функции
Приведенный ниже код:

print(standard_function(7))
print(lambda_function(7))
выводит:

14
14
Рассмотрим еще примеры. Приведенный ниже код:

f1 = lambda: 10 + 20               # функция без параметров
f2 = lambda х, у: х + у            # функция с двумя параметрами
f3 = lambda х, у, z: х + у + z     # функция с тремя параметрами

print(f1())
print(f2(5, 10))
print(f3(5, 10, 30))
выводит:

30
15
45
Когда применение анонимных функций оправдано:

однократное использование функции;
передача функций в качестве аргументов другим функциям;
возвращение функции в качестве результата другой функции.
Однократное использование функции
В одном из прошлых уроков нам приходилось сортировать список кортежей. Как мы уже знаем, встроенная  функция
sorted() (или списочный метод sort()) сортируют по первым значениям кортежей, а в случае их совпадения, по вторым
и т.д. Для сортировки, отличной от стандартной нам приходилось создавать отдельные функции-компараторы для
сравнения элементов:

def compare_by_second(point):
    return point[1]


def compare_by_sum(point):
    return point[0] + point[1]


points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа
Очевидно, что такие функции как compare_by_second() и compare_by_sum() не особо нужны вне контекста сортировки,
поэтому логично их заменить на анонимные функции:

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points, key=lambda point: point[1]))                 # сортируем по второму значению кортежа
print(sorted(points, key=lambda point: point[0] + point[1]))      # сортируем по сумме элементов кортежа
   Название аргумента point в анонимной функции можно заменить на любое другое.

Передача анонимных функций в качестве аргументов другим функциям
Функции высшего порядка map(), filter() и reduce() идеально подойдут для демонстрации удобства анонимных функций в
качестве аргументов других функций.

Теперь нет необходимости делать преобразующую элементы функцию отдельно определенной именованной функцией.

Приведенный ниже код:

numbers = [1, 2, 3, 4, 5, 6]

new_numbers1 = list(map(lambda x: x+1, numbers))      #  увеличиваем на 1
new_numbers2 = list(map(lambda x: x*2, numbers))      #  удваиваем
new_numbers3 = list(map(lambda x: x**2, numbers))     #  возводим в квадрат

print(new_numbers1)
print(new_numbers2)
print(new_numbers3)
выводит:

[2, 3, 4, 5, 6, 7]
[2, 4, 6, 8, 10, 12]
[1, 4, 9, 16, 25, 36]
Приведенный ниже код:

strings = ['a', 'b', 'c', 'd', 'e']
numbers = [3, 2, 1, 4, 5]

new_strings = list(map(lambda x, y: x*y, strings, numbers))

print(new_strings)
выводит:

['aaa', 'bb', 'c', 'dddd', 'eeeee']
Рассмотрим примеры использования анонимных функций в качестве аргумента функции filter().

Приведенный ниже код:

numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]

positive_numbers = list(filter(lambda x: x > 0, numbers))      #  положительные числа
large_numbers = list(filter(lambda x: x > 50, numbers))        #  числа, большие 50
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))     #  четные числа

print(positive_numbers)
print(large_numbers)
print(even_numbers)
выводит:

[2, 4, 10, 30, 50, 100, 90]
[100, 90]
[2, 4, 0, -20, 10, 30, -40, 50, 100, 90]
Приведенный ниже код:

words = ['python', 'stepik', 'beegeek', 'iq-option']

new_words1 = list(filter(lambda w: len(w) > 6, words))    #  слова длиною больше 6 символов
new_words2 = list(filter(lambda w: 'e' in w, words))      #  слова содержащие букву e

print(new_words1)
print(new_words2)
выводит:

['beegeek', 'iq-option']
['stepik', 'beegeek']
Рассмотрим примеры использования анонимных функций в качестве аргументов функции reduce().

Приведенный ниже код:

from functools import reduce

words = ['python', 'stepik', 'beegeek', 'iq-option']
numbers = [1, 2, 3, 4, 5, 6]

summa = reduce(lambda x, y: x + y, numbers, 0)
product = reduce(lambda x, y: x * y, numbers, 1)
sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')

print(summa)
print(product)
print(sentence)
выводит:

21
720
Everyone loves python loves stepik loves beegeek loves iq-option
Возвращение функции в качестве результата другой функции
Анонимные функции могут быть результатом работы других функций.

Приведенный ниже код по значениям a, \, b, \, ca,b,c строит и возвращает квадратный трехчлен:

def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom
Такой код можно переписать так:

def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c
Этот пример показывает, что анонимные функции являются замыканиями: возвращаемая функция запоминает значения
переменных a, b, c из внешнего окружения.

Условный оператор в теле анонимной функции
В теле анонимной функции не получится выполнить несколько действий и не получится использовать многострочные
 конструкции вроде циклов for и while. Однако можно использовать тернарный условный оператор.

Приведенный ниже код:

numbers = [-2, 0, 1, 2, 17, 4, 5, 6]

result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))

print(result)
выводит:

['even', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
Общий вид тернарного условного оператора в теле анонимной функции выглядит так:

значение1 if условие else значение2
Если условие истинно, возвращается значение1 , если нет – значение2.

Анонимные функции не могут содержать многострочных конструкций, зато их легко читать. Этого сложно было бы добиться,
 разреши авторы "многострочные" анонимные функции.

Передача аргументов в анонимную функцию
Как и обычные функции, определенные с помощью ключевого слова def , анонимные функции поддерживают все способы передачи
аргументов:

позиционные аргументы;
именованные аргументы;
переменный список позиционных аргументов (*args);
переменный список именованных аргументов (**kwargs);
обязательные аргументы (*).
Приведенный ниже код:

f1 = lambda x, y, z: x + y + z
f2 = lambda x, y, z=3: x + y + z
f3 = lambda *args: sum(args)
f4 = lambda **kwargs: sum(kwargs.values())
f5 = lambda x, *, y=0, z=0: x + y + z


print(f1(1, 2, 3))
print(f2(1, 2))
print(f2(1, y=2))
print(f3(1, 2, 3, 4, 5))
print(f4(one=1, two=2, three=3))
print(f5(1))
print(f5(1, y=2, z=3))
выводит:

6
6
6
15
6
1
6
Ограничения анонимных функций
Особенности и ограничения анонимных функций в Python:

анонимная функция может содержать только выражение, и не может включать в свое тело операторы;
в теле анонимной функции такие операторы, как return, pass, assert или raise, вызовут исключение SyntaxError;
анонимная функция пишется как одна строка исполнения;
анонимная функция может быть немедленно вызвана 🤓.
Примечания
Примечание 1. Интересная особенность анонимных функций (лямбда-функций) – они являются выражениями. После определения
лямбда-функции ее можно сразу же вызвать.

Приведенный ниже код:

print((lambda х, у: х + у)(5, 10))     # 5 + 10
print(1 + (lambda x: x*5)(10) + 2)     # 1 + 50 + 2
выводит:

15
53
   Анонимные функции можно конструировать и тут же вызывать. На практике это редко применяется.

Примечание 2. В лямбда исчислении, часто применяемом в разработке языков программирования, все функции — анонимные,
 поэтому анонимные функции во многих языках тоже называют "лямбдами" или "лямбда-функциями".

Примечание 3. В Python анонимные функции — лишь сокращенная запись функции, поэтому приведенный ниже код:

f = lambda x: x + 1
print(type(f))
выводит:

<class 'function'>
То есть, анонимные функции имеют такой же тип, как и обычные функции.

Примечание 4. Анонимные функции очень часто используются вместе со встроенными функциями map(), filter(), reduce(),
sorted(), max(), min() и т.д.'''


# func = lambda x, y: x ** y
# print(func(5, 3))


# func = lambda x, y: x + y
# print(func('5', '3'))


# users = [('Timur', 28), ('Ruslan', 21), ('Roman', 30), ('Soltan', 24), ('Robert', 1)]
# result = max(users, key=lambda x: x[1])
# print(result)

#
# from functools import reduce
#
# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = filter(lambda x: x % 2 == 1, obj)
#
# result = reduce(lambda x, y: x + y, obj, 0)
#
# print(result)

# result = list(map(lambda x: x.split(), ['a', 'a b', 'a b c']))
#
# print(result)
# high_ord_func = lambda x, func: x + func(x)
#
# result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)
#
# print(result)


# dict1 = {'x': 1}
# dict2 = {'y': 2}
# dict3 = {'x': 3, 'y': 4}
#
# result = list(filter(lambda d: 'x' in d.keys(), [dict1, dict2, dict3]))
#
# print(result)

'''Требовалось написать программу, которая:

преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
фильтрует список words  и оставляет только палиндромы длиной более 44 символов;
находит произведение чисел из списка numbers.
Программист торопился и написал программу неправильно. Доработайте его программу.'''


# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num, 1), map(lambda num: num ** 2, floats)))
# filter_result = list(filter(lambda name: len(name) > 4, filter(lambda name: name == name[::-1], words)))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)



# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(round, list(map(lambda num: num**2, floats)), [1]*len(floats)))
# filter_result = list(filter(lambda name: len(name)>4 and name==name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


'''Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном 
порядке список primary городов с населением более 10\,000\, 00010000000 человек, в формате:

Cities: Beijing, Buenos Aires, ...
Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование встроенных функций filter(), map(), 
sorted() и reduce(), однако лучше сделать это задание честно 😃.

Примечание 2. Ставить запятую в конце вывода не нужно.'''

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# primary_filt = list(filter(lambda x: x[1] > 10000000, filter(lambda x: x[2] == 'primary', data)))
# primary_filt.sort(key=lambda x: x[0])
# print(str(reduce(lambda x, y: x + y[0] + ', ', primary_filt, 'Cities: '))[:-2])


# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
# s = list(filter(lambda x:x[1] > 10_000_000 and x[2] == 'primary', data))
# s = ', '.join(sorted(list(map(lambda x: x[0], s))))
# print(f'Cities: {s}')


#
# from functools import reduce
#
# data=[['Tokyo', 35676000, 'primary'],
#       ['New York', 19354922, 'nan'],
#       ['Mexico City', 19028000, 'primary'],
#       ['Mumbai', 18978000, 'admin'],
#       ['Sao Paulo', 18845000, 'admin'],
#       ['Delhi', 15926000, 'admin'],
#       ['Shanghai', 14987000, 'admin'],
#       ['Kolkata', 14787000, 'admin'],
#       ['Los Angeles', 12815475, 'nan'],
#       ['Dhaka', 12797394, 'primary'],
#       ['Buenos Aires', 12795000, 'primary'],
#       ['Karachi', 12130000, 'admin'],
#       ['Cairo', 11893000, 'primary'],
#       ['Rio de Janeiro', 11748000, 'admin'],
#       ['Osaka', 11294000, 'admin'],
#       ['Beijing', 11106000, 'primary'],
#       ['Manila', 11100000, 'primary'],
#       ['Moscow', 10452000, 'primary'],
#       ['Istanbul', 10061000, 'admin'],
#       ['Paris', 9904000, 'primary']]
#
# cities = filter(lambda city: city[1] > 10 ** 7 and city[2] == 'primary', data)
# cities = map(lambda city: city[0], cities)
# cities = sorted(cities)
# cities = 'Cities: ' + reduce(lambda city1, city2: f'{city1}, {city2}', cities)
#
# print(cities)


#
# from functools import reduce
#
# data=[['Tokyo', 35676000, 'primary'],
#       ['New York', 19354922, 'nan'],
#       ['Mexico City', 19028000, 'primary'],
#       ['Mumbai', 18978000, 'admin'],
#       ['Sao Paulo', 18845000, 'admin'],
#       ['Delhi', 15926000, 'admin'],
#       ['Shanghai', 14987000, 'admin'],
#       ['Kolkata', 14787000, 'admin'],
#       ['Los Angeles', 12815475, 'nan'],
#       ['Dhaka', 12797394, 'primary'],
#       ['Buenos Aires', 12795000, 'primary'],
#       ['Karachi', 12130000, 'admin'],
#       ['Cairo', 11893000, 'primary'],
#       ['Rio de Janeiro', 11748000, 'admin'],
#       ['Osaka', 11294000, 'admin'],
#       ['Beijing', 11106000, 'primary'],
#       ['Manila', 11100000, 'primary'],
#       ['Moscow', 10452000, 'primary'],
#       ['Istanbul', 10061000, 'admin'],
#       ['Paris', 9904000, 'primary']]
#
# data1 = list(filter(lambda x: x[1] > 10**7 and x[2] == 'primary', data))
# data2 = reduce(lambda x, y: x + y[0] + ', ', sorted(data1), 'Cities: ' )
# print(data2[:-2])