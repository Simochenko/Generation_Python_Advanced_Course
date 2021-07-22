'''Тема урока: вложенные словари, генераторы словарей
Вложенные словари
Генераторы словарей
Аннотация. Урок посвящен вложенным словарям и генераторам словарей.

Вложенные словари
Словари могут содержать другие словари, которые сами, в свою очередь, содержат словари, и так далее на любую глубину.
 Такие словари называются вложенными словарями (мы уже сталкивались с вложенными списками и кортежами). Вложенные
 словари – один из способов представления структурированной информации.

Создание вложенных словарей
Вложенный словарь создается как обычный, только каждое значение в нем – другой словарь.

Приведенный ниже код создает словарь для хранения информации о сотрудниках некоторой компании.

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
Тот же самый словарь info может быть создан по другому:

info = dict(emp1 = {'name': 'Timur', 'job': 'Teacher'},
            emp2 = {'name': 'Ruslan', 'job': 'Developer'},
            emp3 = {'name': 'Rustam', 'job': 'Tester'})
или

ids = ['emp1', 'emp2', 'emp3']

emp_info = [{'name': 'Timur', 'job': 'Teacher'},
            {'name': 'Ruslan', 'job': 'Developer'},
            {'name': 'Rustam', 'job': 'Tester'}]

info = dict(zip(ids, emp_info))
   Число уровней вложенности словарей неограниченно!

Обращение к элементам вложенного словаря
Для того, чтобы получить значения определенных элементов во вложенном словаре, необходимо указать их ключи в нескольких
 квадратных скобках, подобно тому, как мы получали значения во вложенных списках.

Приведенный ниже код:

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

print(info['emp1']['name'])
print(info['emp2']['job'])
выводит:

Timur
Developer
При попытке обращения по несуществующему ключу возникнет ошибка KeyError. Для того, чтобы избежать возникновения
такой ошибки, используйте словарный метод get(), который по умолчанию возвращает значение None если ключ отсутствует
в словаре.

Изменение вложенных словарей
Чтобы изменить значение определенного элемента во вложенном словаре, необходимо обратиться к его ключу и использовать
оператор присвоения (=).

Приведенный ниже код:

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

info['emp1']['job'] = 'Manager'

print(info['emp1'])
выводит:

{'name': 'Timur', 'job': 'Manager'}
Итерация по вложенным словарям
Итерации по вложенным словарям осуществляются как правило двумя циклами for (иногда достаточно одного цикла).

Приведенный ниже код:

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp in info:
    print('Employee ID:', emp)
    for key in info[emp]:
        print(key + ':', info[emp][key])
    print()
выводит:

Employee ID: emp1
name: Timur
job: Teacher

Employee ID: emp2
name: Ruslan
job: Developer

Employee ID: emp3
name: Rustam
job: Tester
Аналогичного результата можно было добиться с помощью метода items():

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp, inf in info.items():
    print('Employee ID:', emp)
    for key in inf:
        print(key + ':', inf[key])
    print()
Генераторы словарей
Пусть требуется создать словарь, ключами которого будут числа от 00 до 55, а значениями – квадраты ключей.

Для создания требуемого словаря можно использовать код:

squares = {}

squares[0] = 0
squares[1] = 1
squares[2] = 4
squares[3] = 9
squares[4] = 16
squares[5] = 25
или:

squares = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
или:

squares = {}

for i in range(5):
    squares[i] = i**2
Первые два способа слишком громоздкие и не подходят, когда чисел много. Третий способ полностью решает поставленную
задачу, однако его можно переписать в стиле Python с использованием генератора словаря:

squares = {i: i**2 for i in range(5)}
Общий вид генератора словаря следующий:

{ключ: значение for переменная in последовательность}

где переменная — имя некоторой переменной, последовательность — последовательность значений, которые она принимает
(любой итерируемый объект), ключ: значение — некоторое выражение, как правило, зависящее от использованной в
списочном выражении переменной, которой будут заполнены элементы словаря.

Примеры использования генератора словарей
Генераторы словаря могут выполнять итерации по любому итерируемому объекту: списки, кортежи, строки, словари.

1. Генератор словаря при итерировании по строке.

Приведенный ниже код:

dct = {c: c * 3 for c in 'ORANGE'}

print(dct)
выводит:

{'O': 'OOO', 'R': 'RRR', 'A': 'AAA', 'N': 'NNN', 'G': 'GGG', 'E': 'EEE'}
2. Для вычисления ключа и значения в генераторе словаря могут быть использованы выражения.

В следующем примере для вычисления ключа используется метод lower(), а для вычисления значения – метод upper().

Приведенный ниже код:

lst = ['ReD', 'GrEeN', 'BlUe']
dict = {c.lower(): c.upper() for c in lst}

print(dict)
выводит:

{'red': 'RED', 'green': 'GREEN', 'blue': 'BLUE'}
3. Извлечение из словаря элементов с определенными ключами.

Приведенный ниже код:

dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]

dict2 = {k: dict1[k] for k in selected_keys}

print(dict2)
выводит:

{0: 'A', 2: 'C', 5: 'F'}
Условия в генераторе словарей
В генераторах словарей можно использовать условный оператор.

Приведенный ниже код создает словарь, ключами которого являются четные числа от 00 до 99, а значениями – квадраты
ключей:

squares = {}
for i in range(10):
    if i % 2 == 0:
        squares[i] = i**2

print(squares)
Такой код можно переписать с помощью генератора словаря в виде:

squares = {i: i**2 for i in range(10) if i % 2 == 0}

print(squares)
Не забываем про возможность указания шага в функции range(). Предыдущий код можно записать и без условного оператора:
squares = {i: i**2 for i in range(0, 10, 2)}.

Генераторы вложенных словарей
Мы также можем использовать генераторы словарей для создания вложенных словарей:

Приведенный ниже код:

squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}

for value in squares.values():
    print(value)
выводит:

{0: 0}
{0: 0, 1: 1}
{0: 0, 1: 1, 2: 4}
{0: 0, 1: 1, 2: 4, 3: 9}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}'''

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i**2 for i in numbers}
# print(result)
import ast
import urllib

'''Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
colors, кроме тех, у которых значением является None.

Примечание. Выводить содержимое словаря result не нужно.'''

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8':
#     None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure',
#           'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand',
#           'c23': None}
#
# print({k:v for k, v in colors.items() if v != None})


# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {x: colors[x] for x in colors if colors[x]}


# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {key: colors[key] for key in colors if colors[key]}


'''Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря
 favorite_numbers , значения которых являются двухзначными числами.

Примечание. Выводить содержимое словаря result не нужно.'''

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
#
# result = {k:v for k, v in favorite_numbers.items() if 100>v>9}
# print(result)


# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {key: value for key, value in favorite_numbers.items() if value in range(10, 100)}


# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {key: value for key,value in favorite_numbers.items() if len(str(value))==2}

#
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {c: favorite_numbers[c] for c in favorite_numbers if 10 >= favorite_numbers[c] / 10 >= 1}


'''Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов
 словаря months , в которых ключ и значение поменялись местами.

Примечание. Выводить содержимое словаря result не нужно.'''
# months = {1: 'January', 2: 'February', 3 : 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9:
#         'September', 10: 'October', 11: 'November', 12: 'December'}


# result = {}
# for (k, v) in months.items():
#
#         result.setdefault(v,k)
# print(result)


# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {v: k for k, v in months.items()}


# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {key: value for value, key in months.items()}



# import ast
#
# s = "{'1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 34:car 3:island 88:power 7:box 17:star 101:ice'}"
# d = ast.literal_eval(s)
#
# print(d)

'''Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка 
numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1.

Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь

result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}
Примечание 2. Выводить содержимое словаря result не нужно. '''

# numbers = sorted([34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360])
# result ={i: [k for k in range(1, i + 1) if i % k == 0] for i in numbers}
# print(result)

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {n: [i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in numbers}


# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {i: [j for j in range(1, i+1) if i%j == 0] for i in numbers}


# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# div = [[i for i in range(1, j+1) if j % i == 0] for j in numbers]
# result = dict(zip(numbers, div))


'''Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет
 строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.

Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь

result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
Примечание 2. Для получения ASCII кода символа используйте функцию ord().

Примечание 3. Выводить содержимое словаря result не нужно.'''

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result ={i: [ord(k) for k in i] for i in words}
# print(result)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {word: [ord(ch) for ch in word] for word in words}


# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {k: [ord(i) for i in k] for k in words}

'''Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов 
словаря letters , за исключением тех, ключи которых есть в списке remove_keys.
Примечание. Выводить содержимое словаря result не нужно.'''

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
#            13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
#            24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {}
# for (k, v) in letters.items():
#     if k in remove_keys:
#         pass
#     else:
#         result.setdefault(k, v)
# print(result)


# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
#            12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
#            23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {i: j for i, j in letters.items() if i not in remove_keys}


# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
#            12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
#            23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {k: letters[k] for k in set(letters) - set(remove_keys)}


# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
#            12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
#            23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {key: letters[key] for key in (set(letters) - set(remove_keys))}

'''В переменной students хранится словарь, содержащий информацию о росте (в см) и весе (в кг) студентов.
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
students , где указан рост больше 167 см, а вес меньше 75 кг.
Примечание. Выводить содержимое словаря result не нужно.'''


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
#             'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
#             'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
#             'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result ={k:v for k, v in students.items() if students[k][0]>167 and students[k][1]<75}
#
# print(result)


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {name: data for name, data in students.items() if data[0] > 167 and data[1] < 75}




# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result =
# print(result)


'''Даны три списка student_ids, student_names, student_grades, содержащие информацию о студентах.

Дополните приведенный код, используя генератор, так чтобы получить список result, содержащий вложенные словари в 
соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].

Примечание 1. Для параллельной итерации по всем трем спискам одновременно можно использовать встроенную функцию zip().

Примечание 2. Выводить содержимое списка result не нужно.'''
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
#                  'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman',
#                  'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# result = [{x: {y: z}} for (x, y, z) in zip(student_ids, student_names, student_grades)]
# print(result)


# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = []
# for i in range(len(student_ids)):
#     a, b, c = student_ids[i], student_names[i], student_grades[i]
#     result.append({a: {b: c}})


# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{s: {student_names[i]: student_grades[i]}} for i, s in enumerate(student_ids)]


# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# st_ng = [{student_names[i]: student_grades[i]} for i in range(len(student_names))]
# result = [{student_ids[i]: st_ng[i]} for i in range(len(student_ids))]


'''Список tuples содержит кортежи, состоящие из трех чисел.

Дополните приведенный код, используя генератор, чтобы получить словарь result, в котором ключом является первый элемент
 каждого кортежа, а значением – кортеж из оставшихся двух элементов.

Примечание. Выводить содержимое словаря result не нужно.'''

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {x: tuple(y) for x, *y in tuples}
# print(result)


# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {i[0]: i[1:] for i in tuples}



# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {x[0]: (x[1], x[2]) for x in tuples}

'''Дополните приведенный код, используя генератор, так чтобы получить словарь result , в котором ключом будет 
позиция числа в списке numbers (начиная с 00), а значением – его квадрат.

Примечание. Выводить содержимое словаря result не нужно.'''

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i: numbers[i]**2 for i in range(len(numbers))}
# print(result)


# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {cnt: x ** 2 for cnt, x in enumerate(numbers)}

'''В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить 
словарь result , в котором числа будут ключами, а слова – значениями.

Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).

Примечание 2. Выводить содержимое словаря result не нужно.'''
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 34:car 3:island 88:power 7:box 17:star 101:ice'
#
# result={}
# result=(dict((int(k.strip()),v.strip()) for k,v in (p.split(':') for p in s.split(' '))))
# print(result)
#
#
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 34:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(k): v for k, v in [s.split(':') for s in s.split()]}


# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 34:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(i.split(':')[0]): i.split(':')[1] for i in s.split(' ')}


# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 34:car 3:island 88:power 7:box 17:star 101:ice'
# result = {int(i[0]): i[1] for i in [j.split(':') for j in s.split()]}



# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# result = {k:v for k, v in my_dict.items() if  }
# print(result)
#
# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# print(*emails, sep = '\n')



# def compliment(Nucleotide):
#     comp = []
#     for i in Nucleotide:
#         if i == "T":
#             comp.append("A")
#         if i == "A":
#             comp.append("U")
#         if i == "G":
#             comp.append("C")
#         if i == "C":
#             comp.append("G")
#
#     return ''.join(comp)
#
# print(compliment(input()))


# def coun(x):
#     dct[x] = dct.get(x, 0) + 1
#     return dct[x]
#
#
# dct = {}
# print(*[coun(k) for k in input().split()])

# def count_letters(word):
#   count = {}
#   for letter in word:
#     if letter not in count: count[letter] = 0
#     count[letter] += 1
#   return count
#
#
#
# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
#
# def score_word(word):
#   return sum([score[c] for c in word])
#
# print(score_word(input().lower()))


# result=(dict[{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# def merge(values):
#     super_dict = {}
#     for d in result:
#         for k, v in d.iteritems():  # d.items() in Python 3+
#             super_dict.setdefault(k, []).append(v)
# print(merge())

# from collections import defaultdict
# customer_dic =defaultdict(lambda: defaultdict(int))
# while 1:
#     try:
#         in_string =str(input())
#     except EOFError:
#         break
#     if not in_string:
#         break
#
#     customer, product, product_quantity = in_string.split()
#     customer_dic[customer][product]=customer_dic[customer][product]+int(product_quantity)
#
# for i in sorted(customer_dic):
#     print(i + ':')
#     for j in sorted(customer_dic[i]):
#         print(j, customer_dic[i][j])



# customers = {}
#
# for line in  range(int(input())):
#     name, good, qty = input().strip().split()
#     if name not in customers:
#         customers[name] = {good: int(qty)}
#     elif good not in customers[name]:
#         customers[name].update({good: int(qty)})
#     else:
#         customers[name].update({good: customers[name].get(good) + int(qty)})
#
#
# for name in sorted(customers):
#     print(name + ':')
#     for good in sorted(customers[name]):
#         print(good, customers[name][good])

# from collections import defaultdict
#
# # dicts = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
# def merge(values):
#     super_dict = defaultdict(set)  # uses set to avoid duplicates
#
#     for d in dicts:
#         for k, v in d.items():  # use d.iteritems() in python 2
#             super_dict[k].add(v)
# print(merge(i))

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

# def build_query_string(params):
#     query = ''
#     for key in params.keys():
#         query += str(key) + '=' + str(params[key])
#     return query
# print(build_query_string({"per": 14, "page": 7}))

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# # res=dict((k, v) for k, v in my_dict.items() if all(x <20 for x in v))
#
#
# print(dict((k, v) for k, v in my_dict.items() if  all(x < 20 for x in v)))

