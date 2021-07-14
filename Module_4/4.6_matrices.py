'''Шахматная доска
На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n×m,
заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную
матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.

Sample Input 1:

3 4
Sample Output 1:

. * . *
* . * .
. * . *
Sample Input 2:

2 2
Sample Output 2:

. *
* .'''

# n, m = map(int,input().split())
# r = [['.*'[(j + i) % 2] for j in range(m)] for i in range(n)]
# for row in r:
#     print(*row)


# n, m = map(int, input().split())
# for i in range(n):
#     row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
#     print(*row)


# n, m = map(int, input().split())
# [print(*[['.', '*'][(i + j)% 2] for j in range(m)]) for i in range(n)]

'''Побочная диагональ
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером 
n×n и заполняет её по следующему правилу:

числа на побочной диагонали равны 1;
числа, стоящие выше этой диагонали, равны 0;
числа, стоящие ниже этой диагонали, равны 2.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.

Sample Input 1:

4
Sample Output 1:

0 0 0 1
0 0 1 2
0 1 2 2
1 2 2 2
Sample Input 2:

2
Sample Output 2:

0 1
1 2'''

# from numpy import sign
# n = int(input())
# a = [[sign(i+j+1-n)+1 for i in range(n)] for j in range(n)]
# for x in a:
#     print(*x)


# n = int(input())
# for i in range(n):
#     row = [0 if i < n - 1 - j else 1 if i == n - 1 - j else 2 for j in range(n)]
#     print(*row)


# def f(i, j, n):
#     if i == n - j - 1:
#         return 1
#     elif i < n - j - 1:
#         return 0
#     else:
#         return 2
#
# n = int(input())
#
# res = [[f(i, j, n) for j in range(n)] for i in range(n)]
#
# for x in res:
#     print(*x)

# n = int(input())
# m = int(input())
#
# args = [iter(range(1, n*m+1)) ]
# l = [ list(t) for t in list(zip(*args)) ]
#
# for i in range(len(l)):
#     print(*l[i], end=' ')
# ***************************************************************************
# n = int(input())
# m = int(input())
# a = []
# for i in range(n):
#     a.append([int(j) for j in range(m*n+1)])
#     print(str(*a[i]).ljust(3), end='')
#

# ***************************************************************************

'''Заполнение змейкой
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером 
n×m заполнив её "змейкой" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. При выводе элементов матрицы, отводите ровно 33 символа на каждый элемент. Для этого используйте
строковый метод ljust().

Sample Input 1:

3 5
Sample Output 1:

1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
Sample Input 2:

5 5
Sample Output 2:

1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25'''
#
# def isZeros(matrix):
#     for char in matrix:
#         if 0 in char:
#             return True
#     return False
#
#
# def check():
#     global DOWNSIDE, UPSIDE, LEFTSIDE, RIGHTSIDE, DOWNDIAG, UPDIAG
#     if i == 0:
#         DOWNSIDE = False
#         UPSIDE = True
#     if i == N - 1:
#         DOWNSIDE = True
#         UPSIDE = False
#     if i != N - 1 and i != 0:
#         DOWNSIDE = False
#         UPSIDE = False
#     if j == 0:
#         LEFTSIDE = True
#         RIGHTSIDE = False
#     if j == M - 1:
#         RIGHTSIDE = True
#         LEFTSIDE = False
#     if j != M - 1 and j != 0:
#         LEFTSIDE = False
#         RIGHTSIDE = False
#
#
# N, M = map(int, input().split())
#
# matrix = [[0] * M for _ in range(N)]
#
# i = 0
# j = 0
#
# UPSIDE = True
# DOWNSIDE = False
# LEFTSIDE = True
# RIGHTSIDE = False
# UPDIAG = False
# DOWNDIAG = True
#
# num = 1
#
# while isZeros(matrix):
#     if matrix[i][j] == 0:
#         matrix[i][j] = num
#         num += 1
#     if (i < N - 1 and LEFTSIDE and DOWNDIAG) or (i < N - 1 and RIGHTSIDE and UPDIAG):
#         i += 1
#         if LEFTSIDE:
#             DOWNDIAG = False
#             UPDIAG = True
#         if RIGHTSIDE:
#             DOWNDIAG = True
#             UPDIAG = False
#         check()
#         continue
#     elif (j < M - 1 and UPSIDE and UPDIAG) or (j < M - 1 and DOWNSIDE and DOWNDIAG):
#         j += 1
#         if UPSIDE:
#             DOWNDIAG = True
#             UPDIAG = False
#         if DOWNSIDE:
#             DOWNDIAG = False
#             UPDIAG = True
#         check()
#         continue
#     elif i > 0 and j < M - 1 and UPDIAG:
#         i -= 1
#         j += 1
#         check()
#         continue
#     elif i < N - 1 and j > 0 and DOWNDIAG:
#         i += 1
#         j -= 1
#         check()
#         continue
#
# for r in range(N):
#     for c in range(M):
#         print(str(matrix[r][c]).ljust(3), end='')
#     print()

# n, m = map(int, input().split())
# for j in range(n):
#     print(' '.join([str(i + 1 + m * j).ljust(3) for i in range(m)][::pow(-1, j)]))

# a, b = map(int, input().split())
# g = iter(range(1, a * b + 1))
# [print(" ".join([f"{next(g):<2}" for j in range(b)][::(-1)**(i % 2)])) for i in range(a)]


# n, m = map(int, input().split())
# matrix = [[0] * m for i in range(n)]
#
# counter = 1
# for i in range(n):
#     if i % 2 == 0:
#         for j in range(m):
#             matrix[i][j] = counter
#             counter += 1
#             if j == m - 1:
#                 break
#     else:
#         for j in range(m - 1, -1, -1):
#             matrix[i][j] = counter
#             counter += 1
#             if j == 0:
#                 break
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end='')
#     print()


'''Заполнение диагоналями 🌶️
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
заполнив её "диагоналями" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. При выводе элементов матрицы, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый
 метод ljust().

Sample Input 1:

3 5
Sample Output 1:

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
Sample Input 2:

3 4
Sample Output 2:

1  2  4  7
3  5  8  10
6  9  11 12'''
# n, m = map(int, input().split())
# c = 1
# l = 0
# a = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(m+n-1):
#     for j in range(n):
#         if ((i-j) > -1) and ((i-j) < m):
#             a[j][i-j]+=c
#             l+=1
#             c+=1
#     l = 0
# for o in a:
#   for o2 in o:
#     print(str(o2).rjust(3), end = '')
#   print()

# n, m = map(int, input().split())
# mt = [[''] * m for i in '1'* n]
# d = 1
# for k in range(1, n + m + 1):
#     for i in range(n):
#         for j in range(m):
#             if i + j + 1 == k:
#                 mt[i][j] = str(d).ljust(3)
#                 d += 1
# [print(*r, sep='') for r in mt]


# n, m = [int(i) for i in input().split()]
# matr = [[0] * m for _ in range(n)]
# k = 1
# for x in range(n * m + 1):
#     for i in range(n):
#         if i > x:
#             continue
#         if x - i >= m:
#             continue
#         matr[i][x - i] = k
#         k += 1
# for row in matr:
#     for c in row:
#         print(str(c).ljust(3), end='')
#     print()

'''Заполнение 3
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив 
её в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и побочной
 диагоналях, остальные позиции матрицы заполнить нулями.

Примечание. При выводе элементов матрицы, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый 
метод ljust().

Sample Input 1:

5
Sample Output 1:

1  0  0  0  1
0  1  0  1  0
0  0  1  0  0
0  1  0  1  0
1  0  0  0  1'''

# n = int(input())
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
#
# for i in range(n):                     # заполняем главную диагональ 1-цами, а побочную 2-ками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 1
#
# for r in range(n):                     # выводим матрицу
#     for c in range(n):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()


# n = int(input())

# matrix =[['0'.ljust(3) for j in range(n)] for b in range(n)]
# for i in range(0, n):
#     for j in range(0, n):
#         if i == j or i == n - j - 1:
#             matrix[i][j] = '1'.ljust(3)
# for row in matrix:
#     print(*row)
#

# n = int(input())
# r = range(n)
# [print(" ".join(f"{int(i == j or (n - i - 1) == j):<2}" for j in r)) for i in r]

'''Заполнение 4
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n×n заполнив 
её в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. При выводе элементов матрицы, отводите ровно 3 символа на каждый элемент. Для этого используйте строковый
 метод ljust().

Sample Input 1:

5
Sample Output 1:

1  1  1  1  1
0  1  1  1  0
0  0  1  0  0
0  1  1  1  0
1  1  1  1  1
Sample Input 2:

7
Sample Output 2:

1  1  1  1  1  1  1
0  1  1  1  1  1  0
0  0  1  1  1  0  0
0  0  0  1  0  0  0
0  0  1  1  1  0  0
0  1  1  1  1  1  0
1  1  1  1  1  1  1'''

# n = int(input())
# matrix = [[0]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i<j and i<n-1-j:
#             matrix[i][j] = 1
#         if i > j and i > n - 1 - j:
#             matrix[i][j] = 1
#         matrix[i][i] = 1
#         matrix[i][n-i-1] = 1
#
# for row in matrix:
#     print(*row)

# n = int(input())
# b = [[0]*n for i in range(n)]
# k = 1
# for i in range(n):
#     for j in range(n):
#         if i<=j and i<=n-j-1:
#             b[i][j]=1
#             b[n-1-i][j]=1
# for r in range(n):
#     for c in range(n):
#         print(str(b[r][c]).ljust(3), end='')
#     print()

# n = int(input())
# [print(*s) for s in
#  [[1 if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j) else 0 for j in range(n)] for i in range(n)]]
# ***************************************

# n, m = map(int, input().split())
# matrix = []
# for i in range(n+1):
#     for j in range(m+1):
#
#        matrix.append([j])
#
# for row in matrix:
#
#     for c in matrix:
#         print(*c, end=" ")


'''Заполнение 1
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером 
n×m и заполняет её числами от 1 до n⋅m в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.

Примечание. При выводе элементов матрицы, отводите ровно 33 символа на каждый элемент. Для этого используйте 
строковый метод ljust().

Sample Input 1:

3 4
Sample Output 1:

1  2  3  4
5  6  7  8
9  10 11 12
Sample Input 2:

4 7
Sample Output 2:

1  2  3  4  5  6  7
8  9  10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28'''

# n, m = map(int,input().split())
# r = 1
# mas = []
# for i in range(n):
#     mas.append([])
#     for j in range(m):
#         mas[i].append(r)
#         r += 1
# for r in range(n):
#     for c in range(m):
#         print(str(mas[r][c]).ljust(3), end='')
#     print()

'''Заполнение 2
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. При выводе элементов матрицы, отводите ровно 3 символа на каждый элемент. Для этого используйте
строковый метод ljust().

Sample Input 1:

3 7
Sample Output 1:

1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21'''

# n, m = [int(i) for i in input().split()]
#
# for i in range(1, (n * m) + 1):
#     print(str(i).ljust(2), end=' ')
#     if i % m == 0:
#         print()

# n, m = map(int,input().split())
# r = 1
# mas = []
# for i in range(n):
#
#     for j in range(m):
#         mas.append([])
#         mas[i].append(r)
#         r += 1
#
# for c in range(n):
#     for r in range(m):
#         print(str(mas[c][r]).ljust(3), end='')
#     print()
#
# n, m = map(int,input().split())
# arr1 = np.arange(n)
# arr2 = np.arange(1,(n+1))
# print((arr1[:,None] + arr2))


'''Заполнение 2
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m 
заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. При выводе элементов матрицы, отводите ровно 3 символа на каждый элемент. Для этого используйте строковый
 метод ljust().

Sample Input 1:

3 7
Sample Output 1:

1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21'''


# n, m = map(int,input().split())
# r = 1
# mas = []
# for j in range(m):
#     mas.append([])
#     for i in range(n):
#         mas[j].append(r)
#         r += 1
# for r in range(n):
#     for c in range(m):
#         print(str(mas[c][r]).ljust(3), end='')
#     print()

# n, m = [int(x) for x in input().split()]
#
# res = [[str(i + j * n + 1).ljust(2) for j in range(m)] for i in range(n)]
#
# for x in res:
#     print(*x)

#
# n, m = list(map(int, input().split()));
#
# for i in range(n):
#     num = i + 1;
#     for j in range(m):
#         print(str(num).ljust(3), end = '');
#         num += n;
#     print()

# n, m = [int(x) for x in input().split()]
#
# for j in range(n):
#     print(' '.join([str(i + 1 % m+1*j).ljust(3) for i in range(m)][::]))


'''Заполнение 5 🌶️
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером 
n×m заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. При выводе элементов матрицы, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый 
метод ljust().

Sample Input 1:

5 5
Sample Output 1:

1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4'''

# n, m = [int(x) for x in input().split()]
# res = [[str((i+1+j)-((i+j)//m)*m).ljust(2)  for j in range(m) ] for i in range(n)]
#
# for x in res:
#     print(*x)


# n, m = map(int, input().split())
# row = list(range(1, m + 1))
# for _ in range(n):
#     print(*row)
#     x = row.pop(0)
#     row.append(x)

# n, m = map(int, input().split())
# a = [i for i in range(1, m+1)]
# for i in range(n):
#     print(*a)
#     a = a[1:] + a[:1]


# r, c = map(int, input().split())
#
# mas = [[0] * c for _ in range(r)]
#
# i = 0
# j = 0
#
# num = 1
#
# right = True
# down = False
# left = False
# up = False
#
#
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

n, c = map(int, input().split()) #строки и столбцы
m = [[0 for _ in range(c)] for _ in range(n)]
i_start, i_end, j_start, j_end = 0, n, 0, c   # интервалы (границы) дыижения по матрице
di, dj = 1, 1  # направления движения
k = 1  # начальное значение заполнителя
i = 0  # костыль для задания первичного движения по первому ряду
while k <= n*c:
    # зполнение вправо
    for j in range(j_start, j_end, dj):
        m[i][j] = str(k).ljust(3)
        k += 1
    dj = -1  # смена направления движения
    i_start += 1  # обрезание заполненного ряда сверху
    if k > n * c:  # прерываение цикла если заолнена вся матрица
        break
    # заполнение вниз
    for i in range(i_start, i_end, di):
        m[i][j] = str(k).ljust(3)
        k += 1
    di = -1  # смена направления движения
    j_end -= 1  # обрезание заполненного столбца справа
    if k > n * c: # прерываение цикла если заолнена вся матрица
        break
    # заполнение влево
    for j in range(j_end - 1, j_start - 1, dj):
        m[i][j] = str(k).ljust(3)
        k += 1
    dj = 1  # смена направления движения
    i_end -= 1 # обрезание заполненного ряда снизу
    if k > n * c: # прерываение цикла если заолнена вся матрица
        break
    # заполнение вверх
    for i in range(i_end - 1, i_start - 1, di):
        m[i][j] = str(k).ljust(3)
        k += 1
    di = 1  # смена направления движения
    j_start += 1 # обрезание заполненного столбца слева
for i in m:
    print(*i)