# n = 3
# list1 = []
#
# for _ in range(n):
#     row = input().split()
#     list1.extend(row)
#
# print(list1)

# 9 7 6
# 2 1
# 3 4 45 67

# ['9', '7', '6', '2', '1', '3', '4', '45', '67']
# Какой тип данных будет у переменной row?
# my_list = [[1], [2, 3], [4, 5, 6]]
# total = 0
#
# for row in my_list:
#     total += sum(row)
#
# print(type(row))

# Что покажет приведенный ниже фрагмент кода?
# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     maximum = max(row)
#     minimum = min(row)
# print(maximum + minimum)
# # 107

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
#
# print(maximum + minimum)

# 636
'''Список по образцу 1
На вход программе подается число nn. Напишите программу, которая создает и выводит построчно вложенный список,
состоящий из nn списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести построчно указанный вложенный список.

Sample Input 1:

3
Sample Output 1:

[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
Sample Input 2:

2
Sample Output 2:

[1, 2]
[1, 2]
Sample Input 3:

5
Sample Output 3:

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]'''

#
# n = int(input())
# my_list = []
#
# for i in range(n):
#     my_list.append(i+1)
# for i in range(n):
#     print(my_list)
#
#
# n = int(input())
# print(*[[i for i in range(1, n+1)] for i in range(1, n+1)], sep = "\n")

'''Список по образцу 2
На вход программе подается число nn. Напишите программу, которая создает и выводит построчно вложенный список, 
состоящий из nn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести построчно указанный вложенный список.

Sample Input 1:

4
Sample Output 1:

[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]'''

# n = int(input())
# my_list = []
# for i in range(n):
#     my_list.append(i + 1)
#     print(my_list)

'''Треугольник Паскаля 1
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике
 на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число nn. Напишите программу, которая возращает указанную строку треугольника Паскаля в 
виде списка (нумерация строк начинается с нуля).

Формат входных данных
На вход программе подается число n \, (n \ge 0)n (n≥0).

Формат выходных данных
Программа должна вывести указанную строку треугольника Паскаля в виде списка.

Примечание 1. Решение удобно оформить в виде функции pascal(), которая принимает номер строки и возвращает 
соответствующую строку треугольника Паскаля.

Примечание 2. Графическая иллюстрация формирования треугольника Паскаля.'''

# x = int(input())
# def PrintPasTriangle(rows):
#     row = [1]
#     for i in range(rows):
#
#         row = [sum(x) for x in zip([0] + row, row + [0])]
#     print(row)
#
#
# PrintPasTriangle(x)

'''Треугольник Паскаля 2
На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника
 Паскаля.

Формат входных данных
На вход программе подается число n \, (n \ge 1)n (n≥1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

Sample Input 1:

4
Sample Output 1:

1
1 1
1 2 1
1 3 3 1
Sample Input 2:

5
Sample Output 2:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1'''

# x = int(input())
# def PrintPasTriangle(rows):
#     row = [1]
#     for i in range(rows):
#         print(* row)
#         row = [sum(x) for x in zip([0] + row, row + [0])]
#
#
# PrintPasTriangle(x)
#
# pasc = [1]
# for x in range(int(input())):
#     print(*pasc)
#     pasc[1:] = list(map(lambda a, b: a + b, pasc, pasc[1:] + [0]))
#
# def chunks(lst, n):
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]
#
#
# print(list(chunks(range(10, 75), 10)))


# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[i][j], end=' ')
#     print()

# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[j][i], end=' ')
#     print()

# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()

# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)  #101

'''Разбиение на чанки
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, которое задает размер чанка (куска). Функция должна вернуть список, состоящий из чанков указанной размерности.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.

Sample Input 1:

a b c d e f
2
Sample Output 1:

[['a', 'b'], ['c', 'd'], ['e', 'f']]
Sample Input 2:

a b c d e f
3
Sample Output 2:

[['a', 'b', 'c'], ['d', 'e', 'f']]
Sample Input 3:

a b c d e f
6
Sample Output 3:

[['a', 'b', 'c', 'd', 'e', 'f']]
Sample Input 4:

a b c d e f r g b
2
Sample Output 4:

[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]'''

# def chunked(arr, size):
#     arrs = []
#     while len(arr) > size:
#         pice = arr[:size]
#         arrs.append(pice)
#         arr = arr[size:]
#     arrs.append(arr)
#     return arrs
#
#
# x = input().split()
# y = int(input())
# print(chunked(x, y))

# def chunked(sp, n):
#     return [sp[x:x + n] for x in range(0,len(sp),n)]
#
#
# s = input().split()
# n = int(input())
# print(chunked(s, n))


# from itertools import product
#
#
# def sublists(lst):
#     for doslice in product([True, False], repeat=len(lst) -1):
#         slices = []
#         start = 0
#         for i, slicehere in enumerate(doslice, 0):
#             if slicehere:
#                 slices.append(lst[start:i])
#                 start = i
#         slices.append(lst[start:])
#         yield slices
#
#
# from pprint import pprint
#
# mylist = input()
# pprint(list(sublists(mylist)))


'''Упаковка дубликатов 🌶️
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
 последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Sample Input 1:

a b c d
Sample Output 1:

[['a'], ['b'], ['c'], ['d']]
Sample Input 2:

w w w o r l d g g g g r e a t t e c c h e m g g p w w
Sample Output 2:

[['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], 
['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]'''

# from itertools import groupby
# s = input()
# res = [list(v) for k, v in groupby(s.split())]
# print(res)

# res = []
# a = input().split()
# for i in a:
#     res.append([i]) if not res or i not in res[-1] else res[-1].append(i)
# print(res)

# s = input().split()
# x = []
# for i in range(len(s)):
#     if not x or x[-1][-1] != s[i]:
#         x.append([s[i]])
#     else:
#         x[-1].append(s[i])
# print(x)

'''Подсписки списка 🌶️🌶️
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. 
Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4],
 но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. Пустой 
 список — подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка 
 [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу,
 которая выводит список, содержащий все возможные подсписки списка, включая пустой список.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный список, содержащий все возможные подсписки, включая пустой список в соответствии с 
примерами.

Sample Input 1:

a b
Sample Output 1:

[[], ['a'], ['b'], ['a', 'b']]
Sample Input 2:

a b v
Sample Output 2:

[[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]'''

# str_in = input('').split()
# new_list = [[]]
# for len_substr in range(len(str_in)):
#     for i in range(len(str_in) - len_substr):
#         new_list.append(str_in[i:i + len_substr + 1])
#
# print(new_list)


# print([[]] + [l[j:i + j + 1] for l in [input().split()] for i in range(len(l)) for j in range(len(l) - i)])