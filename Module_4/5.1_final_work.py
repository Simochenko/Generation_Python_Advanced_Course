"""
Каждый n-ый элемент
На вход программе подается строка текста, содержащая символы и число n. Из данной строки формируется список.
Напишите программу, которая разделяет список на вложенные подсписки так, что n последовательных элементов принадлежат
разным подспискам.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной
строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Графическая иллюстрация для 1 теста.

Sample Input 1:

a b c d e f g h i j k l m n
3
Sample Output 1:

[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
Sample Input 2:

a b c d e f g h i j k l m n
2
Sample Output 2:

[['a', 'c', 'e', 'g', 'i', 'k', 'm'], ['b', 'd', 'f', 'h', 'j', 'l', 'n']]
Sample Input 3:

a b c d e f g h i j k l m n
1
Sample Output 3:

[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']]
"""

# C = input().split()
# n = int(input())
# def list_slice(S, step):
#     return [S[i::step] for i in range(step)]
# print(list_slice(C,n))

# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)


# s = input().split()
# n = int(input())
# res = [[] for _ in range(n)]
# for i in range(len(s)):
#     res[i % n].append(s[i])
# print(res)


# st = input().split()
# n = int(input())
#
# st1 = []
#
# for i in range(n):
#     st1.append(st[i::n])
#
# print(st1)

'''Максимальный в области 2
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.
Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы побочной диагонали также учитываются.

Sample Input 1:

3
1  4  5
6  7  8
1  1  6
Sample Output 1:

8
Sample Input 2:

4
0  1  4  6
0  0  2  5
0  0  0  7
0  0  0  0
Sample Output 2:

7
'''
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# t_max = max([matrix[j][i] for i in range(0,len(matrix)) for j in range(i+1)])
# print(t_max)

# n = int(input())
# m = [list(map(int, input().split())) for _ in range(n)]
# print(max(m[i][j] for i in range(n) for j in range(n) if i >= n - 1 -j))

# n = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# lst = []
# for i in range(n):
#     lst.append(max(matrix[i][n-i-1:]))
# print(max(lst))


'''Транспонирование матрицы
Напишите программу, которая транспонирует квадратную матрицу.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести транспонированную матрицу.

Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

Примечание 2. Задачу можно решить без использования вспомогательного списка. 

Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

1 4 7
2 5 8
3 6 9'''


# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for row in [*zip(*matrix)]:
#     print(*row)



# n,maxim=int(input()),0
# m=[[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         print(m[j][i],end=' ')
#     print()


# n = int(input())
# m = [list(map(int, input().split())) for _ in range(n)]
# [print(*s) for s in [[m[j][i] for j in range(n)] for i in range(n)]]


# n = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]
#
# for i in zip(*matrix):
#     print(*i)

'''Снежинка
На вход программе подается нечетное натуральное число n. Напишите программу, которая создает матрицу размером 
n×n заполнив её символами . . Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную 
диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе подается нечетное натуральное число (n>3) — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Sample Input 1:

5
Sample Output 1:

* . * . *
. * * * .
* * * * *
. * * * .
* . * . *'''


# n = int(input())
# a = [["."] * n for i in range(n)]
# for i in range(n):
#     a[i][i] = "*"
#     a[n - 1 - i][i] = "*"
#     a[i][n//2] = "*"
#     a[n//2][i] = "*"
# print('\n'.join([' '.join([str(i) for i in row]) for row in a]))

# n = int(input())
# res = [['*' if i == j or i+1+j == n or i == n//2  or j == n//2 else '.' for j in range(n)] for i in range(n)]
#
# for r in res:
#     print(*r, sep = ' ')


# n = int(input())
# arr = [['.'] * n for _ in range(n)]
# mid = n // 2
# for i in range(n):
#     for j in range(n):
#         if i == j or i == n - j - 1 or i == mid or j == mid:
#             arr[i][j] = '*'
#     print(*arr[i])

# n = int(input())
# m = [['.'] * n for _ in range(n)]
# for i in range(n):
#     m[i][i] = '*'
#     m[i][n - 1 - i] = '*'
#     m[n // 2][i] = '*'
#     m[i][n // 2] = '*'
# [print(*s) for s in m]


'''Симметричная матрица
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.

Sample Input 1:

3
0  3  10
4  9  3
7  4  0
Sample Output 1:

YES
Sample Input 2:

3
0  1  2
1  2  7
2  3  4
Sample Output 2:

NO'''

# n = int(input())
# matrix = []
# h=('')
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# for k in range(0,n):
#     for l in range(0,n-k-1):
#         if matrix[k][l] != matrix[n-l-1][n-k-1]:
#             h = ('False')
#             break
# if h != ('False'):
#     print('YES')
# else:
#     print('NO')


# n=int(input())
# m=list()
# for i in range(n):
#     m.append(list(map(int,input().split())))
# res="YES"
# for i in range(n):
#     for j in range(n):
#         if m[i][j]!=m[~j][~i]:
#             res="NO"
# print(res)
#

# n = int(input())
# is_symmetric = True
# t = [input().split() for _ in range(n)]
# for i in range(n):
#     for j in range(n - 1 - i):
#         if t[i][j] != t[n - 1 - j][n - 1 - i]:
#             is_symmetric = False
#             break
#     if not is_symmetric:
#         break
# print('YES' if is_symmetric else 'NO')

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# flag = 'YES'
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
#             flag = 'NO'
#             break
#     if flag == 'NO':
#         break
# print(flag)

'''Латинский квадрат 🌶️
Латинским квадратом порядка nn называется квадратная матрица размером n×n, каждая строка и каждый столбец которой 
содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная квадратная матрица 
латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы:
 n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

Sample Input 1:

4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
Sample Output 1:

YES
Sample Input 2:

3
1 2 3
3 2 1
2 3 4
Sample Output 2:

NO'''

# n = int(input())
# lst = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     lst.append(temp)
#
# def checklatin(latin) :
#
#     numbers = set(range(1, len(latin) + 1))
#
#     if (any(set(row) != numbers for row in latin) or any(set(col) != numbers for col in zip(*latin))) :
#         print ("NO")
#
#     else:
#         print ("YES")
#
# checklatin(lst)

# n = int(input())
# m = [[int(x) for x in input().split()] for _ in range(n)]
# mt = [m[c].copy() for c in range(len(m))]
# for i in range(n):
#     for j in range(n):
#         mt[i][j] = m[j][i]
# sort = list(range(1,n+1))
# ans = 'YES'
# for i in range(n):
#     if sort != sorted(m[i]) or sort != sorted(mt[i]):
#         ans = 'NO'
#         break
# print(ans)

# s = [[int(j) for j in input().split()] for i in range(int(input()))]
# n = list(range(1, len(s)+1))
# y = 1
# for i in range(len(s)):
#     if sorted(s[i]) != n:
#         y = 0
# s1 = [['0'] * len(s) for _ in range(len(s))]
# for i in range(len(s)):
#     for j in range(len(s)):
#         s1[i][j] = s[j][i]
# for i in range(len(s1)):
#     if sorted(s1[i]) != n:
#         y = 0
# print('YES' if y == 1 else 'NO')


'''Ходы ферзя
На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. Клетку, 
где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните 
точками.

Формат входных данных
На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации (то есть в виде e4, где сначала 
записывается номер столбца (буква от a до h, слева направо), затем номер строки (цифра от 11 до 88, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

Sample Input 1:

c4
Sample Output 1:

. . * . . . * .
. . * . . * . .
* . * . * . . .
. * * * . . . .
* * Q * * * * *
. * * * . . . .
* . * . * . . .
. . * . . * . .'''

from math import fabs

# board = [['.'] * 8 for _ in range(8)]
# pos = input()
# g =  int(pos[1])   # строчка
# v = 'abcdefgh'.find(pos[0])   # столбец
#
#
# board[v][g - 1] = 'Q'
#
# for i in range(0, 8):
#     for j in range(1, 9):
#         if (i != v or j != g) and ((i == v or j == g) or (abs(i - v) == abs(j - g))):
#             board[i][j - 1] = '*'
#
# board = list(zip(*board))
# for x in reversed(board):
#     print(' '.join(x))

# pos = input()
# x = 8 - int(pos[1])
# y = 'abcdefgh'.find(pos[0])
# arr = [['.'] * 8 for _ in range(8)]
# for i in range(8):
#     for j in range(8):
#         if i == x and j == y:
#             arr[i][j] = "Q"
#         elif i == x or j == y or abs(i - x) == abs(j - y):
#             arr[i][j] = "*"
#     print(*arr[i])

# l = input()
# col = l[0]
# st = 8 - int(l[1])
# doska = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
# col = doska[col]
# s = [['.'] * 8 for _ in range(8)]
# for i in range(len(s)):
#     for j in range(len(s)):
#         if st == i or col == j or abs(st-i) == abs(col-j):
#             s[i][j] = '*'
# s[st][col] = 'Q'
# [print(*i) for i in s]


'''Диагонали параллельные главной
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и заполняет 
её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 0;
на двух диагоналях, прилегающих к главной, число 1;
на следующих двух диагоналях число 2, и т.д.
Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Sample Input 1:

5
Sample Output 1:

0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0'''


# n = int(input())
# a = [[abs(i - j) for j in range(n)] for i in range(n)]
# for row in a:
#     print(' '.join([str(i) for i in row]))

# n = int(input())
# arr = [[abs(i - j) for j in range(n)] for i in range(n)]
# for row in arr:
#     print(*row)

# n = int(input())
# a = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         a[i][j] = abs(j-i)
#
# for i in a:
#     print(*i)


'''Заполнение спиралью 🌶️🌶️
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
заполнив её "спиралью" в соответствии с образцом.
Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.
Примечание. При выводе элементов матрицы, отводите ровно 33 символа на каждый элемент.
Sample Input 1:

4 5
Sample Output 1:

1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8'''

# r, c = [int(i) for i in input().split()]
# mas = [[0] * c for _ in range(r)]
# i = 0
# j = 0
# num = 1
# right = True
# down = False
# left = False
# up = False

# def zero(mas):
#     for row in mas:
#         if 0 in row:
#             return True
#     return False
#
#
# while zero(mas):
#     if mas[i][j] == 0:
#         mas[i][j] = num
#         num += 1
#
#     if j < c - 1 and mas[i][j + 1] == 0 and right:
#         j += 1
#
#     elif i < r - 1 and mas[i + 1][j] == 0 and down:
#         i += 1
#
#     elif j >= 0 and mas[i][j - 1] == 0 and left:
#         j -= 1
#
#     elif i >= 0 and mas[i - 1][j] == 0 and up:
#         i -= 1
#     elif right:
#         right = False
#         down = True
#
#     elif down:
#         down = False
#         left = True
#
#     elif left:
#         left = False
#         up = True
#
#     elif up:
#         up = False
#         right = True
#
# for row in mas:
#     print(*row)

# n,m = map(int,input().split())
# l = [[0 for i in range(m)] for i in range(n)]
# c = 0
# i = 0
# j = -1
# while c != n*m:
#     while j < m - 1 and l[i][j+1] == 0:   # двигаюсь влево
#         j += 1
#         c += 1
#         l[i][j] = c
#     while i < n - 1 and l[i+1][j] == 0:   # двигаюсь вниз
#        i += 1
#        c += 1
#        l[i][j] = c
#     while j > 0 and l[i][j-1] == 0 :   # двигаюсь вправо
#        j -= 1
#        c += 1
#        l [i][j] = c
#     while i > 0 and l[i - 1][j] == 0:   # двигаюсь вверх
#        i -= 1
#        c += 1
#        l[i][j] = c
# for row in l:
#     print(*row)

# n, c = map(int, input().split()) #строки и столбцы
# m = [[0 for _ in range(c)] for _ in range(n)]
# i_start, i_end, j_start, j_end = 0, n, 0, c   # интервалы (границы) дыижения по матрице
# di, dj = 1, 1  # направления движения
# k = 1  # начальное значение заполнителя
# i = 0  # костыль для задания первичного движения по первому ряду
# while k <= n*c:
#     # зполнение вправо
#     for j in range(j_start, j_end, dj):
#         m[i][j] = str(k).ljust(3)
#         k += 1
#     dj = -1  # смена направления движения
#     i_start += 1  # обрезание заполненного ряда сверху
#     if k > n * c:  # прерываение цикла если заолнена вся матрица
#         break
#     # заполнение вниз
#     for i in range(i_start, i_end, di):
#         m[i][j] = str(k).ljust(3)
#         k += 1
#     di = -1  # смена направления движения
#     j_end -= 1  # обрезание заполненного столбца справа
#     if k > n * c: # прерываение цикла если заолнена вся матрица
#         break
#     # заполнение влево
#     for j in range(j_end - 1, j_start - 1, dj):
#         m[i][j] = str(k).ljust(3)
#         k += 1
#     dj = 1  # смена направления движения
#     i_end -= 1 # обрезание заполненного ряда снизу
#     if k > n * c: # прерываение цикла если заолнена вся матрица
#         break
#     # заполнение вверх
#     for i in range(i_end - 1, i_start - 1, di):
#         m[i][j] = str(k).ljust(3)
#         k += 1
#     di = 1  # смена направления движения
#     j_start += 1 # обрезание заполненного столбца слева
# for i in m:
#     print(*i)
#
# # put your python code here
# n, m = [int(_) for _ in input().split()]
# matrix = []
#
# for i in range(n):
#     temp = [0] * m
#     matrix.append(temp)
#
# num = 1
#
# def one_side(a, b, step, r, c):
#     # a - нач. знач. цикла, b - кон. знач. цикла, step - шаг
#     # r - значение для первого индекса матрицы
#     # с - значение для второго индекса матрицы
#     # если r или c равно 'v', то для индекса используем переменную цикла
#     global num
#     for i in range(a, b, step):
#         if c == 'v':
#             matrix[r][i] = num
#         elif r == 'v':
#             matrix[i][c] = num
#         num += 1
#     return i
#
# for i in range(int(n / 2) + 1):
#     j = one_side(i, m - i, 1, i, 'v')  # верхняя строка слева направо
#     if num > n * m:
#         break
#     k = one_side(i + 1, n - i, 1, 'v', j)  # правый столбец сверху вниз
#     if num > n * m:
#         break
#     x = one_side(m - i - 2, i - 1, -1, k, 'v')  # нижняя строка справа налево
#     if num > n * m:
#         break
#     one_side(n - i - 2, i, -1, 'v', i)  # левый столбец снизу вверх
#     if num > n * m:
#         break
#
# for row in matrix:
#     for j in range(m):
#         print(str(row[j]).ljust(3), end=' ')
#     print()