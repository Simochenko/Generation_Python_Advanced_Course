'''Тема урока: матрицы
Работа с матрицами
Квадратные и прямоугольные матрицы
Функции ljust() и rjust()
Главная и побочная диагонали
Аннотация. Урок посвящен работе с матрицами — прямоугольными таблицами.

Матрицы
В прошлых уроках мы изучили вложенные списки, то есть списки, входящие в качестве элементов в другие списки. Частный
 случай вложенных списков — матрицы — прямоугольные таблицы, заполненные какими-то значениями, обычно числами.



Матрицы часто применяются в математике, так как многие задачи с их помощью гораздо проще сформулировать, записать
и решить.

Для работы с матрицами нужно уметь получать элемент ii-й строки jj-го столбца. Для этого обычно заводят список строк
матрицы, где каждая строка — список элементов. Получается вложенный список или список списков. Теперь, чтобы получить
определенный элемент, достаточно из списка строк матрицы выбрать ii-ю и взять jj-й элемент этой строки.

Давайте заведем матрицу размера 3×4 (3 строки и 4 столбца), содержащую числа, и получим элемент на позиции
(2, 3)(2, 3), то есть элемент второй строки в третьем столбце.

matrix  = [[2, -5, -11, 0],
           [-9, 4, 6, 13],
           [4, 7, 12, -2]]

print(matrix[1][2])  # вывод элемента на позиции (2, 3)
В переменной matrix — хранится вся матрица, при этом matrix[1] — список значений во второй строке, matrix[1][2] —
элемент в третьем столбце этой строки.



В математике нумерация строк и столбцов начинается с единицы, а не с нуля. По договоренности сначала всегда
указывается строка, а затем — столбец. Элемент на ii-ой строке, jj-м столбце матрицы aa обозначается так a_{ij}a
ij
​
 .

Перебор элементов матрицы
Чтобы перебрать элементы матрицы, необходимо использовать вложенные циклы. Например, выведем на экран все элементы
матрицы, перебирая их по строкам:

rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов

matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
Результатом работы такого кода будет:

2 3 1 0
9 4 6 8
4 7 2 7
Для перебора элементов матрицы по столбцам можно использовать следующий код:

rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов

matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()
Результатом работы такого кода будет:

2 9 4
3 4 7
1 6 2
0 8 7
Функции ljust() и rjust()
Рассмотрим программный код:

rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
 Результатом работы такого кода будет:

277 -930 11 0
9 43 6 87
4456 8 290 7
Выведенная матрица не сильно похожа на упорядоченный прямоугольник. Элементы матрицы имеют разное количество
разрядов и результат вывода получается смазанным. Для решения проблемы удобно использовать строковые методы
ljust() и rjust().

Метод ljust()
Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.

Результатом выполнения следующего кода:

print('a'.ljust(3))
print('ab'.ljust(3))
print('abc'.ljust(3))
будет:

a⎵⎵
ab⎵
abc
Исходная строка не обрезается, даже если в ней больше символов, чем нужно.

Результатом выполнения следующего кода:

print('abcdefg'.ljust(3))
будет:

abcdefg
Строковый метод ljust() использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.

Результатом выполнения следующего кода:

print('a'.ljust(5, '*'))
print('ab'.ljust(5, '$'))
print('abc'.ljust(5, '#'))
будет:

a****
ab$$$
abc##
Метод rjust()
Строковый метод rjust() выравнивает текст по ширине, добавляя пробелы в начало текста.

Результатом выполнения следующего кода:

print('a'.rjust(3))
print('ab'.rjust(3))
print('abc'.rjust(3))
будет:

⎵⎵a
⎵ab
abc
Исходная строка не обрезается, даже если в ней больше символов, чем нужно.

Результатом выполнения следующего кода:

print('abcdefg'.rjust(3))
будет:

abcdefg
Строковый метод rjust() использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.

Результатом выполнения следующего кода:

print('a'.rjust(5, '*'))
print('ab'.rjust(5, '$'))
print('abc'.rjust(5, '#'))
будет:

****a
$$$ab
##abc
Применив метод ljust() для выравнивания столбцов при выводе таблицы мы получим следующий код:

rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()
Результатом выполнения такого кода будет:

277   -930  11    0
9     43    6     87
4456  8     290   7
Квадратные матрицы
Матрица с одинаковым количеством строк и столбцов называется квадратной. У квадратной матрицы есть две диагонали:

главная: проходит из верхнего левого в правый нижний угол матрицы;
побочная: проходит из нижнего левого в правый верхний угол матрицы.


Элементы с равными индексами i == j находятся на главной диагонали. Такие элементы обозначаются matrix[i][i].

Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1), где n — размерность матрицы,
находятся на побочной диагонали.

Таким образом, чтобы установить элементы главной или побочной диагонали, достаточно одного цикла.

Результатом выполнения следующего кода:

n = 8
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8

for i in range(n):                     # заполняем главную диагональ 1-цами, а побочную 2-ками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2

for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
будет:

1 0 0 0 0 0 0 2
0 1 0 0 0 0 2 0
0 0 1 0 0 2 0 0
0 0 0 1 2 0 0 0
0 0 0 2 1 0 0 0
0 0 2 0 0 1 0 0
0 2 0 0 0 0 1 0
2 0 0 0 0 0 0 1
Индексыi и jэлементов на главной диагонали связаны соотношением i = j. Индексы i и jэлементов на побочной диагонали
связанны соотношением i + j + 1 = n (или  j = n - i - 1), где n — размерность матрицы

Заметим также, что:

если элемент находится выше главной диагонали, то i < j, если ниже, i > j.
если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже, i + j + 1 > n.
Примечания
Примечание 1. Чтобы понять, в какой области лежит элемент можно воспользоваться следующей картинкой.



Примечание 2. Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
Примечание 3. Для считывания квадратной матрицы размерности n, заполненной числами, удобно использовать следующий код:

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)'''
'''Вывести матрицу 1
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в
 матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой 
 строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

Формат входных данных
На вход программе подаются два числа n и m — количество строк и стобцов в матрице, далее идут n \times mn×m слов,
 каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним символом пробела.

Sample Input 1:

4
2
и
швец
и
жнец
и
на
дуде
игрец
Sample Output 1:

и швец
и жнец
и на
дуде игрец
Sample Input 2:

2
3
язык
болтает
а
голова
не
знает
Sample Output 2:

язык болтает а
голова не знает'''

# n = int(input())
# m = int(input())
#
# res = [[None for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         res[i][j] = input()
#
# for row in res:
#     print(*row)
# print()
# for c in range(m):
#     for r in range(n):
#         print(res[r][c], end=' ')
#     print()



# n, m = int(input()), int(input())
# arr = [[input() for _ in range(m)] for _ in range(n)]
# for row in arr:
#     print(*row)
# print()
# for i in range(m):
#     for j in range(n):
#         print(arr[j][i], end=' ')
#     print()
# *********************************************************************************************
'''След матрицы
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит
 след заданной квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы 
матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — след заданной матрицы.

Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

15
Sample Input 2:

4
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
Sample Output 2:

4'''
# n = int(input())
# a = []
# for i in range(n):
#     a.append([int(j) for j in input().split()])
#
# def printDiagonalSums(mat, n):
#     principal = 0
#     for i in range(0, n):
#         for j in range(0, n):
#             if (i == j):
#                 principal += mat[i][j]
#     print(principal)
#
# printDiagonalSums(a, n)
# *****************************************************************************

#
# res = 0
# for i in range(int(input())):
#     res += int(input().split()[i])
# print(res)


'''Больше среднего
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести nn чисел — для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной строки.

Sample Input 1:

4
1 2 3 4
5 6 3 15
0 2 3 1
5 2 8 5
Sample Output 1:

2
1
2
1'''
# import numpy
# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#     s = (numpy.mean(temp))
#     count = 0
#     for i in temp:
#
#         if i>s:
#             count += 1
#     print(count)


# n = int(input())
# [print(sum([_ > sum(r)/n for _ in r])) for r in [list(map(int, input().split())) for _ in range(n)]]


# n = int(input())
# matrix = []
# counter = 0
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     sr = sum(temp)/n
#     for j in range(n):
#         if temp[j] > sr:
#             counter += 1
#     print(counter)
#     counter = 0

'''Максимальный в области 1
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.

Sample Input 1:

3
1 4 5
6 7 8
1 1 6
Sample Output 1:

7
Sample Input 2:

4
0 1 4 6
0 0 2 5
0 0 0 7
0 0 0 0
Sample Output 2:

0
Sample Input 3:

2
6 0
7 9
Sample Output 3:

9
'''

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# t_max = max([matrix[i][j] for i in range(0,len(matrix)) for j in range(i+1)])
# print(t_max)


# print(max(e for i in range(int(input())) for e in input().split()[:i + 1]))

# n = int(input())
# c = 0
# for i in range(n):
#     c = max(c, max([int(x) for x in input().split()[:i + 1]]))
# print(c)

'''Максимальный в области 2 🌶️
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы 
построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы диагоналей также учитываются.

Sample Input 1:

3
1 4 5
6 7 8
1 1 6
Sample Output 1:

8
Sample Input 2:

4
0 1 4 6
0 0 2 5
0 0 0 7
0 0 0 0'''

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# t_max = max([matrix[i-1][j-1] for i in range(0,len(matrix)) for j in range(i+1)])
# print(t_max)

'''Суммы четвертей
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую 
и правую.



Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой 
четверти.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы
 построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.

Sample Input 1:

4
1 2 3 4
5 6 7 8
3 4 5 6
1 2 3 4
Sample Output 1:

Верхняя четверть: 5
Правая четверть: 14
Нижняя четверть: 5
Левая четверть: 8
Sample Input 2:

5
1 4 3 4 7
5 6 7 8 4
3 8 5 6 1
1 2 9 4 8
5 6 1 5 8
Sample Output 2:

Верхняя четверть: 18
Правая четверть: 19
Нижняя четверть: 21
Левая четверть: 17
Sample Input 3:

2
99 72
65 11
Sample Output 3:

Верхняя четверть: 0
Правая четверть: 0
Нижняя четверть: 0
Левая четверть: 0'''

# n = int(input())
# sum_left = 0
# sum_top = 0
# sum_right = 0
# sum_lower = 0
# matrix = [[int(c) for c in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (
#                 (i > j and i < n - 1 - j)
#         ) :
#             sum_left += matrix[i][j]
#         if (
#                 (i < j and i < n - 1 - j)
#         ):
#                 sum_top += matrix[i][j]
#
#         if (
#                 (i < j and i > n - 1 - j)
#         ):
#             sum_right += matrix[i][j]
#
#         if (
#                 (i > j and i > n - 1 - j)
#         ):
#             sum_lower += matrix[i][j]
# print(f'Верхняя четверть:', sum_top)
# print(f'Правая четверть:', sum_right)
# print(f'Нижняя четверть:', sum_lower)
# print(f'Левая четверть:', sum_left)

n = int(input())
mtr = [[int(ch) for ch in input().split()] for _ in range(n)]
print('Верхняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i < n - 1 - j)]))
print('Правая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i > n - 1 - j)]))
print('Нижняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i > n - 1 - j)]))
print('Левая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i < n - 1 - j)]))



n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
t = ['Верхняя', 'Правая', 'Нижняя', 'Левая', 0, 0, 0, 0]
for i in range(n):
    for j in range(n):
        if (i != j) and (i != abs(n - j - 1)):
            t[4 + (i > j) + (i > abs(n - j - 1)) + ((i > j) & (j < abs(n - i - 1))) * 2] += x[i][j]

for i in range(4):
    print(t[i] + ' четверть:', t[i + 4])