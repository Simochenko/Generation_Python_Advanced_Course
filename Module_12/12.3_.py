'''Метод Монте-Карло
Метод Монте-Карло – группа численных методов, основанных на воспроизведении и статистическом анализе большого числа
 реализаций случайного процесса. Проводится математическое моделирование случайных процессов и параметры их реализации
  оцениваются статистически. Метод лежит в основе статистического моделирования.

   Метод Монте-Карло часто называют методом статистических испытаний.

Основоположники метода Монте-Карло

Станислав Улам

Джон фон Нейман

Николас Метрополис
Статистическое моделирование широко применяется для решения задач из различных областей человеческого знания - биологии, химии, физики, экономики и других. Задачи, где широко используется этот подход:

численное интегрирование;
расчеты в системах массового обслуживания;
расчеты качества и надежности изделий;
расчеты прохождения нейтронов и других частиц через вещество;
передача сообщений при наличии помех;
задачи теории игр;
задачи динамики разреженного газа;
задачи дискретной оптимизации;
задачи финансовой математики.
Вычисление площадей
Применим метод Монте-Карло и к задаче вычисления площади геометрической фигуры на плоскости.

Поместим фигуру в прямоугольник и будем наугад бросать точки в этот прямоугольник. Будем исходить из того, что чем больше площадь фигуры, тем чаще в нее будут попадать точки. Таким образом, при большом числе nn точек, наугад выбранных внутри прямоугольника, доля точек, содержащихся в данной фигуре kk, приближенно равна отношению площади этой фигуры и площади прямоугольника.

Если площадь прямоугольника равна S_0S
0
​
  и в результате испытаний, из которых при kk исходах случайные точки оказались внутри фигуры, то площадь SS фигуры будет определяться выражением
S = \dfrac{k}{n} \cdot S_0.
S=
n
k
​
 ⋅S
0
​
 .
 Рассмотрим алгоритм решения задачи на конкретных примерах.

Пример 1. Рассмотрим фигуру, множество точек которой определяется следующей системой неравенств:

\begin{cases} 0\le x \le 1\\ 0\le y \le 1\\ y\le x^2\end{cases}
⎩
⎨
⎧
​

0≤x≤1
0≤y≤1
y≤x
2

​

Графическое изображение указанной фигуры в плоскости xOyxOy имеет вид:



Площадь такой фигуры S = \dfrac13 \approx 0.33333S=
3
1
​
 ≈ 0.33333 (считается через интеграл).

Алгоритм Монте-Карло: площадь искомой фигуры составляет часть квадрата со сторонами 11. Площадь такого квадрата равна 11.

Генерируем случайные числа xx и yy равномерно распределенные на отрезке [0; \, 1][0;1]. Это будут координаты случайной точки в квадрате, в которую заключена фигура, площадь которой требуется найти. Полученная точка может как попасть в исследуемую фигуру, так и не попасть.
Проверяем принадлежность точки к исследуемой фигуре. Если попадания нет, т.е. не выполняется неравенство y \le x^2y≤x
2
 , то переходим к пункту 1 и генерируем координаты новой точки. Если попадание есть, то фиксируем это попадание, то есть увеличиваем на единицу значение счетчика числа попаданий и снова переходим к пункту 1.


Примечание. Заметим, что попадание случайной точки точно на границу фигуры можно отнести как к первому, так и ко второму исходу.

Пункты 11 и 22 следует повторить в цикле достаточно большое количество nn раз. От количества повторений напрямую зависит точность результата. После проведения nn повторов площадь фигуры найдем по формуле:
S = \dfrac{k}{n} \cdot S_0.
S=
n
k
​
 ⋅S
0
​
 .

Пример программы на Python:

import random

n = 1000
k = 0
s0 = 1
for _ in range(n):
    x = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1

    if y <= x**2:                # если попадает в нужную область
        k += 1

print((k/n)*s0)
Составим таблицу:

nn	SS
1010	0.60.6
100100	0.370.37
10001000	0.3370.337
1000010000	0.33370.3337
100000100000	0.333290.33329
10000001000000	0.3335710.333571
1000000010000000	0.33328280.3332828
100000000100000000	0.333367070.33336707
Пример 2. Рассмотрим фигуру, множество точек которой определяется следующей системой неравенств:

\begin{cases} -2\le x \le 2\\ -2\le y \le 2\\ y^3-2x^2 \le -1\\ 2y+x^3 \le 3 \end{cases}
⎩
⎨
⎧
​

−2≤x≤2
−2≤y≤2
y
3
 −2x
2
 ≤−1
2y+x
3
 ≤3
​

Графическое изображение указанной фигуры в плоскости xOyxOy имеет вид:



Площадь такой фигуры нам заранее известна и равна S = 8.38404S=8.38404.



Алгоритм Монте-Карло: площадь искомой фигуры составляет часть квадрата со сторонами 44. Площадь такого квадрата равна 1616.

Генерируем случайные числа xx и yy, равномерно распределенные на отрезках [-2; \, 2][−2;2]. Это будут координаты случайных точек в квадрате, в который заключена фигура искомой площади. Полученная точка может как попасть в исследуемую фигуру, так и не не попасть.
Проверяем принадлежность точки к исследуемой фигуре. Если попадания нет, не выполняется хотя бы одно из  неравенств y^3-2x^2 \le -1y
3
 −2x
2
 ≤−1 или 2y+x^3 \le 32y+x
3
 ≤3, переходим к пункту 11 и генерируем координаты новой точки. Если попадание есть, фиксируем это попадание, то есть увеличиваем на единицу значение счетчика числа попаданий и снова переходим к пункту 11.
import random

n = 1000
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if y**3 - 2*x**2 <= -1 and 2*y + x**3 <= 3:
        k += 1

print((k/n)*s0)
Составим таблицу:

nn	SS
1010	9.69.6
100100	8.968.96
10001000	8.2248.224
1000010000	8.38248.3824
100000100000	8.365288.36528
10000001000000	8.3833768.383376
1000000010000000	8.38415848.3841584
100000000100000000	8.384041348.38404134
Примечания
Примечание 1. Свое экзотическое название метод получил от города Монте-Карло в княжестве Монако, известного благодаря
 казино, поскольку именно рулетка является одним из самых широко известных генераторов случайных чисел. Станислав Улам
 пишет в своей автобиографии «Приключения математика», что название было предложено Николасом Метрополисом в честь его
  дяди, азартного игрока.



Примечание 2. Активное применение метода началось с появлением ЭВМ, способных выполнять сотни операций для получения
 необходимых статистических данных. Развитие метода Монте-Карло пришлось на 1950-е годы, когда его использовали ученые
 из лаборатории ВВС США и исследовательской корпорации RAND, работающие над созданием водородной бомбы, в том числе и
  гениальный ученый Джон фон Нейман. Неймана считают одним из основателей метода, как, впрочем, и самих ЭВМ.

Примечание 3. Аналогичным образом можно вычислять объемы тел в пространстве.

Примечание 4. Подробнее о методе Монте-Карло можно почитать тут.'''

'''Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью 
системы неравенств:
'''


# import random
#
# n = 10**6
# k = 0
# s = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if x**3 +y**4+2 >= 0 and 3*x+y**2 <= 2:
#         k += 1
#
# print((k/n)*s)

'''Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа π.

Примечание 1. Площадь единичного круга, то есть круга с радиусом, равным R =1 равна S =πR2 =π.

Примечание 2. Уравнение единичной окружности имеет вид x^2+y^2 = 1x 
'''


# import random
# n = 10**6
# k = 0.0
# for i in range(n):
#     x = random.random()
#     y = random.random()
#     k += (x * x + y * y < 1.0)
# print(4 * k / n)

# from random import uniform as dart
#
# n, S0, k = 1e6, 4, 0
# for _ in range(int(n)):
#     k += sum(dart(-1, 1) ** 2 for _ in 'xy') <= 1
# print(k * S0 / n)

# import random
# counter = 0
# n = 10 ** 6
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if x ** 2 + y ** 2 < 1:
#         counter += 1
# print(4 * counter / n)


'''Болотная сортировка
Болотная сортировка (Bogosort) — неэффективный алгоритм сортировки, используемый только в образовательных целях и противопоставляемый другим, более реалистичным алгоритмам.

Принцип работы алгоритма прост, как плесень. Перетряхиваем список случайным образом до тех пор пока он внезапно не отсортируется. Процесс может счастливо завершиться сразу, а может длиться до тепловой смерти Вселенной. Это уж как повезёт.

   Bogo sort is the fastest sort if you're very lucky.

Время работы алгоритма
Среднее время работы алгоритма болотной сортировки на современном компьютере:

Кол-во элементов	10	11	12	13	14	15	16	17	18	19	20
Среднее время	0,00370,0037 с	0,0450,045 с	0,590,59 с	8,48,4 с	2,12,1 мин	33,633,6 мин	9,79,7 ч	7,297,29 сут	139139 сут	7,67,6 лет	160160 лет
Колода в 3232 карты будет сортироваться компьютером в среднем 2,7\cdot 10^{19}2,7⋅10 
19
  лет.

Реализация алгоритма
Для реализации алгоритма болотной сортировки будем использовать функцию shuffle(), которая случайным образом перемешивает содержимое списка.

import random

def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):                  # реализация алгоритма болотной сортировки
    while not is_sort(nums):
        random.shuffle(nums)
    return nums

numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)                # выводим отсортированный список'''
