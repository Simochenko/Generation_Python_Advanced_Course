"""Тема урока: кортежи
Функция tuple()
Особенности кортежей
Методы кортежей
Вложенные кортежи
Аннотация. Урок посвящен кортежам (тип данных tuple).

Функция tuple()
Встроенная функция list() может применяться для преобразования кортежа в список.

Приведенный ниже код:

number_tuple = (1, 2, 3, 4, 5)
number_list = list(number_tuple)
print(number_list)
выводит:

[1, 2, 3, 4, 5]
Встроенная функция tuple()  может применяться для преобразования списка в кортеж.

Приведенный ниже код:

str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)
print(str_tuple)
выводит:

('один', 'два', 'три')
Аналогичным образом мы можем создать кортеж на основании строки.

Приведенный ниже код:

text = 'hello python'
str_tuple = tuple(text)
print(str_tuple)
выводит:

('h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n')
Обратите внимание, что символ пробел содержится в кортеже str_tuple.

Преобразование строки в список позволяет получить список символов строки. Это может быть полезно, например, когда надо
изменить один символ строки:

s = 'симпотичный'
print(s)
a = list(s)
a[4] = 'а'
s = ''.join(a)
print(s)
Приведенный выше код выводит:

симпотичный
симпатичный
С этой же целью может потребоваться преобразование кортежа в список:

writer = ('Лев Толстой', 1827)
print(writer)
a = list(writer)
a[1] = 1828
writer = tuple(a)
print(writer)
Приведенный выше код выводит:

('Лев Толстой', 1827)
('Лев Толстой', 1828)
Особенности кортежей
Кортежи поддерживают те же операции, что и списки, за исключением изменяющих содержимое.

Кортежи поддерживают:

доступ к элементу по индексу (только для получения значений элементов);
методы, в частности index(), count();
встроенные функции, в частности len(), sum(), min() и max();
срезы;
оператор принадлежности in;
операторы конкатенции (+) и повторения (*).
Функция len()
Длиной кортежа называется количество его элементов. Для того, чтобы посчитать длину кортежа мы используем встроенную
 функцию len().

Следующий программный код:

numbers = (2, 4, 6, 8, 10)
languages = ('Python', 'C#', 'C++', 'Java')

print(len(numbers))      # выводим длину кортежа numbers
print(len(languages))    # выводим длину кортежа languages

print(len(('apple', 'banana', 'cherry')))   # выводим длину кортежа, состоящего из 3 элементов
выведет:

5
4
3
Оператор принадлежности in
Оператор in позволяет проверить, содержит ли кортеж некоторый элемент.

Рассмотрим следующий код:

numbers = (2, 4, 6, 8, 10)

if 2 in numbers:
    print('Кортеж numbers содержит число 2')
else:
    print('Кортеж numbers не содержит число 2')
Такой код проверяет, содержит ли кортеж numbers число 22 и выводит соответствующий текст:

Кортеж numbers содержит число 2
Мы можем использовать оператор in вместе с логическим оператором not. Например

numbers = (2, 4, 6, 8, 10)

if 0 not in numbers:
    print('Кортеж numbers не содержит нулей')
Индексация
При работе со списками (строками) мы использовали индексацию, то есть обращение к конкретному элементу списка (строки)
по его индексу. Аналогично можно индексировать и элементы кортежей.

Для индексации кортежей в Python используются квадратные скобки [], в которых указывается индекс (номер) нужного
элемента в кортеже:

Пусть numbers = (2, 4, 6, 8, 10).

Таблица ниже, показывает как работает индексация:

Выражение	Результат	Пояснение
numbers[0]	22	первый элемент кортежа
numbers[1]	44	второй элемент кортежа
numbers[2]	66	третий элемент кортежа
numbers[3]	88	четвертый элемент кортежа
numbers[4]	1010	пятый элемент кортежа
Так же, как и в списках, для нумерации с конца разрешены отрицательные индексы.

Выражение	Результат	Пояснение
numbers[-1]	1010	пятый элемент кортежа
numbers[-2]	88	четвертый элемент кортежа
numbers[-3]	66	третий элемент кортежа
numbers[-4]	44	второй элемент кортежа
numbers[-5]	22	первый элемент кортежа
Как и в списках, попытка обратиться к элементу кортежа по несуществующему индексу:

print(numbers[17])
вызовет ошибку:

IndexError: tuple index out of range
Срезы
Рассмотрим кортеж numbers = (2, 4, 6, 8, 10).

С помощью среза мы можем получить несколько элементов кортежа, создав диапазон индексов разделенных двоеточием
numbers[x:y].

Следующий программный код:

print(numbers[1:3])
print(numbers[2:5])
выводит:

(4, 6)
(6, 8, 10)
При построении среза numbers[x:y] первое число – это то место, где начинается срез (включительно), а второе – это
место, где заканчивается срез (невключительно).

При использовании срезов с кортежами мы также можем опускать второй параметр в срезе numbers[x:] (но поставить
 двоеточие), тогда срез берется до конца кортежа. Аналогично если опустить первый параметр numbers[:y], то
 можно взять срез от начала кортежа.

  Срез numbers[:] возвращает копию исходного кортежа.

Как и в списках, можно использовать отрицательные индексы в срезах кортежей.

Операция конкатенации + и умножения на число *
Операторы + и * применяют для кортежей как и для списков.

Следующий программный код:

print((1, 2, 3, 4) + (5, 6, 7, 8))
print((7, 8) * 3)
print((0,) * 10)
выводит:

(1, 2, 3, 4, 5, 6, 7, 8)
(7, 8, 7, 8, 7, 8)
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Для генерации кортежей, состоящих строго из повторяющихся элементов, умножение на число — самый короткий и
правильный путь.

Расширенные операторы += и *= также можно использовать при работе с кортежами.

Следующий программный код:

a = (1, 2, 3, 4)
b = (7, 8)
a += b   # добавляем к кортежу a кортеж b
b *= 5   # повторяем кортеж b 5 раз

print(a)
print(b)
выводит:

(1, 2, 3, 4, 7, 8)
(7, 8, 7, 8, 7, 8, 7, 8, 7, 8)
Встроенные функции sum(), min(), max()
Встроенная функция sum() принимает в качестве параметра кортеж чисел и вычисляет сумму его элементов.

Следующий программный код:

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Сумма всех элементов кортежа =', sum(numbers))
выводит:

Сумма всех элементов кортежа = 55
Встроенные функции min() и max() принимают в качестве параметра кортеж и находят минимальный и максимальный
элементы соответственно.

Следующий программный код:

numbers = (3, 4, 10, 3333, 12, -7, -5, 4)
print('Минимальный элемент кортежа =', min(numbers))
print('Максимальный элемент кортежа =', max(numbers))
выводит:

Минимальный элемент кортежа = -7
Максимальный элемент кортежа = 3333
Функции min() и max() можно применять только к кортежам с одним типом данных. Если кортеж содержит разные типы
данных, скажем целое число (int) и строку (str), то во время выполнения программы произойдет ошибка.

Метод index()
Метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению. Таким
образом, в метод передается один параметр:

value: значение, индекс которого требуется найти.
Если элемент в кортеже не найден, то во время выполнения происходит ошибка.

Следующий программный код:

names = ('Gvido', 'Roman' , 'Timur')
position = names.index('Timur')
print(position)
выведет:

2
Следующий программный код:

names = ('Gvido', 'Roman' , 'Timur')
position = names.index('Anders')
print(position)
приводит к ошибке:

ValueError: tuple.index(x): x not in tuple
Чтобы избежать таких ошибок, можно использовать метод index() вместе с оператором принадлежности in:

names = ('Gvido', 'Roman' , 'Timur')
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в кортеже')
Метод count()
Метод count() возвращает количество элементов в кортеже, значения которых равны переданному в метод значению.

Таким образом, в метод передается один параметр:

value: значение, количество элементов, равных которому,  нужно посчитать.
Если значение в кортеже не найдено, то метод возвращает 00.

Следующий программный код:

names = ('Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur')
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1)
print(cnt2)
print(cnt3)
выведет:

3
1
0
Кортежи не поддерживают такие методы, как append(), remove(), pop(), insert(), reverse(), sort(), так как они изменяют
содержимое.

Вложенные кортежи
Подобно спискам, мы можем создавать вложенные кортежи.

Следующий программный код:

colors = ('red', ('green', 'blue'), 'yellow')
numbers = (1, 2, (4, (6, 7, 8, 9)), 10, 11)
print(colors[1][1])
print(numbers[2][1][3])
выводит:

blue
9
"""
'''Дополните приведенный код, используя индексацию кортежа, чтобы переменная last, содержала последний элемент 
кортежа countries.'''

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# last = countries[-1]
# print(last)

'''Дополните приведенный код, используя срезы, так чтобы он вывел первые 66 элементов кортежа primes.

Примечание. Результатом вывода должна быть строка (2, 3, 5, 7, 11, 13).'''

# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# print(primes[:6])


'''Дополните приведенный код, используя срезы, так чтобы он вывел элементы кортежа countries, кроме первых двух.
Примечание. Результатом вывода должна быть строка ('Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 
'Chile', 'Cameroon').'''

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:])

'''Дополните приведенный код, используя срезы, чтобы он вывел все элементы кортежа countries, кроме последних трех.

Подсказка
Не забывайте, что элементы кортежа нумеруются с −1 начиная с конца.'''

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

'''Дополните приведенный код, используя срезы, чтобы он вывел все элементы кортежа countries, кроме двух последних 
и трех первых.'''

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

'''Дополните приведенный код так, чтобы переменная number содержала количество элементов кортежа countries.

Подсказка
Используйте встроенную функцию len().'''

# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)


'''Дополните приведенный код так, чтобы он вывел сумму минимального и максимального элементов кортежа numbers.'''

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# minN = min(numbers)
# maxN = max(numbers)
# print(maxN + minN)


'''Дополните приведенный код так, чтобы переменная index, содержала индекс элемента «Slovenia» в кортеже countries.

Подсказка
Используйте кортежный метод index().'''

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)

'''Дополните приведенный код так, чтобы переменная number, содержала количество вхождений «Spain» в кортеж countries.

Подсказка
Используйте кортежный метод count().
'''

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile',
# 'Spain', 'Cameroon')
# number = countries.count('Spain')
# print(number)

'''Дополните приведенный код, используя операторы конкатенации (+) и умножения кортежа на число (*), чтобы он вывел 
кортеж:
 (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13).'''

# numbers1 = (1, 2, 3)*2
# numbers2 = (6,)*9
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
# print(numbers1+numbers2+numbers3)


'''В переменную city_name вводится название города (например, Москва), а в переменную city_year – год его основания 
(например, 11471147). Заполните пропущенную строку таким образом, чтобы в переменной city оказался кортеж из значений 
этих двух переменных (сначала название города, затем год основания).'''
#
# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)

# city_name = [input()]
# city_year = [int(input())]
# city = tuple(city_name)+ tuple(city_year)
# print(city)


'''Дополните приведенный код, так чтобы получить список, содержащий только непустые кортежи исходного списка tuples, 
не меняя порядка их следования.

Подсказка 1
Для проверки пустоты кортежа используйте встроенную функцию len().

Подсказка 2
Используйте списочное выражение.

 '''

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [x for x in tuples if x]
# print(non_empty_tuples)

'''Дополните приведенный код так, чтобы переменная new_tuples, содержала исходный список кортежей с последним 
элементом каждого, измененным на численное значение 100.

Подсказка 1
Используйте списочное выражение.

Подсказка 2
Чтобы получить все элементы кортежа t кроме последнего, используем срез t[:-1].

Подсказка 3
Чтобы создать кортеж, содержащий единственный элемент 100, мы используем (100,).

Напишите программу. Тестируется через stdin → stdout'''

# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = ([t[:-1] + (100,) for t in tuples])
# print(new_tuples)


# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [tuple(list(i)[:-1]+[100]) for i in tuples]
# print(new_tuples)


# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = []
# for c in tuples:
#     k=list(c)
#     k[-1]=100
#     new_tuples.append(tuple(k))
# print(new_tuples)
