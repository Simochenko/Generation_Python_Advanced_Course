'''Таблица умножения
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте
 матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 33 символа (для этого используйте
 строковый метод ljust()).

Sample Input 1:

4
6
Sample Output 1:

0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8  10
0  3  6  9  12 15
Sample Input 2:

3
5
Sample Output 2:

0  0  0  0  0
0  1  2  3  4
0  2  4  6  8
Sample Input 3:

6
6
Sample Output 3:

0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8  10
0  3  6  9  12 15
0  4  8  12 16 20
0  5  10 15 20 25'''

# n = int(input())
# m = int(input())
#
# res = [[0 for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         res[i][j] = i * j
# for r in range(n):
#     for c in range(m):
#         print(str(res[r][c]).ljust(3), end='')
#     print()

# n, m = int(input()), int(input())
# for i in range(n):
#     for j in range(m):
#         print(f'{i * j:<3}', end="")
#     print()

# [print(*[str(i * j).ljust(3) for j in d[1]]) for d in [[range(int(input())) for _ in 'nm']] for i in d[0]]

'''Максимум в таблице
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем n строк
 по m целых чисел в каждой, отделенных символом пробела.

Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

Формат входных данных
На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице, затем сами
 элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы. Если 
таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у
 которого меньше номер столбца.

Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.

Sample Input 1:

3
4
0 3 2 4
2 3 5 5
5 1 2 3
Sample Output 1:

1 2
Sample Input 2:

3
3
5 3 4
2 3 0
4 1 5
Sample Output 2:

0 0
Sample Input 3:

2
8
4 3 4 4 1 2 2 3
2 3 0 3 3 4 4 5
Sample Output 3:

1 7'''

# n = int(input())
# m = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]
# max_i, max_j = 0, 0
# all_max = a[0][0]
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > all_max:
#             all_max = a[i][j]
#             max_i, max_j = i, j
# print(max_i, max_j)

# n, m = int(input()), int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# lst1 = [max(elem) for elem in matrix]
# elem_max = max(lst1)
# row_max = lst1.index(elem_max)
# column_max = matrix[row_max].index(elem_max)
# print(row_max, column_max)


'''Обмен столбцов
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа nn и mm — количество строк и столбцов в матрице,
 затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.

Sample Input 1:

3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1
Sample Output 1:

12 11 13 14
22 21 23 24
32 31 33 34
Sample Input 2:

3
3
11 12 13
21 22 23
31 32 33
2 1
Sample Output 2:

11 13 12 
21 23 22 
31 33 32 '''

# n = int(input())
# m = int(input())
# a = []
# for i in range(n):
#     a.append([int(j) for j in input().split()])
# c1, c2 = map(int, input().split())
# for i in range(n):
#     a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
#     print(*a[i], sep=" ")


# row, col = input().split()
#
# matrix = [[int(x) for x in input().split()] for _ in range(int(row))]
#
# inx1,  inx2 = input().split()
# inx1, inx2 = int(inx1), int(inx2)
#
# for m in matrix:
#     m[inx1], m[inx2] = m[inx2], m[inx1]
#
# for mx in matrix: print(*mx)


'''Симметричная матрица
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы 
построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.

Sample Input 1:

3
0 1 2
1 2 3
2 3 4
Sample Output 1:

YES
Sample Input 2:

3
0 1 2
1 2 7
2 3 4
Sample Output 2:

NO
Sample Input 3:

2
1 2
3 4
Sample Output 3:

NO'''

# n = int(input())
#
# a = []
# for i in range(n):
#     row = input().split()
#     for j in range(n): row[j] = int(row[j])
#     a.append(row)
# m = 0
# for i in range(1, n):
#     k = 0
#     for j in range(i):
#         if (a[i][j] == a[j][i]): k = k + 1;
#     if k == i: m = m + 1
# if (m == n - 1):
#     print('YES')
# else:
#     print('NO')

# n = int(input())
#
# matrix = [[int(item) for item in input().split()] for _ in range(n)]
# matrix_T = [[matrix[i][j] for i in range(n)] for j in range(n)]
#
# if (matrix == matrix_T):
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# is_symmetric = True
# t = [input().split() for _ in range(n)]
# for i in range(n):
#     for j in range(i):
#         if t[i][j] != t[j][i]:
#             is_symmetric = False
#             break
#     if not is_symmetric:
#         break
# print('YES' if is_symmetric else 'NO')

'''Обмен диагоналей
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной
 диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
  элемент на главной диагонали и на побочной диагонали).

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы 
построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.

Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

7 2 9 
4 5 6 
1 8 3 
Sample Input 2:

2
1 2
4 5
Sample Output 2:

4 5
1 2'''

# n = int(input())
# a = [input().split() for i in range(n)]
# for i in range(n):
#     a[i][i], a[-(i+1)][i]=a[-(i+1)][i], a[i][i]
# print('\n'.join([' '.join([str(i) for i in row]) for row in a]))


# n = int(input())
#
# res = [[int(x) for x in input().split()] for _ in range(n)]
#
# for j in range(n):
#     res[j][j], res[n - j - 1][j] = res[n - j - 1][j], res[j][j]
#
# for x in res:
#     print(*x)

'''Зеркальное отображение
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной
 оси симметрии.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы
 построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.

Sample Input 1:

4
1 2 3 4
5 6 7 8
8 6 4 2
3 4 5 6
Sample Output 1:

3 4 5 6
8 6 4 2
5 6 7 8
1 2 3 4
Sample Input 2:

3
1 2 3
4 5 6
7 8 9
Sample Output 2:

7 8 9
4 5 6
1 2 3'''

# from numpy import flipud
# n = int(input())
# matrix = [[int(_) for _ in input().split()] for _ in range(n)]
# for row in flipud(matrix):
#     print(*row)

# n = int(input())
# res = [[int(x) for x in input().split()] for _ in range(n)]
# for j in range(n - 1, -1, -1):
#     print(*res[j])

# n = int(input())

# matrix = [[int(item) for item in input().split()] for _ in range(n)]
# matrix.reverse()
#
# for row in matrix:
#     print(*row)

'''Магический квадрат
Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная из чисел 1, 2, 3,…,n **2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
   которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: 
n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

Sample Input 1:

3
8 1 6
3 5 7
4 9 2
Sample Output 1:

YES
Sample Input 2:

3
8 2 6
3 5 7
4 9 1
Sample Output 2:

NO
Sample Input 3:

3
4 9 2
3 5 7
8 1 6
Sample Output 3:

YES'''

# def is_magic_square(matrix, S, N):
#     return (all(sum(row) == S for row in matrix)
#             and all(sum(column) == S for column in zip(*matrix))
#             and sum(matrix[i][i] for i in range(N)) == S
#             and sum(matrix[i][N-1-i] for i in range(N)) == S
#             and set(x for row in matrix for x in row) == set(range(1, N**2 + 1)))
#
# N = int(input())
# try:
#     matrix = [list(map(int, input().split())) for _ in range(N)]
# except ValueError:  # non integer
#     print('NO')
# else:
#     print('YES' if N == 0 or is_magic_square(matrix, sum(matrix[0]), N) else 'NO')


# import numpy as np
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# v = {*np.sum(a, axis=1), *np.sum(a, axis=0), sum(np.diag(a)), sum(np.fliplr(a).diagonal())}
# if len(v) == 1:
#     print('YES')
# else:
#     print('NO')

'''Поворот матрицы
Напишите программу, которая поворачивает квадратную матрицу чисел на 90^∘
  по часовой стрелке.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы
 построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

7 4 1 
8 5 2 
9 6 3 
Sample Input 2:

4
1 9 4 2
3 8 1 5
6 7 4 6
1 9 7 8
Sample Output 2:

1 6 3 1
9 7 8 9
7 4 1 4
8 6 5 2
Sample Input 3:

2
1 2
3 4
Sample Output 3:

3 1
4 2'''

# from numpy import rot90
# n = int(input())
# matrix = [[int(_) for _ in input().split()] for _ in range(n)]
# for row in rot90(matrix,3):
#     print(*row)

# matrix = []
#
# for _ in range(int(input())):
#     matrix.append([int(x) for x in input().split()])
#
# for row in zip(*matrix[::-1]):
#     print(*row)

# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# for i in range(n):
#     for j in range(n - 1, -1, -1):
#         print(matrix[j][i], end=' ')
#     print()

# print(*[" ".join(i) for i in list(zip(*reversed([input().split() for i in range(int(input()))])))], sep="\n")

# row = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# pos = input()
# posy = row[pos[0]]
# posx = int(pos[1])-1
# desk = []
# for i in range(8):
#     list = []
#     for j in range(8):
#         list.append('.')
#     desk.append(list)
# desk[posx][posy] = 'N'
# if posx > 1:
#     if posy > 0:
#         desk[posx - 2][posy - 1] = '*'
#     if posy < 7:
#         desk[posx - 2][posy + 1] = '*'
# if posx < 6:
#     if posy > 0:
#         desk[posx + 2][posy - 1] = '*'
#     if posy < 7:
#         desk[posx + 2][posy + 1] = '*'
# if posy > 1:
#     if posx > 0:
#         desk[posx - 1][posy - 2] = '*'
#     if posx < 7:
#         desk[posx + 1][posy - 2] = '*'
# if posy < 6:
#     if posx > 0:
#         desk[posx - 1][posy + 2] = '*'
#     if posx < 7:
#         desk[posx + 1][posy + 2] = '*'
# for i in range(8):
#     print(*(desk[i]))

'''Шахматная доска
На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n×m, 
заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную 
матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

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

