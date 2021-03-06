'''Тема урока: модуль random
Случайные числа
Псевдослучайные числа
Модуль random
Аннотация. Урок посвящен модулю random, который содержит функции по работе с псевдослучайными числами.

Случайные числа
Случайные числа – последовательность чисел, в которой невозможно предсказать следующее число, зная все предыдущие.

Случайные числа широко используются в различных задачах программирования:

в играх (имитация подбрасывания игрального кубика и другие подобные ситуации);
в программах имитационного моделирования;
в статистических программах, случайным образом отбирающих данные для анализа;
в компьютерной безопасности для шифрования уязвимых данных.
Для создания истинно случайных чисел можно бросать монету, игральные кости, или измерять какой-нибудь шумовой сигнал.

Псевдослучайные числа
Ставить сложные электронные приборы на каждый компьютер для генерации истинно случайных чисел дорого, поэтому
математики и программисты создали алгоритмы получения псевдослучайных чисел.

Для обычного человека псевдослучайные числа практически не отличаются от случайных, однако они вычисляются по
математической формуле, и зная первое число и формулу, можно определить любое следующее.

Python предлагает встроенные функции для работы с псевдослучайными числами. Эти функции хранятся в модуле random
в стандартной библиотеке.

Модуль random
Модуль random предоставляет функции для генерации псевдослучайных чисел, букв и случайного выбора элементов
последовательности (списка, строки и т.д.).

Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:

import random
После подключения модуля мы можем использовать его функции.

Функция randint()

Функция randint() принимает два обязательных аргумента a и b и возвращает псевдослучайное целое число из отрезка
[a; \, b][a;b].

Следующий код выводит два псевдослучайных целых числа: num1 из отрезка [0; 17][0;17] и num2 из отрезка [-5; 5][−5;5].

import random

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)
Левая и правая граница a и b включаются в диапазон генерируемых псевдослучайных чисел. Результатом вызова функции
random.randint(2, 9) может быть любое число от 22 до 99, включая 22 и 99.

Следующий код выводит 1010 псевдослучайных целых чисел из диапазона [1; \, 100][1;100]:

import random

for _ in range(10):
    print(random.randint(1, 100))
Среди этих чисел возможны повторения.

Функция randrange()
Если вы помните, как применять функцию range(), то почувствуете себя непринужденно с функцией randrange().
 Функция randrange() принимает такие же аргументы, что и функция range(). Различие состоит в том, что функция
 randrange()
не возвращает саму последовательность чисел. Вместо этого она возвращает случайно выбранное число из
последовательности чисел.

Следующий код присваивает переменной num псевдослучайное число в диапазоне от 00 до 99:

import random

num = random.randrange(10)
Аргумент 1010 задает конечный предел последовательности значений. Функция возвратит случайно выбранное число из
последовательности чисел от 00 до конечного предела, исключая сам предел.

Следующий код задает начальное значение и конечный предел последовательности:

import random

num = random.randrange(5, 10)
Таким образом в переменной num будет храниться псевдослучайное число в диапазоне от 55 до 99.

Следующий код задает начальное значение, конечный предел и величину шага:

import random

num = random.randrange(0, 101, 10)
Таким образом в переменной num будет храниться псевдослучайное число из последовательности чисел:
 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.

Функция random()
Функции randint() и randrange() возвращают псевдослучайное целое число. А вот функция random() возвращает
псевдослучайное число с плавающей точкой (вещественное число). В функцию random() никаких аргументов не
передается. Функция random() возвращает случайное число с плавающей точкой в диапазоне от 0.00.0 до 1.01.0
(исключая 1.01.0).

Следующий код выводит случайное число с плавающей точкой из диапазона [0.0; \, 1.0)[0.0;1.0):

import random

num = random.random()
print(num)
Функция uniform()
Функция uniform() тоже возвращает случайное число с плавающей точкой, но при этом она позволяет задавать диапазон
для отбора значений.

Следующий код выводит псевдослучайное число с плавающей точкой из диапазона [1.5; \, 17.3][1.5;17.3] (включительно):

import random

num = random.uniform(1.5, 17.3)
print(num)
Функция seed()
Как уже было сказано псевдослучайные числа вычисляются на основе некой формулы. Генерация случайных чисел инициируется
 начальным значением. Оно используется в вычислении, возвращающем следующее случайное число в ряду. Когда модуль
 random импортируется, он получает системное время из внутреннего генератора тактовых импульсов компьютера и
 использует его как начальное значение. Системное время – целое число, представляющее собой текущую дату и время
 вплоть до сотой секунды. Если бы всегда использовалось одно и то же начальное значение, функции генерации случайных
 чисел всегда  возвращали бы один и тот же ряд псевдослучайных чисел. Поскольку системное время меняется каждую
 сотую долю секунды, можно утверждать, что всякий раз, когда импортируется модуль random, будет создана отличающаяся
 от предыдущих последовательность случайных чисел.

Вместе с тем, некоторые программы требуют генерации одной и той же последовательности случайных чисел. Для этого можно
вызвать функцию seed(), задав начальное значение.

Следующий код генерирует 1010 псевдослучайных чисел, и при этом содержит инструкцию, явно устанавливающую начальное
значение для генератора случайных чисел:

import random

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))
Результат выполнения такого кода:

67
54
39
47
38
23
99
91
91
70
Если выполнить код еще раз, получим ту же самую последовательность псевдослучайных чисел.

Примечания
Примечание 1. Подключение модуля следующим образом:

from random import *
позволяет в дальнейшем не писать название модуля и символ точки при вызове функций модуля.

Примечание 2. Функции модуля random на самом деле являются методами одноименного класса random.

Примечание 3. В Python для генерации псевдослучайных чисел используется один из самых совершенных алгоритмов генерации
псевдослучайных чисел – "вихрь Мерсенна", разработанный в 19971997 году. Реализация выполнена на языке CC, является
быстрой и потокобезопасной.

Примечание 4. Настоящие случайные числа можно получить с сайта. Данный сайт использует атмосферный шум для создания
по-настоящему случайных чисел.

Примечание 5. Пусть rr – случайное число из интервала (0; \, 1)(0;1). Для того, чтобы перевести такое число в интервал
 (a; \, b)(a;b) можно воспользоваться формулой a + (b-a)\cdot ra+(b−a)⋅r'''
import random


'''Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество
 попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).

Примечание. Например, при n=7n=7 ваша программа может выводить:

Орел
Решка
Решка
Орел
Орел
Орел
Решка'''

# from random import randint
# num = int(input())
# flips = [randint(0,1) for r in range(num)]
# results = []
# for object in flips:
#         if object == 0:
#             results.append('Орел')
#         elif object == 1:
#             results.append('Решка')
# print(*results, end=' ', sep='\n')

# import random
#
# n = int(input())    # количество попыток
# for _ in range(n):
#     print(random.choice(['Орел', 'Решка']))

# import random
#
# n = int(input())
# for _ in range(n):
#     print('Орел' if random.randrange(2) else 'Решка')

# from random import randint
#
# COIN = ['Орел', 'Решка']
#
# for _ in range(int(input())):
#     print(COIN[randint(0, 1)])


'''Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 6 гранями. Программа
 принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани 
 кубика (каждое на отдельной строке).

Примечание. Например, при n=7 ваша программа может выводить:

5
5
6
6
2
6
2
'''
# from random import randint
#
# for _ in range(int(input())):
#     print(randint(1, 6))

# import random
# print(*[random.randint(1, 6) for _ in range(int(input()))], sep='\n')


# import random
#
# n = int(input())    # количество попыток
# for i in range(n):
#   print(random.randint(1,6))
#
#
# import random
# print(*[random.randint(1, 6) for _ in range(int(input()))], sep='\n')

# from random import*
# [print (randrange(1, 7)) for _ in range(int(input()))]

'''Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину
 пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем
  регистре).

Примечание 1. Символам A..Z английского языка соответствуют номера с 6565 по 9090 в таблице символов ASCII.

Примечание 2. Символам a..z английского языка соответствуют номера с 9797 по 122122 в таблице символов ASCII.

Примечание 3. Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.

 Примечание 4. Например, при длине пароля, равной 1515 символам ваша программа может выводить:

peJFAmhqfaAeKDu'''

# import string
# import random
# def id_generator(size=int(input()), chars=string.ascii_uppercase+string.ascii_lowercase):
#   return ''.join(random.choice(chars) for _ in range(size))
# print(id_generator())

# import random
#
# length = int(input())    # длина пароля
# password = ''
# for i in range(length):
#     password += [chr(random.randint(65, 90)), chr(random.randint(97, 122))][random.randint(0, 1)]
# print(password)

# from random import randint as R
#
# for _ in range(int(input())):
#     print([chr(R(65, 90)), chr(R(97, 122))][R(0, 1)], end = '')

# from random import *
#
# for _ in range(int(input())):
#     print(chr(choice([randint(65, 90), randint(97, 122)])), end='')

# print(''.join(__import__('random').sample([chr(n) for a, b in ((65, 91), (97, 123)) for n in range(a, b)], int(input()))))
#
#
# print(''.join(__import__('random').sample(__import__('string').ascii_letters, int(input()))))


'''Лотерейный билет содержит 77 чисел из диапазона от 1 до 49 (включительно).

Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
 Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.

Примечание. Убедитесь, что сгенерированные числа не содержат дубликатов.'''


# from random import sample
# print(*map('{}'.format, sorted(sample(range(1,49), 7))))

# from random import *
# lot = set()
# while len(lot) != 7:
#     lot.add(randint(1, 49))
# print(*sorted(lot))

# import random as rnd
# print(*sorted(rnd.sample(range(1, 50), 7)))


# import random
# s = list(range(1, 50))
# random.shuffle(s)
# print(*sorted(s[:7]))

# import random
# l = set()
# while len(l) < 7:
#     l.add(random.randint(1, 49))
# print(*sorted(l))