'''Тема урока: модуль fraction
Модуль fractions
Тип данных Fraction
Аннотация. Урок посвящен модулю fractions и типу данных Fraction.

В этом уроке мы изучим числовой тип данных Fraction, который представляет из себя обыкновенную дробь, с заданными 
числителем и знаменателем;

Рациональное число
Рациональное число – это число, которое можно представить в виде дроби \dfrac{m}{n} 
n
m
​
 , где m, nm,n соответственно, числитель и знаменатель, которые имеют целочисленное значение, при этом знаменатель
  не равен нулю. 

Например, в дроби \dfrac{5}{6} 
6
5
​
  числитель m = 5m=5, а знаменатель n=6n=6.

   Знаменатель дроби показывает количество равных частей, а числитель дроби показывает, сколько из них взято.



Тип данных Fraction
Для работы с рациональными числами в Python используется тип данных Fraction. Тип данных Fraction как и Decimal
 реализован программно, поэтому он в разы медленнее встроенных числовых типов данных int и float. Тип данных Fraction
  неизменяемый. Операции над данными этого типа приводят к созданию новых объектов, при этом старые не меняются.

Чтобы использовать возможности типа данных Fraction нужно предварительно подключить модуль fractions:

from fractions import Fraction
Создание Fraction
Создать Fraction число можно несколькими способами:

из целых чисел, передав значения числителя и знаменателя дроби,
из строки на основании десятичного представления;
из строки на основании обыкновенной дроби;
из числа с плавающей точкой (не рекомендуется).
Приведенный ниже программный код создает Fraction числа на основе целых чисел и строк:

from fractions import Fraction

num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')

print(num1, num2, num3, sep='\n')
и выводит:

3/4
11/20
1/9
Нужно быть очень внимательным при создании Fraction чисел из чисел с плавающей точкой (float), потому что float числа
 округляются внутри до ближайшего возможного, а Fraction об этом ничего не знает, поэтому копирует содержимое float.

Приведенный ниже программный код создает Fraction число на основе числа с плавающей точкой:

from fractions import Fraction

num = Fraction(0.34)

print(num)
вместо ожидаемого вывода:

17/50
 код выводит:

6124895493223875/18014398509481984
Не рекомендуется создавать Fraction числа из float чисел. В Fraction попадет уже неправильно округленное число.
 Создавать Fraction числа нужно из целых чисел, либо из строк!

Обратите внимание на то, что при создании рационального числа Fraction, автоматически происходит сокращение числителя и
 знаменателя дроби.

Приведенный ниже код:

from fractions import Fraction

num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')

print(num1, num2, num3, sep='\n')
выводит:

1/2
3/4
1/4
Так же стоит обратить внимание на вывод дробей, являющимися целыми числами.

Приведенный ниже код:

from fractions import Fraction

num1 = Fraction(5, 1)        # 5/1 = 5
num2 = Fraction(23, 23)      # 23/23 = 1

print(num1, num2, sep='\n')
выводит:

5
1
Сравнение Fraction чисел
Fraction числа можно сравнивать между собой точно так же, как и любые другие числа. Доступны 66 основных операторов 
сравнения:

>: больше;
<: меньше;
>=: больше либо равно;
<=: меньше либо равно;
==:  в точности равно;
!=: не равно.
Приведенный ниже код:

from fractions import Fraction

num1 = Fraction(1, 2)        # 1/2
num2 = Fraction(15, 30)      # 15/30=1/2
num3 = Fraction(3, 5)        # 3/5
num4 = Fraction(5, 3)        # 5/3
num5 = 1
num6 = 0.8


print(num1 == num2)
print(num1 != num4)
print(num2 > num3)
print(num4 <= num1)
print(num1 < num5)
print(num6 > num4)
выводит:

True
True
False
False
True
False
Обратите внимание на то, что мы можем сравнивать Fraction числа и целые числа (числа с плавающей точкой) без явного 
приведения типов. 

Арифметические операции над Fraction числами
Тип данных Fraction отлично интегрирован в язык Python. С Fraction числами работают все привычные операции: сложение, 
вычитание, умножение, деление, возведение в степень.

Приведенный ниже код:

from fractions import Fraction

num1 = Fraction('1/10')
num2 = Fraction('2/3')

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
выводит:

23/30
-17/30
1/15
3/20
Мы также можем совершать арифметические операции над Fraction и целыми числами (миксовать Fraction и int), но не
 рекомендуется смешивать их с float.

Приведенный ниже код:

from fractions import Fraction

num = Fraction('3/8')

print(num + 1)
print(num - 1)
print(num * 2)
print(num ** 4)
выводит:

11/8
-5/8
3/4
81/4096
Обратите внимание, на то, что операция возведения в степень (**) для Fraction чисел может возвращать вещественный
 результат.

Приведенный ниже код:

from fractions import Fraction

num1 = Fraction('3/8')
num2 = Fraction('1/2')

print(num1 ** num2)
выводит:

0.6123724356957945
По сути тут происходит вычисление числа \left(\dfrac{3}{8}\right)^{\frac12} = \sqrt{\dfrac{3}{8}} \approx
 0.6123724356957945( 
8
3
​
 ) 
2
1
​
 
 = 
8
3
​
 
​
 ≈0.6123724356957945.

Математические функции
Fraction числа можно передавать как аргументы функций, ожидающих float. Тогда они будут преобразованы во float. К 
примеру, модуль math оперирующий float числами, может работать и с Fraction числами.

Приведенный ниже код:

from fractions import Fraction
from math import *

num1 = Fraction('1.44')
num2 = Fraction('0.523')

print(sqrt(num1))
print(sin(num2))
print(log(num1 + num2))
выводит:

1.2
0.4994813555186418
0.6744739152943241
Важно понимать, что результатом работы функций модуля math являются float числа, а не Fraction.

Свойства numerator и denominator
Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator.

Приведенный ниже код:

from fractions import Fraction

num = Fraction('5/16')

print('Числитель дроби равен:', num.numerator)
print('Знаменатель дроби равен:', num.denominator)
выводит:

Числитель дроби равен: 5
Знаменатель дроби равен: 16
В Python 3.8 появился метод as_integer_ratio(), который возвращает кортеж, состоящий из числителя и знаменателя 
данного Fraction числа.

Приведенный ниже код:

from fractions import Fraction

num = Fraction('-5/16')

print(num.as_integer_ratio())
выводит:

(-5, 16)
Метод limit_denominator()
Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит 
переданного аргумента.

Приведенный ниже код:

from fractions import Fraction
import math

print('PI =', math.pi)

num = Fraction(str(math.pi))

print('No limit =', num)

for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)
выводит:

PI = 3.141592653589793
No limit = 3141592653589793/1000000000000000
3
16/5
22/7
267/85
311/99
355/113
3126535/995207
Метод limit_denominator() позволяет получить очень точные рациональные приближения иррациональных чисел, что очень
 удобно во многих математических задачах.

Примечания
Примечание 1. Для того, чтобы каждый раз не писать название типа, можно использовать следующий код:

from fractions import Fraction as F

num1 = F('1/5') + F('3/2')
num2 = F('1/4') * F('2/5')

print(num1)
print(num2)
Примечание 2. Полное руководство по данному типу данных находится в официальной документации.

Примечание 3. В Python нельзя совершать арифметические операции (+, -, *, /) между типами Decimal и Fraction. 

Приведенный ниже код:

from decimal import Decimal
from fractions import Fraction

num1 = Decimal('12.5')
num2 = Fraction(19, 3)

print(num1 + num2)
приводит к ошибке:

TypeError: unsupported operand type(s) for +: 'Decimal' and 'Fraction'''''

'''Десятичные числа хранятся в списке numbers в виде строк. Дополните приведенный код, чтобы он для каждого десятичного
 числа вывел его представление в виде обыкновенной дроби в формате:

десятичное число = обыкновенная дробь
Примечание. Программа должна вывести

6.34 = 317/50
4.08 = 102/25
3.04 = 76/25
...'''
#
# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# for i in numbers:
#     print(i, '=', Fraction(i))

# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# for num in numbers:
#     print(f'{num} = {Fraction(num)}')


# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# print(*[f'{i} = {Fraction(i)}' for i in numbers], sep='\n')


'''Десятичные числа разделенные символом пробела хранятся в строковой переменной s. Дополните приведенный код, чтобы он вывел сумму наибольшего и наименьшего числа в виде обыкновенной дроби.'''

# from fractions import Fraction
# from decimal import Decimal as D
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# nums = [D(x) for x in s.split()]
# S=D(max(nums))+D(min(nums))
# print(Fraction(S))

# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# s = [Fraction(num) for num in s.split()]
# print(max(s) + min(s))


# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# li = [Fraction(i) for i in s.split()]
# print(max(li)+min(li))


'''Сократите дробь
Даны два натуральных числа mm и nn. Напишите программу, которая сокращает дробь \dfrac{m}{n} 
n
m
​
  и выводит ее.

Формат входных данных
На вход программе подается два натуральных числа, числитель и знаменатель дроби, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести ответ на задачу.

Sample Input 1:

3
6
Sample Output 1:

1/2'''

# from fractions import Fraction
# a=int(input())
# b=int(input())
#
# num1 = Fraction(a,b)
# print(num1)


# from fractions import Fraction as fr
#
# print(fr(int(input()), int(input())))


# from fractions import Fraction
# print(Fraction(f'{input()}/{input()}'))


# from fractions import Fraction
# n, m = Fraction(input()), Fraction(input())
# print(n/m)

'''
Операции над дробями
Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и 
частное.

Формат входных данных
На вход программе подаются две ненулевые дроби, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести сумму, разность, произведение и частное двух дробей.

Примечание. Обратите внимание на третий тест: исходные дроби сокращать не нужно, а результат нужно.

Sample Input 1:

2/3
3/7
Sample Output 1:

2/3 + 3/7 = 23/21
2/3 - 3/7 = 5/21
2/3 * 3/7 = 2/7
2/3 / 3/7 = 14/9'''

# from fractions import Fraction
# num3=input()
# num4=input()
# num1 = Fraction(num3)
# num2 = Fraction(num4)
#
# print(f'{num3} + {num4} = {num1 + num2}')
# print(f'{num3} - {num4} = {num1 - num2}')
# print(f'{num3} * {num4} = {num1 * num2}')
# print(f'{num3} / {num4} = {num1 / num2}')


# from fractions import Fraction as F
# operators = {'+': F.__add__, '-': F.__sub__, '*': F.__mul__, '/': F.__truediv__}
# a, b = [input() for _ in '..']
# ops = [*map(F, (a, b))]
# for op in operators:
#     print(f'{a} {op} {b} = {operators[op](*ops)}')


# from fractions import Fraction as fr
#
# f1, f2 = input(), input()
# print(f1, '+', f2, '=', fr(f1) + fr(f2))
# print(f1, '-', f2, '=', fr(f1) - fr(f2))
# print(f1, '*', f2, '=', fr(f1) * fr(f2))
# print(f1, '/', f2, '=', fr(f1) / fr(f2))


'''Сумма дробей 1
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет и выводит рациональное число, 
равное значению выражения 
\dfrac{1}{1^2} + \dfrac{1}{2^2} + \dfrac{1}{3^2} + \dfrac{1}{4^2} + \ldots + \dfrac{1}{n^2}
1 
2
 
1
​
 + 
2 
2
 
1
​
 + 
3 
2
 
1
​
 + 
4 
2
 
1
​
 +…+ 
n 
2
 
1
​
 

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание 1. Результирующая дробь должна быть несократимой.

Примечание 2. Подробнее о ряде обратных квадратов можно почитать тут.

Sample Input 1:

1
Sample Output 1:

1
Sample Input 2:

2
Sample Output 2:

5/4
Sample Input 3:

3
Sample Output 3:

49/36'''

# from fractions import Fraction as Fr
# n = int(input())
# lst = [(1/Fr(i**2)) for i in range(1, n + 1)]
# print(Fr(sum(lst)))


# from fractions import Fraction as F
# print(sum([F(1, i**2) for i in range(1, int(input()) + 1)]))


# from fractions import Fraction as Fr
# res = 0
# for i in range(1, int(input()) + 1):
#     res += Fr(1, i ** 2)
# print(res)


# from fractions import Fraction as F
# def fss(n):
#     return F(1) if n < 2 else fss(n - 1) + F(1, n * n)
# print(fss(int(input())))


# from fractions import Fraction as F
# n = int(input())
# print(sum([F(1, i**2) for i in range(1, n+1)]))


'''Сумма дробей 2
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет и выводит рациональное число,
 равное значению выражения 
\dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \dfrac{1}{4!} + \ldots + \dfrac{1}{n!}

 

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание 1. Результирующая дробь должна быть несократимой.

Примечание 2. Для вычисления факториала можно использовать функцию factorial из модуля math.

Sample Input 1:

1
Sample Output 1:

1
Sample Input 2:

2
Sample Output 2:

3/2
Sample Input 3:

3
Sample Output 3:

5/3'''

# from fractions import Fraction as Fr
# n = int(input())
# lst = [(1 / Fr(math.factorial(i))) for i in range(1, n + 1)]
# print(Fr(sum(lst)))


# from math import factorial
# from fractions import Fraction as F
#
# print(sum(F(1 / F(factorial(i))) for i in range(1, int(input()) + 1)))


# from fractions import Fraction as F
# from math import factorial as fack
# print(sum([F(1, fack(i)) for i in range(1, int(input())+1)]))


# from fractions import Fraction
# from math import factorial
#
# n = int(input())
# print(sum([Fraction(1, factorial(i)) for i in range(1, n + 1)]))

'''Юный математик 🌶️
Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем. 
Вчера на уроке математики Дима узнал, что дробь называется правильной, если ее числитель меньше знаменателя, и 
несократимой, если нет равной ей дроби с меньшими натуральными числителем и знаменателем.

Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и решая разные задачки с правильными
 несократимыми дробями. Одну из этих задач Дима предлагает решить вам с помощью компьютера.

На вход программе подается натуральное число nn. Напишите программу, которая находит наибольшую правильную несократимую
 дробь с суммой числителя и знаменателя равной nn.

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух 
чисел. Функция реализована в модуле math.

Sample Input 1:

10
Sample Output 1:

3/7
Sample Input 2:

23
Sample Output 2:

11/12'''

# import math
# from fractions import Fraction as F
# n = int(input())
# a=n//2
# b=n-a
# while math.gcd(a, b)!= 1:
#     a-=1
#     b+=1
#
# print(F(a, b))


# from math import gcd
#
# n = int(input())
# i = n // 2
# while gcd(i, n - i) != 1:
#     i -= 1
# print(f'{i}/{n - i}')


# from fractions import Fraction as F
# from math import gcd
# n=int(input())
# res=[]
# for a in range(1,n//2+n%2):
#     if gcd(a,n-a)==1:
#         res.append(F(a,n-a))
# print(max(res))

# from fractions import Fraction as F
# num = int(input())
# for i in range(num // 2 ,num + 1):
#     if i > num - i and str(F(str(num - i) + "/" + str(i))) == str(num - i) + "/" + str(i):
#         print(F(str(num - i) + "/" + str(i)))
#         break


'''Упорядоченные дроби
На вход программе подается натуральное число nn. Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 00 и 11, знаменатель которых не превосходит nn.

Формат входных данных
На вход программе подается натуральное число n, \, n > 1n,n>1.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух чисел. Функция реализована в модуле math.

Sample Input 1:

5
Sample Output 1:

1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
Sample Input 2:

4
Sample Output 2:

1/4
1/3
1/2
2/3
3/4'''



# from fractions import Fraction
# from math import gcd
#
# n = int(input())
# nums = set()
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         num = Fraction(i, j)
#         if num < 1 and gcd(i, j):
#             nums.add(num)
# print(*sorted(nums), sep='\n')


# from fractions import Fraction
# numbers = set()
# for i in range(2, int(input()) + 1):
#     for j in range(1, i):
#         numbers.add(Fraction(j, i))
# print(*sorted(numbers), sep='\n')


#
# from fractions import Fraction as F
# print(*sorted(set(F(i, j) for j in range(1, int(input()) + 1) for i in range(1, j))), sep='\n')

# from fractions import Fraction as F
# l=[]
# n = int(input())
# for i in range(1, n):
#     for j in range(1, n+1):
#         if i / j < 1:
#             u = str(i)+'/'+str(j)
#             l.append(u)
# l = set(map(F, l))
# print(*sorted(l), sep='\n')


# from math import gcd
# from fractions import Fraction
# n = int(input())
# print(*sorted([Fraction(j, i) for j in range(1, n) for i in range(2, n + 1) if j < i and gcd(j, i) == 1]), sep='\n')