'''Что будет выведено на экран в результате выполнения следующей программы?
'''
# numbers = [1, 2, 5, 3, 4]
# numbers.sort(key=lambda x: -x)
# print(numbers)

#[5, 4, 3, 2, 1]


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda: True, primes))
# print(result)   # error


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda x: True, primes))
# print(result) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# print(full_name('ben', 'affleck')) # Full name: Ben Affleck


'''Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является неотрицательным числом (целым или вещественным) и False в противном случае.

Примечание 1. Следующий программный код:

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))
должен выводить:

False
True
False
False
True
False
False
True
Примечание 2. Неотрицательные числа — это положительные числа и число нуль.

Примечание 3. Вызывать анонимную функцию не нужно.'''

# is_non_negative_num = lambda x: x.replace('.', '', 1).isdigit()
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))


# is_non_negative_num = lambda x: bool(sum(c in '0123456789.' for c in x) == len(x) and x.count('.') <= 1)

# is_non_negative_num = lambda s: s.count('.') <= 1 and set(s) <= set('.1234567890')


# import re
# is_non_negative_num = lambda n: bool(re.match(r'\d+$|\d+\.?\d+$', n))
#
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))



# is_non_negative_num = lambda x: x.count('.') < 2 and x.replace('.', '').isdigit() and float(x) >= 0


'''Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.

Примечание 1. Следующий программный код:

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
должен выводить:

False
True
True
True
True
False
False
True
Примечание 2. Используйте вспомогательную функцию из прошлого степа.

Примечание 3. Вызывать анонимную функцию не нужно.'''

# is_num = lambda x: bool(x.replace('.', '', 1).lstrip('-').isdigit() and not '.-' in x)

# is_num = lambda x: x.lstrip("-").replace(".", "", 1).isdecimal()


# is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
#
# is_num = lambda q: is_non_negative_num(q[1:]) if q[0] == '-' else is_non_negative_num(q)
#
#
# import re
# is_num = lambda n: re.match(r'-?\d*\.?\d+$', n) is not None
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))

'''Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words, имеющие 
длину ровно 66 символов. Слова следует вывести в алфавитном порядке на одной строке, разделив символом пробела.

Примечание. Используйте анонимную функцию в качестве критерия фильтрации.'''

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
#          'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow',
#          'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday',
#          'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept',
#          'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# print(*sorted(list(filter(lambda x: len(x) == 6, words))))

'''Напишите программу, которая с помощью встроенных функций map() и filter() удаляет из списка numbers все нечетные
 элементы, большие 4747, а все четные элементы нацело делит на два (целочисленное деление – //). Полученные числа 
 следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.

Примечание. Используйте анонимную функцию в качестве критерия фильтрации.'''


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27,
#            57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29,
#            88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# print(*list(map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: (x > 47 and x % 2 == 0) or x < 47, numbers))))


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80,
#            80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83,
#            27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66,
#            29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# print(*map(lambda y: y >> (~y & 1), filter(lambda x: ~x & 1 or x < 48, numbers)))


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# print(*map(lambda x: x if x % 2 == 1 else x // 2 , filter(lambda x: '' if x % 2 == 1 and x > 47 else x, numbers)), sep=' ')

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# print(*map(lambda n: n >> (not n % 2), filter(lambda n: n < 48 or not n % 2, numbers)))


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# print(*map(lambda x: [x // 2, x][x % 2], filter(lambda x: x < 48 or not x % 2, numbers)))


'''Список data содержит информацию о численности населения некоторых штатов США. Напишите программу сортировки по 
убыванию списка data на основании последнего символа в названии штата. Затем распечатайте элементы этого списка, каждый 
на новой строке в формате:


<название штата>: <численность населения>

Vermont: 626299
Massachusetts: 7029917
...
Примечание 1. Сортировка производится в лексикографическом порядке (по алфавиту) по убыванию на основании последнего
 символа в названии штата. При этом, если два штата имеют одинаковый последний символ, следует сохранить их 
 взаиморасположение в начальном списке.

Примечание 2. Используйте анонимную функцию в качестве критерия сортировки.'''

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# data.sort(key= lambda x: x[-1][-1], reverse=True)
# for el in data:
#     print(f'{el[1]}: {el[0]}')
#

# data = [(19542209, 'New York') ,(4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# print(*map(lambda r: f'{r[1]}: {r[0]}', sorted(data, key=lambda r: r[1][-1], reverse=True)), sep='\n')


# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# for i in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f'{i[1]}: {i[0]}')


# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# data=list(sorted(data, key=lambda d: d[1][-1], reverse=True))
# for el in data:
#     print(el[1]+": " + str(el[0]))

'''Список data содержит слова на русском языке. Напишите программу его сортировки по возрастанию длины слов, а
 затем в лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом 
 пробела.

Примечание 1. Используйте анонимную функцию в качестве критерия сортировки.

Примечание 2. Если длина слов совпадает, сортировать нужно в лексикографическом порядке.'''

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# print(*sorted(data, key=lambda x: (len(x), x)))

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# print(*sorted(data, key=lambda x: f'o_O{len(x)}{x}'))


'''Список mixed_list содержит целочисленные и строковые значения. Напишите программу, которая с помощью встроенной функции max() находит и выводит наибольшее числовое значение в указанном списке.

Примечание 1. Для решения задачи используйте анонимную функцию и необязательный аргумент key  функции max().

Примечание 2. Обратите внимание, что сравнивать числа и строки нельзя.'''


# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
# digits = list(filter(lambda x: type(x) == int, mixed_list))
# print(max(digits))


# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
# print(max(mixed_list, key=lambda x: (isinstance(x, int), x)))

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
# print(max(mixed_list, key=lambda x: (0, x)[type(x) == int]))


'''Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки по неубыванию 
значений элементов, при этом числа должны следовать до строк.  Элементы отсортированного списка выведите на одной
 строке, разделив символом пробела.

Примечание 1. Для решения задачи используйте анонимную функцию и необязательный аргумент key  функции sorted().

Примечание 2. Если бы список mixed_list содержал значения:

mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
то результатом работы программы должно быть:

0 1 3 5 8 a aab ab ac c'''

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
# print(*sorted(mixed_list, key=lambda x: ((isinstance(x, str), x), (isinstance(x, int), x))))

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# print(*sorted(mixed_list, key=str))


# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# print(*sorted(mixed_list, key=lambda x: (isinstance(x, str), x)))


'''Противоположный цвет
В цветовой схеме RGB цвета задаются с помощью трех компонентов:

R — интенсивность красной составляющей цвета;
G — интенсивность зеленой составляющей цвета;
B — интенсивность синей составляющей цвета.
Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B). Считается, что такие цвета хорошо гармонируют друг с 
другом.

Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета. 

Формат входных данных
На вход программе подается строка, содержащая три целых неотрицательных числа, компоненты R, G и B начального цвета, 
 разделенные символом пробела.

Формат выходных данных
Программа должна вывести три компонента R, G и B противоположного цвета, разделенные символом пробела.

Примечание. Попробуйте решить задачу в одну строку с помощью встроенной функции map().



Sample Input 1:

244 11 120
Sample Output 1:

11 244 135
Sample Input 2:

0 0 0
Sample Output 2:

255 255 255'''

# color = list(map(int, input().split()))
# print(*map(lambda x: 255 - x, color))

# print(*map(lambda c: 255 - int(c), input().split()))


# print(*[255 - int(i) for i in input().split()])


# print(*map(int.__sub__, (255,) * 3, map(int, input().split())))


'''Значение многочлена 🌶️
Многочленом степени nn называется выражение вида 
a_nx^n + a_{n-1}x^{n-1}+\ldots + a_2x^2+a_1x+a_0
a 
n
​
 x 
n
 +a 
n−1
​
 x 
n−1
 +…+a 
2
​
 x 
2
 +a 
1
​
 x+a 
0
​
 
где a_n, \, a_{n-1}, \ldots , a_2, \, a_1,\, a_0a 
n
​
 ,a 
n−1
​
 ,…,a 
2
​
 ,a 
1
​
 ,a 
0
​
  — коэффициенты многочлена (a_n \neq 0a 
n
​
 

=0).

На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число xx
 на второй строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении xx.

Формат входных данных
На вход программе на первой строке подаются коэффициенты многочлена (целые числа), разделенные символом пробела и
 целое число xx на второй строке.

Формат выходных данных
Программа должна вывести одно число — значение указанного многочлена при заданном значении xx.

Примечание 1. Первый тест задает многочлен 2x^2+4x+32x 
2
 +4x+3, второй тест задает многочлен x^6+2x^5+3x^4+4x^3+5x^2+6x+7x 
6
 +2x 
5
 +3x 
4
 +4x 
3
 +5x 
2
 +6x+7.

Примечание 2. Решение задачи необходимо оформить в виде функции evaluate(coefficients, x), которая принимает список
 коэффициентов и значение аргумента. Функция evaluate() должна быть реализована на основе встроенных функций map(), 
 filter() и reduce().

Примечание 3. Не забудьте вызвать функцию evaluate(), чтобы вывести результат 😀.

Sample Input 1:

2 4 3
10
Sample Output 1:

243
Sample Input 2:

1 2 3 4 5 6 7
1
Sample Output 2:

28'''






'''Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает 
значение True, если он делится без остатка на 1919 или на 1313 и False в противном случае.

Примечание 1. Следующий программный код:

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))
должен выводить:

True
True
False
False
True
Примечание 2. Вызывать анонимную функцию не нужно.'''

# func = lambda x: x%19==0 or x%13==0


# func = lambda x: not (x % 19 and x % 13)

# func = lambda x: x%19==0 or x%13==0

# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

'''Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
 значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен)
  и False в противном случае.

Примечание 1. Следующий программный код:

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
должен выводить:

False
False
True
False
False
True
Примечание 2. Вызывать анонимную функцию не нужно.'''


# func = lambda x: x[-1:].upper()=='A'and x.upper()[0:1]=='A'
#
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))

# func=lambda x: x[0] in 'aA' and x[-1] in 'aA'

# func = lambda x: x[0].lower() == x[-1].lower() == 'a'

# func = lambda x: (x[0] + x[-1]).lower() == 'aa'

# func = lambda x: x.lower().startswith('a') and x.lower().endswith('a')