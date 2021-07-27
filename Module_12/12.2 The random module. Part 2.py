'''Тема урока: модуль random
Метод shuffle()
Метод choice()
Метод sample()
Модуль string
Аннотация. Урок посвящен модулю random, в частности, методам работы с последовательностями.

Метод shuffle()
Метод shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.

Следующий код перемешивает список numbers случайным образом, а затем выводит его содержимое:

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)
Результатом работы такого кода может быть:

[4, 7, 8, 1, 2, 3, 6, 5]
Метод choice()
Метод choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один случайный элемент.

Следующий код выводит по одному случайному элементу из строки 'BEEGEEK', списка [1, 2, 3, 4] и кортежа
('a', 'b', 'c', 'd'):

import random

print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(('a', 'b', 'c', 'd')))
Результатом работы такого кода может быть:

E
3
c
Метод sample()
Метод sample() принимает два обязательных аргумента: первый – список (строка, кортеж, множество), второй – количество
случайных элементов. Возвращает список из указанного количества уникальных (имеющих разные индексы) случайных элементов.

Результатом работы кода:

import random

numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))
может быть:

[9]
[12, 5]
[9, 2, 8]
[12, 8, 9, 5, 2]
Количество случайных элементов не должно превышать длину исходного списка (строки). Следующий код:

import random

numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 6))
приведет к ошибке:

ValueError: Sample larger than population or is negative
Модуль string
Встроенный модуль string раньше использовался для расширения стандартных возможностей (функционала) строкового типа
данных str. На текущий момент все функции из модуля string переехали в методы строкового типа данных str, однако в
 модуле string остались удобные константные строки, которые можно использовать при решении задач.

Приведенный ниже код:

import string

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
выводит:

abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
0123456789abcdefABCDEF
01234567
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c
Примечания
Примечание 1. Помимо рассмотренных в уроке методов, модуль random содержит много дополнительных методов. Подробнее о
модуле random можно почитать в документации.'''
from random import random

'''IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.

Примечание 1. Пример правильного (неправильного) IP адреса:

192.168.5.250        # правильный
199.300.521.255      # неправильный
Примечание 2. Вызывать функцию generate_ip() не нужно, требуется только реализовать.'''

# from random import randint
#
#
# def generate_ip():
#     a = randint(0, 255)
#     b = randint(0, 255)
#     c = randint(0, 255)
#     d = randint(0, 255)
#     return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
#
#
# print(generate_ip())


# from random import randint
#
# def generate_ip():
#     return f'{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}'

# from random import choice
#
# def generate_ip():
#     return '.'.join(str(choice(range(256))) for _ in range(4))

# import random
# def generate_ip():
#     return '.'.join([str(random.randint(1, 225)) for _ in '1234'])

'''Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква 
английского алфавита, Number – число от 00 до 9999 (включительно).

Напишите функцию generate_index(), которая с помощью модуля randomгенерирует и возвращает случайный корректный 
почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный
Примечание 2. Обратите внимание на символ _ в почтовом индексе.

Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.'''


# import string
# import random
#
#
# def generate_ip():
#    a = random.choice(string.ascii_uppercase)
#    b = random.choice(string.ascii_uppercase)
#    c = random.randint(0, 100)
#    d = random.randint(0, 100)
#    return (str(a)  + str(b) + str(c) + '_'  + str(d)+str(b)  + str(a))
# print(generate_ip())

# from random import choice, randint
# from string import ascii_uppercase as letter
#
# def generate_index():
#     return f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}{choice(letter)}{choice(letter)}'


# import random
# import string
# def generate_index():
#     return(f"{''.join(random.sample(string.ascii_uppercase,2))}{random.randint(1,99)}_{random.randint(1,99)}{''.join(random.sample(string.ascii_uppercase,2))}")
#
#
# from random import choice, randrange
# from string import ascii_uppercase
#
# def generate_index():
#     n1, n2 = (randrange(100) for i in range(2))
#     a, b, c, d = (choice(ascii_uppercase) for i in range(4))
#     return (f'{a}{b}{n1}_{n2}{c}{d}')

# from random import sample
# from string import ascii_uppercase,digits
# def generate_index():
#     return ''.join(sample(ascii_uppercase,2)+sample(digits,2)+['_']+sample(digits,2)+sample(ascii_uppercase,2))
#
# import random
# import string
#
# def generate_index():
#     idx = []
#     idx.append(''.join(random.sample(string.ascii_uppercase, 2)))
#     idx.append(str(random.choice(range(100))))
#     idx.append('_')
#     idx.append(str(random.choice(range(100))))
#     idx.append(''.join(random.sample(string.ascii_uppercase, 2)))
#
#     return ''.join(idx)

'''Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы
 (двумерного списка).

Примечание. Выводить содержимое матрицы не нужно.'''

# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# random.shuffle(matrix)
# print(matrix)


# import random as rnd
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# n, m, lst = len(matrix), len(matrix[0]), sum(matrix, [])
# rnd.shuffle(lst)
# matrix = [[lst[i * m + j] for j in range(m)] for i in range(n)]
# print(matrix)

# import random
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# random.shuffle(matrix)
# for row in matrix:
#     random.shuffle(row)

# from random import *
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# shuffle(matrix)
# [shuffle(i) for i in matrix]


'''Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит
 их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 7 цифр;
все 100 лотерейных билетов должны быть различными.'''

# from random import sample
# print(*map('{}'.format,(sample(range(999999,10000000), 100))),sep='\n')


# from random import sample as r
# print(*r(range(int(1e6), int(1e7)), 100), sep='\n')

# from random import randint
# s=set()
# while len(s)!=100:
#     s.add(randint(1000000,9999999))
# print(*s,sep='\n')

# import random
# set_tickets=set()
# while len(set_tickets)<100:
#     set_tickets.add(random.randint(1000000,9999999))
# [print(i) for i in set_tickets]

#
# import random
#
# cet = set()
# while len(cet) != 100:
#     cet.add(random.randint(1000000, 9999999))
# print(*cet, sep='\n')


'''Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

Например, слова пила и липа или пост и стоп – анаграммы.

Напишите программу, которая считывает одно слово и генерирует с помощью модуля random его случайную анаграмму.

Примечание. Обратите внимание на то, что метод shuffle() работает со списком, а не со строкой.'''


# sentence = input()
# sentence = sentence.split()
#
# new_sentence = ''
# for word in sentence:
#     new_sentence += word[::-1] + ' '
#
# print(new_sentence)


# from random import sample as S
# anagram = input()
# print(''.join(S(anagram, len(anagram))))

# import random as R
# st = [i for i in input()]
# R.shuffle(st)
# print(*st, sep='')

# import random
# l = list(input())
# random.shuffle(l)
# print(''.join(l))


# from random import shuffle as sh
# word = input()
# result = list(word)
#
# while result == list(word):
#     sh(result)
# print(*result, sep='')


# from random import shuffle
# word = [i for i in input()]
# shuffle(word)
# print(''.join(word))


'''Тайный друг
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе 
с ним решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число nn – общее количество учеников. Далее идут nn строк, содержащих 
имена и фамилии учеников.

Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного
 друга, разделённые дефисом.

Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть тайным другом для 
нескольких учеников.

Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны и другие способы выбора тайных друзей.

Для отладки кода 🟡
Sample Input 1:

3
Светлана Зуева
Аркадий Белых
Борис Боков
Sample Output 1:

Светлана Зуева - Борис Боков
Аркадий Белых - Светлана Зуева
Борис Боков - Аркадий Белых
Sample Input 2:

5
Владимир Смолов
Тагир Хан
Давид Лавров
Арина Приходько
Глеб Анисимов
Sample Output 2:

Владимир Смолов - Тагир Хан
Тагир Хан - Арина Приходько
Давид Лавров - Глеб Анисимов
Арина Приходько - Владимир Смолов
Глеб Анисимов - Давид Лавров
Sample Input 3:

2
Руслан Адашев
Святослав Герасимов
Sample Output 3:

Руслан Адашев - Святослав Герасимов
Святослав Герасимов - Руслан Адашев'''

# group = []
# x1 = 1
# countStudents = int(input())
#
# for times in range(0, countStudents):
#     students = input()
#     group.append(students)
#
# for main in range(0, len(group)):
#     if main == len(group) - 1:
#         print(group[main], ' - ', group[0])
#     else:
#         print(group[main], ' - ', group[x1])
#         x1 += 1


# from random import choice as r
#
# p = [input() for _ in range(int(input()))]
# f = set(p)
# for s in p:
#     c = r(list(f - {s}))
#     print(s + ' - ' + c)
#     f -= {c}

# students = [input() for _ in range(int(input()))]
# friends = students[:]
# friends.insert(0, friends.pop())
#
# for student, friend in zip(students, friends):
#     print(f'{student} - {friend}')


# import random
# l = [input() for i in range(int(input()))]
# random.shuffle(l)
# for i in range(len(l)):
#     print(f"{l[i]} - {l[(i + 1) % len(l)]}")


# from random import shuffle
# l = [input() for _ in range(int(input()))]
# r = l[:]
# while any(a == b for a, b in zip(l, r)):
#     shuffle(r)
# for a, b in zip(l, r):
#     print(a, '-', b)


'''Генератор паролей 1
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных 
и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Формат входных данных
На вход программе подаются два числа nn и mm, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем
 регистре.

Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length 
символов.
Примечание 4. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей.

Для отладки кода 🟡
Sample Input 1:

9
7
Sample Output 1:

YbykdW8
heEWSyL
MDxYCzf
syWRujr
mFGBYNJ
bhmg5ip
2XmPgsx
hy7UMVs
JzKPyBw'''


# import random
#
# chars = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
#
# number = int(input())
# length = int(input())
# for n in range(number):
#     password =''
#     for i in range(length):
#         password += random.choice(chars)
#     print(password)

# import string, random
#
# def generate_password(length):
#     symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
#     symbols = ''.join([symbol for symbol in symbols if symbol not in "lIoO"])
#     return ''.join(random.sample(symbols, length))
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')


# import string
# import random
# def generate_password(length):
#     simbol = [i for i in (string.ascii_letters+string.digits) if i not in "lI1oO0"]
#     return ''.join(random.sample(simbol, length))


# from random import sample
# from string import ascii_letters, digits
# abc = [c for c in ascii_letters + digits if c not in 'lI1oO0']
# n, m = (int(input()) for _ in 'nm')
# for _ in range(n):
#     print(''.join(sample(abc, m)))



'''Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных
 и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной 
букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа nn и mm, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length
 символов.
Примечание 3. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации
 паролей.

Для отладки кода 🟡
Sample Input 1:

9
7
Sample Output 1:

iHnPg7q
Njj9m3N
tQ9v5ut
6qPZ3tV
6gVScya
kU8ncAY
5CKX9Da
UTQRve4
FyRe8NN'''

# import string, random
#
#
# def generate_password(length):
#     symbols = ([x for x in string.ascii_uppercase if x not in 'OI'],
#                [x for x in string.ascii_lowercase if x not in 'ol'],
#                [x for x in string.digits[2:]])
#
#     password = [random.choice(symbols[i]) for i in range(3)]
#     password += random.sample(''.join([''.join(symbols[i]) for i in range(3)]), length - 3)
#     random.shuffle(password)
#
#     return ''.join(password)
#
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')



# import random
# import string
#
# def generate_password(length):
#     l = [i for i in (string.ascii_letters + string.digits) if i not in 'lI1o0O']
#     while True:
#         pas = [0 for _ in range(length)]
#         pas[0] = random.choice('23456789')
#         pas[1] = random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')
#         pas[2] = random.choice('abcdefghijkmnpqrstuvwxyz')
#         pas[3:] = random.sample(l, length - 3)
#         print(''.join(pas))
#         break
#
# def generate_passwords(count, length):
#     for _ in range(count):
#         generate_password(length)
#
# n, m = int(input()), int(input())
# generate_passwords(n, m)


# import string
# from random import shuffle, choice
#
# a, b, c = 'ABCDEFGHIJKLMNPQRSTUVWXYZ', 'abcdefghijkmnpqrstuvwxyz', '23456789'
#
# into0 = [choice(j) for j in (a, b, c)]
# into1 = [i for i in string.ascii_letters + string.digits if i not in '0oO1Il']
#
#
# def generate_password(length):
#     shuffle(into0)
#     shuffle(into1)
#     return ''.join(into1[:length - 3] + into0)
#
#
# def generate_passwords(count, length):
#     print(*[generate_password(length) for _ in range(count)], sep='\n')
#
#
# n, m = int(input()), int(input())
# generate_passwords(n, m)


# import string
# from random import sample, shuffle
#
# set1 = set('23456789')
# set2 = set(string.ascii_uppercase) - set('IO')
# set3 = set(string.ascii_lowercase) - set('lo')
# n, m = int(input()), int(input())
# for _ in range(n):
#     password = sample(set1, 1) + sample(set2, 1) + sample(set3, 1) + sample(set1|set2|set3, m-3)
#     shuffle(password)
#     print(''.join(password))


'''Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до 75
(включительно), при этом центральная клетка является пустой (она заполняется числом 0).

Игра-лото "Cупер Бинго". Играть в лотерею онлайн бесплатно

Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.

Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно 3 символа. Для этого используйте 
строковый метод ljust().

Примечание 2. Пример возможного ответа:

1  16 31 46 61
10 30 42 47 68
3  18 0  48 63
9  19 34 49 70
5  20 35 50 65
Возможны и другие способы генерации карточки для игры в бинго.'''

# from random import sample
#
# nums = iter(sample(list(range(1, 76)), 24))
# [print(*('0  ' if i == j == 2 else str(next(nums)).ljust(3) for j in range(5))) for i in range(5)]


# from random import sample as r
#
# n = r(range(1, 75), 24)
# n = n[:12] + [0] + n[12:]
# [print(''.join(str(n[i * 5 + j]).ljust(3) for j in range(5))) for i in range(5)]


# from random import sample
# line = sample(range(1, 76), 25)
# card = [line[i: i + 5] for i in (0, 5, 10, 15, 20)]
# card[2][2] = 0
# for line in card:
#     line = [str(x).ljust(3, ' ') for x in line]
#     print(*line, sep='')



# from random import *
# numbers = set(sample([i for i in range(1, 76)], 25))
# s = [[numbers.pop() for _ in range(5)] for _ in range(5)]
# s[2][2] = 0
# for row in s:
#     print(*(str(k).ljust(3) for k in row))