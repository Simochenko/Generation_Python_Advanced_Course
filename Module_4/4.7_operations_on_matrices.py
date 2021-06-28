'''Тема урока: операции над матрицами
Сложение матриц
Умножение матрицы на число
Умножение матриц
Аннотация. Урок посвящен основным операциям над матрицами в математике.

Сложение матриц
При сложении матриц AA и BB получается такая матрица CC, каждый элемент которой представляет собой сумму пары соответствующих элементов исходных матриц AA и BB. Складывать можно только матрицы одинаковой размерности (n \times mn ×m), с равным количеством строк и столбцов. Таким образом, математически сумма матриц выглядит так:
C_{n \times m} = A_{n \times m} + B_{n \times m}
C
n×m
​
 =A
n×m
​
 +B
n×m
​

Каждый элемент искомой матрицы равен сумме соответствующих элементов заданных матриц:

c_{ij} = a_{ij} + b_{ij}
c
ij
​
 =a
ij
​
 +b
ij
​

Пример. Даны две матрицы:

A=\begin{bmatrix} 2& -3&1\\ 5 & 4 &-2 \end{bmatrix}, \, \, \, B=\begin{bmatrix} 4& 2&-5\\ -4 & 1 &3 \end{bmatrix}
A=[
2
5
​

−3
4
​

1
−2
​
 ],B=[
4
−4
​

2
1
​

−5
3
​
 ]
Найти сумму матриц A+BA+B.
Решение. Имеем

A + B = \begin{bmatrix} 2& -3&1\\ 5 & 4 &-2 \end{bmatrix} + \begin{bmatrix} 4& 2&-5\\ -4 & 1 &3 \end{bmatrix} = \begin{bmatrix} 6& -1&-4\\ 1 & 5 & 1 \end{bmatrix}
A+B=[
2
5
​

−3
4
​

1
−2
​
 ]+[
4
−4
​

2
1
​

−5
3
​
 ]=[
6
1
​

−1
5
​

−4
1
​
 ]

Свойства сложения матриц
Коммутативность – результат сложения матриц не зависит от их перестановки:
A+B = B+A;
A+B=B+A;
Ассоциативность – результат сложения матриц не зависит от расстановки скобок:
A + (B + C) = (A + B) + C;
A+(B+C)=(A+B)+C;
Сложение с нулевой матрицей – для любой матрицы существует нейтральный элемент, которым является нулевая матрица, сложение с которым не изменяет исходную матрицу. Нулевая матрица – матрица, все элементы которой имеют нулевое значение:
A+0 = 0 + A = A;
A+0=0+A=A;
Существование противоположной матрицы – для ненулевой матрицы AA всегда есть матрица -A−A, сложение с  которой даст в результате нулевую матрицу:
A+(-A) = 0.
A+(−A)=0.
Умножение матрицы на число
Операция умножения матрицы AA на число kk заключается в построении матрицы kA = [k \cdot a_{ij}]kA=[k⋅a
ij
​
 ]. Умножать на число можно матрицы любого размера. В результате умножения получается матрица того же размера, что исходная.

Произведение матрицы AA на число kk – результирующая матрица B = kAB=kA того же размера, полученная умножением каждого из элементов a_{ij}a
ij
​
  исходной матрицы на заданное число.

Пример. Даны матрица AA и число kk:

A=\begin{bmatrix} 5& -2& 4\\ 3 & 1 &-3 \end{bmatrix}, \, \, \, k=7
A=[
5
3
​

−2
1
​

4
−3
​
 ],k=7
Найти произведение матрицы и числа.
Решение. Имеем

k\cdot A = 7\cdot\begin{bmatrix} 5& -2& 4\\ 3 & 1 &-3 \end{bmatrix} = \begin{bmatrix} 35& -14&28\\ 21 & 7 & -21 \end{bmatrix}
k⋅A=7⋅[
5
3
​

−2
1
​

4
−3
​
 ]=[
35
21
​

−14
7
​

28
−21
​
 ]

Свойства умножения матрицы на число
Единица – нейтральное число умножения любой матрицы, результат умножения на нейтральное число – исходная матрица:
1 \times A = A;
1×A=A;
Результат умножения любой матрицы на ноль – нулевая матрица, все элементы которой равны нулю:
0 \times A = 0;
0×A=0;
Для матриц одного размера и действительного числа выполняется свойство дистрибутивности умножения относительно сложения:
k \times (A + B) = k \times A + k \times B;
k×(A+B)=k×A+k×B;
Для любой матрицы и суммы действительных чисел выполняется свойство дистрибутивности:
(k + n) \times A = k \times A + n \times A;
(k+n)×A=k×A+n×A;
Для любой матрицы и произведения любых действительных чисел выполняется свойство ассоциативности умножения:
(k \times n) \times A = k \times (n \times A).
(k×n)×A=k×(n×A).
Умножение матрицы на матрицу
Умножение двух матриц AA и BB – вычисление результирующей матрицы CC, каждый элемент c_{ij}c
ij
​
  которой равен сумме произведений элементов соответствующих строки первой матрицы a_{ik}a
ik
​
  и столбца второй матрицы b_{kj}b
kj
​
 .

Одну матрицу можно умножать на другую только тогда, когда количество столбцов в первой матрице совпадает с количеством
строк во второй матрице. То есть, матрицы должны быть согласованы по размерности. Результат умножения матрицы размера
n\times mn×m на матрицу размером m\times km×k – матрица размером n\times kn×k.

Итак, произведение матрицы A_{n\times m}A
n×m
​
  на матрицу B_{m\times k}B
m×k
​
  – матрица C_{n\times k}C
n×k
​
 , элемент c_{ij}c
ij
​
  которой, находящийся в ii-ой строке и jj-ом столбце, равен сумме произведений элементов ii-ой строки матрицы AA на соответствующие элементы jj-ого столбца матрицы BB.

Каждый элемент матрицы C_{n\times k}C
n×k
​
  равен:

c_{ij} = \sum_{k=1} ^{m} a_{ik} \cdot b_{kj} = a_{i1}\cdot b_{1j} + a_{i2}\cdot b_{2j}+\ldots +a_{im}\cdot b_{mj}
c
ij
​
 =
k=1
∑
m
​
 a
ik
​
 ⋅b
kj
​
 =a
i1
​
 ⋅b
1j
​
 +a
i2
​
 ⋅b
2j
​
 +…+a
im
​
 ⋅b
mj
​

где kk принимает значение от 11 до mm.

Пример. Даны две матрицы AA и BB:

A=\begin{bmatrix} 2& -3&1\\ 5 & 4 &-2 \end{bmatrix}, \, \, \, B=\begin{bmatrix} -7& 5 \\ 2 &-1 \\ 4 &3 \end{bmatrix}
A=[
2
5
​

−3
4
​

1
−2
​
 ],B=
⎣
⎡
​

−7
2
4
​

5
−1
3
​

⎦
⎤
​

Найти произведение матриц A\times BA×B.
Решение. При перемножении матрицы A_{2\times 3}A
2×3
​
  на матрицу B_{3\times 2}B
3×2
​
  мы получаем матрицу C_{2\times 2}C
2×2
​
 . Имеем:

c_{11} = 2\cdot(-7) + (-3)\cdot 2 + 1 \cdot 4 = -16, \quad c_{12} = 2\cdot 5 + (-3)\cdot(-1) + 1\cdot 3 = 16\\ c_{21} = 5\cdot(-7) + 4\cdot 2 + (-2) \cdot 4 = -35, \quad c_{22} = 5\cdot 5 + 4\cdot(-1) + (-2)\cdot 3 = 15
c
11
​
 =2⋅(−7)+(−3)⋅2+1⋅4=−16,c
12
​
 =2⋅5+(−3)⋅(−1)+1⋅3=16
c
21
​
 =5⋅(−7)+4⋅2+(−2)⋅4=−35,c
22
​
 =5⋅5+4⋅(−1)+(−2)⋅3=15
Таким образом

A \cdot B=\begin{bmatrix} 2& -3&1\\ 5 & 4 &-2 \end{bmatrix} \cdot\begin{bmatrix} -7& 5 \\ 2 &-1 \\ 4 &3 \end{bmatrix} =\begin{bmatrix} -16& 16\\ -35 & 15 \end{bmatrix}
A⋅B=[
2
5
​

−3
4
​

1
−2
​
 ]⋅
⎣
⎡
​

−7
2
4
​

5
−1
3
​

⎦
⎤
​
 =[
−16
−35
​

16
15
​
 ]

Свойства умножения матриц
Ассоциативность – (A\times B)\times C = A\times (B\times C)(A× B)× C =A×(B× C);
Дистрибутивность –
A\times (B + C) = A\times B + A\times C, \, (A+B)\times C = A\times C + B \times C;
A×(B+C)=A×B+A×C,(A+B)×C=A×C+B×C;
Ассоциативность и коммутативность относительно умножения на число –
(k\times A)\times B = k\times (A\times B) = A\times (k\times B);
(k×A)×B=k×(A×B)=A×(k×B);
В общем случае умножение матриц не коммутативно –
A\times B \neq B\times A;
A×B

=B×A;
Примечания
Примечание 1. Демонстрация операции перемножения матриц.'''

'''Сложение матриц
Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах, 
затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу.

Sample Input 1:

2 4
1 2 3 4
5 6 7 1

3 2 1 2
1 3 1 3
Sample Output 1:

4 4 4 6
6 9 8 4'''

# n, m = map(int, input().split())
# resX = []
# for i in range(n):
#     resX.append([int(j) for j in input().split()])
# h = input()
# resY = []
# for i in range(n):
#     resY.append([int(j) for j in input().split()])
#
# result = []
# for sublist in zip(resX, resY):
#     temp = []
#     for numbers in zip(sublist[0], sublist[1]):
#         temp.append(sum(numbers))
#     result.append(temp)
#
# for r in result:
#     print(*r)

# n, m = map(int, input().split())
# arra = [list(map(int, input().split())) for _ in range(n)]
# input()
# arrb = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     print(*list(x + y for x, y in zip(arra[i], arrb[i])))

# n, m = [int(x) for x in input().split()]
#
# A = [[int(x) for x in input().split()] for _ in range(n)]
# input()
# B = [[int(x) for x in input().split()] for _ in range(n)]
#
# C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
#
# for x in C:
#     print(*x)

'''Умножение матриц
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем 
элементы первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы 
затем элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу.

Sample Input 1:

2 2
1 2
3 2

2 2
3 2
1 1
Sample Output 1:

5 4
11 8'''

# n, m = map(int, input().split())
# resX = []
# for i in range(n):
#     resX.append([int(j) for j in input().split()])
# h = input()
# m, k = map(int, input().split())
# resY = []
# for i in range(m):
#     resY.append([int(j) for j in input().split()])
#
# def matrixmult (A, B):
#     C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 C[i][j] += A[i][k]*B[k][j]
#     return C
# for x in matrixmult(resX, resY):
#     print(*x)

# n, m = [int(i) for i in input().split()]
# a = [[int(i) for i in input().split()] for _ in range(n)]
# input()
# x, k = [int(i) for i in input().split()]
# b = [[int(i) for i in input().split()] for _ in range(x)]
# c = [[0 for _ in range(k)] for _ in range(n)]
# for i in range(n):
#     for j in range(k):
#         c[i][j] = sum(a[i][y] * b[y][j] for y in range(m))
# for row in c:
#     print(*row)


# n, m = [int(i) for i in input().split()]
# matrixA = [[int(i) for i in input().split()] for _ in range(n)]
# input()
# m, k = [int(i) for i in input().split()]
# matrixB = [[int(i) for i in input().split()] for _ in range(m)]
#
# matrixC = [[0] * k for _ in range(n)]
#
# for i in range(n):
#     for j in range(k):
#         for q in range(m):
#             matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
#
# for row in matrixC:
#     print(*row)

'''Возведение матрицы в степень
Напишите программу, которая возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы,
 затем натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу.

Sample Input 1:

3
1 2 3
4 5 6
7 8 9
2
Sample Output 1:

30 36 42
66 81 96
102 126 150'''

# import numpy as np
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# k = int(input())
# result = np.linalg.matrix_power(matrix, k)
# for row in result:
#     print(*row)

# n = int(input())
# m1 = [[int(j) for j in input().split()] for i in range(n)]
# m = int(input())
# res = m1
#
# for l in range(m-1):
#     res = [[sum([res[i][p] * m1[p][j] for p in range(n)]) for j in range(n)] for i in range(n)]
#
# for r in res:
#     print(*r)

n = int(input())
s1 = []
s3 = []
for _ in range(n):  # 1 матрица
    s1.append(list(map(int, input().split())))
s2 = s1
m = int(input())
z = 0
for r in range(m - 1):
    s3 = []
    for i in range(n):
        s3.append([])
        for j in range(n):
            for p in range(n):
                z += s1[i][p] * s2[p][j]
            s3[i].append(z)
            z = 0
    s2 = s3
for i in range(n):
    print(*s3[i])