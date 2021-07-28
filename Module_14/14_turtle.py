'''Тема урока: модуль turtle
Черепашья графика
Модуль turtle
Рисование отрезков прямой
Поворот черепашки
Установка углового направления черепашки
Изменение внешнего вида черепашки
Аннотация. Урок посвящен черепашьей графике: модулю turtle и основным командам.

Черепашья графика
В конце 19601960-х годов преподаватель Массачусетского технологического института (МIТ) Сеймур Пейперт начал использовать роботизированную "черепашку" для обучения студентов программированию.

Черепашка была связана с компьютером, на котором обучаемый мог вводить команды, побуждающие черепашку перемещаться. У черепашки имелось перо, которое можно было поднимать и опускать. Ее можно было положить на лист бумаги и, программируя движение, создать рисунок.



Python имеет систему черепашьей графики, имитирующую эту роботизированную черепашку. Система выводит на экран небольшой курсор (черепашку). Перемещение черепашки по экрану рисует линии и геометрические фигуры. Для этого используется модуль turtle.

Модуль turtle
Система черепашьей графики не встроена в интерпретатор Python и хранится в модуле turtle. В начале программы с использованием черепашьей графики пишут инструкцию импорта этого модуля:

import turtle
Для визуализации черепашьей графики мы будем использовать онлайн среду trinket.

Рисование отрезков прямой
В результате команды turtle.showturtle() появляется графическое окно с черепашкой. Черепашка первоначально расположена в центре графического окна, "холста". Выглядит она как стрелка с острием на месте головы. Если дать черепашке команду двигаться вперед, она переместится в направлении, указываемом стрелкой.

   По умолчанию на старте черепашка смотрит на восток.

Для перемещения черепашки вперед на nn пикселей применяется команда turtle.forward(n). Например, команда turtle.forward(100) переместит черепашку вперед на 100100 пикселей.

Для перемещения черепашки назад на nn пикселей применяется команда turtle.backward(n). Например, команда turtle.backward(250) переместит черепашку назад на 250250 пикселей.



Поворот черепашки
Когда черепашка появляется, она по умолчанию направлена на восток, то есть вправо, или под углом 0^{\circ}0
∘
 .



При помощи команд turtle.right() и turtle.left() можно повернуть черепашку:

команда turtle.right(angle) поворачивает черепашку вправо на angle градусов;
команда turtle.left(angle) поворачивает черепашку влево на angle градусов.


Рассмотрим программный код:

import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
Такой код перемещает черепашку на 100100 пикселей вперед. Далее он поворачивает черепашку на 90^{\circ}90
∘
  вправо (черепашка будет смотреть вниз). Затем он перемещает черепашку на 100100 пикселей вперед.



Рассмотрим программный код с использованием команды turtle.left():

import turtle

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
Такой код сначала перемещает черепашку на 100100 пикселей вперед. Затем он поворачивает черепашку на 120^{\circ}120
∘
  влево (черепашка будет смотреть на северо-запад). И далее он перемещает черепашку на 100100 пикселей вперед.



Команды turtle.right() и turtle.left() поворачивают черепашку на указанный угол от ее направления в этот момент, а не от исходного. К примеру, текущее угловое направление составляет 90^{\circ}90
∘
 , строго на север. Если ввести команду turtle.left(20), то черепашка повернется влево на 20^{\circ}20
∘
 . Ее новое угловое направление составит 110^{\circ}110
∘
 , по отношению к начальному положению, когда угол равен 0^{\circ}0
∘
 .

В качестве еще одного примера рассмотрим код:

import turtle

turtle.forward(50)
turtle.left(45)

turtle.forward(50)
turtle.left(45)

turtle.forward(50)
turtle.left(45)

turtle.forward(50)
В начале направление черепашки составляет 0^{\circ}0
∘
 . Далее черепашка перемещается на 5050 пикселей вперед и поворачивается на 45^{\circ}45
∘
  влево. Затем еще дважды повторяет перемещение вперед на 5050 пикселей и поворот на 45^{\circ}45
∘
  влево. После всех этих поворотов угловое направление черепашки составит 135^{\circ}135
∘
 .



Установка углового направления черепашки
Команда turtle.setheading() применяется для установки углового направления черепашки с заданным углом. В качестве аргумента нужно указать желаемый угол.

Рассмотрим код:

import turtle

turtle.forward(100)
turtle.setheading(90)

turtle.forward(100)
turtle.setheading(180)

turtle.forward(100)
turtle.setheading(270)

turtle.forward(100)
Первоначальное угловое направление черепашки составляет 0^{\circ}0
∘
 . Далее установлено направление черепашки 90^{\circ}90
∘
  (на север). Затем установлено направление черепашки 180^{\circ}180
∘
  (на запад). Потом установлено направление черепашки 270^{\circ}270
∘
  (на юг).



Получение текущего углового направления черепашки
Чтобы получить текущее угловое направление черепашки используется команда turtle.heading().

Приведенный ниже код:

import turtle

print(turtle.heading())
turtle.setheading(180)
print(turtle.heading())
поворачивает черепашку на запад и выводит:

0.0
180.0


Изменение внешнего вида черепашки
По умолчанию черепашка выглядит как стрелочка, но возможен и другой внешний вид. Для его изменения используют команду shape(). Команда принимает в качестве аргумента строковое название фигуры, определяющей форму черепашки. Доступные фигуры:

square (квадрат);
arrow (стрелка);
circle (круг);
turtle (черепашка);
triangle (треугольник);
classic (классическая стрелка).
import turtle

turtle.shape('square')
turtle.forward(100)
turtle.setheading(90)

turtle.shape('arrow')
turtle.forward(100)
turtle.setheading(180)

turtle.shape('turtle')
turtle.forward(100)
turtle.setheading(270)

turtle.shape('circle')
turtle.forward(100)


При необходимости можно использовать собственные рисунки для создания внешнего вида черепашки.



Примечания
Примечание 1. Полная документация по черепашьей графике находится тут. Рекомендуем с ней ознакомиться.

Примечание 2. Не весь функционал черепашки доступен в Trinket. Подробности в разделе turtle.

Примечание 3. Все рассмотренные команды являются методами класса Turtle (ООП).

Примечание 4. Можно настроить размер шрифта в Trinket.'''

# import turtle
#
# def rectangle(width, height):
#   for _ in range(2):
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)
# rectangle(100, 50)
#

# import turtle
#
# def triangle(side):
#   for _ in range(3):
#     turtle.forward(side)
#     turtle.left(120)
# triangle(160)


# import turtle
# def square(side):
#   for _ in '123':
#     turtle.left(22.5)
#     for _ in '1234':
#       turtle.forward(side)
#       turtle.left(90)
#
# square(90)


# import turtle
#
#
# def square(side):
#     for _ in range(4):
#         turtle.forward(side)
#         turtle.left(90)
#
#
# for _ in range(8):
#     turtle.left(45)
#     square(120)


# import turtle
# turtle.showturtle()
#
# def polygonal(size, what):
#
#     y = 360 / what
#     for _ in range(what):
#         turtle.forward(size)
#         turtle.left(y)
#
# polygonal(200, 6)

# import turtle
#
#
# def hexagon(side):
#     for _ in '1' * 6:
#         turtle.forward(side)
#         turtle.right(60)
#
#
# def count(size, num):
#     for _ in range(num):
#         hexagon(size)
#         turtle.right(120)
#         turtle.forward(size)
#         turtle.left(60)
#
#
# count(60, 6)


# import turtle
#
# for _ in '12':
#   turtle.forward(150)
#   turtle.left(120)
#   turtle.forward(150)
#   turtle.left(60)

# import turtle
# def romb(side):
#     turtle.speed(1000)
#
#     for _ in range(10):
#         turtle.left(36)
#         for _ in '12':
#             turtle.forward(side)
#             turtle.left(-60)
#             turtle.forward(side)
#             turtle.left(-120)
#
#
# romb(100)

#
# import turtle
#
#
# def star(side):
#     turtle.speed(50)
#     for _ in range(10):
#         turtle.forward(side)
#         turtle.backward(side)
#         turtle.left(36)
#
#
# star(100)


# import turtle
# turtle.speed(10)
#
# def star5(side):
#   for _ in range(5):
#     turtle.forward(side)
#     turtle.right(144)
#
# star5(200)


# import turtle
#
# turtle.speed(50)
#
#
# def cube(side):
#     i = 0
#     for _ in range(15):
#
#         for _ in '1234':
#             turtle.left(90)
#             turtle.forward(side + i)
#         i += 10
#
#
# cube(50)


# import turtle
# turtle.speed(10)
# i=0
# for _ in range(41):
#   turtle.left(90)
#   turtle.forward(10+i)
#   i += 5


'''Тема урока: модуль turtle
Поднятие и опускание пера
Рисование кругов и точек
Изменение размера пера
Изменение цвета рисунка
Изменение цвета фона
Создание штампа
Возвращение экрана в исходное состояние
Получение текущей позиции черепашки
Управление скоростью анимации черепашки
Аннотация. Урок посвящен черепашьей графике и модулю turtle.

Поднятие и опускание пера
Исходная роботизированная черепашка, использованная преподавателем Сеймуром Пейпертом, лежала на большом листе бумаги 
и имела перо, которое можно было поднимать и опускать. Когда перо было опущено на бумагу, оно чертило линию во время 
перемещения черепашки. Когда перо поднималось, оно не касалось бумаги, и черепашка во время движения не оставляла за
 собой линии.

Команда turtle.penup() поднимает перо, а команда turtle.pendown() – опускает. Когда перо поднято, черепашка перемещается не оставляя линии. Когда перо опущено, черепашка во время перемещения чертит линию. По умолчанию перо опущено.

Приведенный ниже код:

import turtle

turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
выводит пунктирную линию.



Рисование кругов и точек
Чтобы черепашка нарисовала круг, можно применить команду turtle.circle(). Такая команда рисует круг заданного в виде аргумента в пикселях радиуса.

Например, команда turtle.circle(80) побуждает черепашку нарисовать круг с радиусом 8080 пикселей.

Приведенный ниже код:

import turtle

turtle.circle(80)
изображает круг радиусом в 8080 пикселей.



Команда turtle.dot() применяется, чтобы черепашка нарисовала точку.

Приведенный ниже код:

import turtle

turtle.dot()
turtle.forward(50)

turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)
рисует три точки на одной прямой с расстоянием в 5050 пикселей между ними.



Изменение размера пера
Для изменения ширины пера черепашки в пикселях можно применить команду turtle.pensize(). Аргумент команды – целое число, задает ширину пера.

Приведенный ниже код устанавливает ширину пера в 55 пикселей и затем рисует круг:

import turtle

turtle.pensize(5)
turtle.circle(80)


Изменение цвета рисунка
Для изменения цвета рисунка можно применить команду turtle.pencolor(). Аргумент команды – строковое представление названия цвета.

Приведенный ниже код меняет цвет рисунка на красный и затем рисует круг:

import turtle

turtle.pencolor('red')
turtle.circle(80)


С командой turtle.pencolor() можно использовать многочисленные предопределенные названия цветов. Наиболее широко используемые названия цветов:

red (красный);
green (зеленый);
bluе (синий);
yellow (желтый);
cyan (сине-зелёный).
Команда turtle.pencolor() позволяет работать не только с предопределенными названиями цветов, но и с цветами, заданными в формате RGB (Red Green Blue). В качестве аргумента команды turtle.pencolor() можно использовать либо кортеж из 33 чисел (r, g, b), либо просто три числа r, g, b.



В Python 3 для того, чтобы использовать цвет в формате RGB, нужно предварительно установить значение colormode в 255255, для этого нужно использовать команду turtle.Screen().colormode(255). Подробнее об этом можно почитать в документации.

Изменение цвета фона
Для изменения фонового цвета графического окна можно применить команду turtle.Screen().bgcolor(). В этом случае тоже можно использовать цвета с предопределенными названиями или задать цвет в RGB формате.

Приведенный ниже код меняет цвет фона на серый, цвет рисунка на зеленый и затем рисует круг:

import turtle

turtle.Screen().bgcolor('gray')
turtle.pencolor('green')
turtle.circle(80)


Мы также можем установить фоновое изображение с помощью команды turtle.Screen().bgpic().



Создание штампа
С помощью команды turtle.stamp() можно оставить штамп черепашки. Использование команды turtle.stamp() производит тот же эффект, что и команда turtle.dot(), но оставляет отметку в форме черепашки.

Приведенный ниже код:

import turtle

turtle.shape('turtle')

for i in range(3):
    turtle.forward(50)
    turtle.stamp()
создает следующий рисунок:



При использовании команды turtle.stamp() цветом штампа будет цвет заливки или по умолчанию черный.



Возвращение экрана в исходное состояние
Для возвращения графического окна черепашки в исходное состояние существуют три команды:

turtle.clear();
turtle.reset();
turtle.clearscreen().
Команда turtle.clear() стирает все рисунки в графическом окне. Но не меняет положение черепашки, цвет рисунка и цвет фона графического окна.

Команда turtle.reset() стирает все рисунки, имеющиеся в графическом окне, задает черный цвет рисунка и возвращает черепашку в исходное положение в центре экрана. Эта команда не переустанавливает цвет фона графического окна.

Команда turtle.clearscreen() стирает все рисунки в графическом окне, меняет цвет рисунка на черный, а цвет фона на белый, и возвращает черепашку в исходное положение в центре графического окна.

Примечания
Примечание 1. Для установления размера графического окна можно применить команду turtle.Screen().setup(). Аргументы команды – ширина и высота (в пикселях).

Приведенный ниже код создает графическое окно шириной 640 \times 480640×480 пикселей:

import turtle
turtle.Screen().setup(640, 480)
Примечание 2. Все цвета, доступные в черепашьей графике, выглядят так.

Палитра 1
Палитра 2
Палитра 3
Палитра 4
'''
# import turtle
#
# for i in range(20):
#     turtle.penup()
#     turtle.dot()
#     turtle.forward(10)

# import turtle
# for i in '12':
#   turtle.forward(150)
#   turtle.left(90)
#   turtle.dot()
#   turtle.forward(50)
#   turtle.left(90)
#   turtle.dot()

# import turtle
#
# def line(side):
#     turtle.forward(side)
#     turtle.stamp()
#     turtle.backward(side)
#
#
# def many_lines(quantity, side, dot_size):
#     turtle.dot(dot_size)
#     for i in range(1, quantity + 1):
#         turtle.setheading((360 / quantity) * i)
#         line(side)
#
# many_lines(8,40, 10)


# import turtle
#
# def turtle_stamp(side):
#     turtle.penup()
#     turtle.forward(side)
#     turtle.pendown()
#     turtle.stamp()
#     turtle.penup()
#     turtle.backward(side)
#
#
#
# def turtle_stamps(quantity, side):
#     turtle.shape('turtle')
#     turtle.stamp()
#     for i in range(1, quantity + 1):
#         turtle.setheading((360 / quantity) * i)
#         turtle_stamp(side)
#
# turtle_stamps(8,40)



# import turtle
#
# def turtle_stamp(side1, side2, side3):
#     turtle.Screen().bgcolor('Blue')
#     turtle.penup()
#     turtle.forward(side1)
#     turtle.pendown()
#     turtle.forward(side2)
#     turtle.penup()
#     turtle.forward(side3)
#     turtle.pendown()
#     turtle.stamp()
#     turtle.penup()
#     turtle.backward(side1 + side2 + side3)
#
# def turtle_stamps(quantity, side1, side2, side3):
#     turtle.shape('turtle')
#     turtle.stamp()
#     for i in range(1, quantity + 1):
#         turtle.setheading((360 / quantity) * i)
#         turtle_stamp(side1, side2, side3)
#
# turtle_stamps(12,100, 50, 20)



# import turtle
# turtle.speed(10)
# turtle.Screen().bgcolor('LightGreen')
# for i in range(6, 35):
#   turtle.shape('turtle')
#   turtle.stamp()
#   turtle.right(28)
#   turtle.penup()
#   turtle.forward(i*2.5)

# import turtle
# turtle.speed(10)
# colors = ['purple', 'orange', 'red', 'blue', 'yellow', 'forestgreen']
# for i in range(2, 47):
#   turtle.color(colors[i % 6])
#   turtle.forward(i * 3.6)
#   turtle.pensize(i * 0.7)
#   turtle.left(45)
#
# import turtle
# turtle.speed(10)
#
# def triangle(side):
#   for _ in range(3):
#     turtle.forward(side)
#     turtle.left(120)
#
# a = 200
# b0 = ((a / 3 * 2) ** 2 - (a / 3) ** 2) ** 0.5
#
# triangle(a)
# turtle.penup()
# turtle.goto(0, b0)
# turtle.right(60)
# turtle.pendown()
# triangle(a)


# import turtle
# turtle.speed(10)
#
# def rays(h):
#   turtle.penup()
#   turtle.goto(0, h)
#   s = int(h / 9 * 2)
#   for i in range(h, -h - 1, -s):
#     turtle.pendown()
#     turtle.color('mediumseagreen')
#     turtle.goto(i, 0)
#     turtle.color('blue')
#     turtle.dot()
#     turtle.penup()
#     turtle.goto(0, h)
#
# rays(170)
# turtle.color('red')
# turtle.dot()
# turtle.hideturtle()


# import turtle
# turtle.speed(10)
#
# color = ['limegreen', 'red', 'black', 'deepskyblue', 'yellow']
# s = 6
# turtle.pensize(s)
#
# def circles(r):
#   x0 = [r + s, -r, -3*r - s, -2*r - s]
#   y0 = [r + 10, r + 10, r + 10, 0]
#   for i in range(5):
#     turtle.color(color[i % 5])
#     turtle.circle(r)
#     turtle.penup()
#     turtle.goto(x0[i % 4], y0[i % 4])
#     turtle.pendown()
#
# circles(40)
# turtle.hideturtle()


# import turtle
# turtle.Screen().setup(300, 550)
# turtle.speed(10)
#
# turtle.circle(100)
# turtle.circle(50)
# turtle.penup()
# turtle.goto(0, 25)
# turtle.pendown()
# turtle.goto(0, 60)
# turtle.circle(15)
#
# n = [45, -45]
# for i in range(2):
#   turtle.penup()
#   turtle.goto(n[i % 2], 110)
#   turtle.pendown()
#   turtle.pensize(15)
#   turtle.dot()
#
# k = [90, -90]
# for i in range(2):
#   turtle.penup()
#   turtle.goto(k[i % 2], 167)
#   turtle.pendown()
#   turtle.pensize(1)
#   turtle.circle(35)
#
# turtle.hideturtle()


# import turtle, random
# turtle.Screen().bgcolor('cyan')
# turtle.speed(0)
#
# spos = [i for i in range(-180, 180)]
# scolors = ['blue', 'darkblue', 'darkgrey', 'violet', 'darkviolet']
#
# def sflake(ray):
#   turtle.penup()
#   turtle.goto(random.sample(spos, 2))
#   turtle.pendown()
#   turtle.color(random.choice(scolors))
#   for _ in range(8):
#     turtle.forward(ray)
#     for _ in range(3):
#       turtle.backward(ray / 4)
#       turtle.left(45)
#       turtle.forward(ray / 4)
#       turtle.backward(ray / 4)
#       turtle.right(90)
#       turtle.forward(ray / 4)
#       turtle.backward(ray / 4)
#       turtle.left(45)
#     turtle.backward(ray / 4)
#     turtle.left(45)
#
# for i in range(10):
#   sflake(random.randint(15, 50))
#
# turtle.hideturtle()

'''import turtle
from random import randrange

def random_color():
  return randrange(256), randrange(256), randrange(256) 

def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)

def left_mouse_click(x, y):
    draw_circle(x, y, 10)

turtle.hideturtle()

turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()'''

# import turtle
# turtle.Screen().setup(300, 400)
# turtle.speed(10)
#
# turtle.hideturtle()
# turtle.fillcolor('beige')
# turtle.begin_fill()
# turtle.goto(100, 0)
# turtle.goto(100, 100)
# turtle.goto(0, 100)
# turtle.goto(0, 0)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(-20, 100)
# turtle.pendown()
# turtle.fillcolor('brown')
# turtle.begin_fill()
# turtle.goto(50, 180)
# turtle.goto(120, 100)
# turtle.goto(-20, 100)
# turtle.end_fill()


# import turtle as t
# t.Screen().setup(300, 400)
# t.speed(10)
# t.hideturtle()
#
# t.begin_fill()
# t.goto(60, 0)
# t.goto(60, 160)
# t.goto(0, 160)
# t.goto(0, 0)
# t.end_fill()

# y0 = [30, 80, 130]
# cls = ['limegreen', 'yellow', 'red']
#
# for i in range(3):
#   t.penup()
#   t.goto(30, y0[i % 3])
#   t.pendown()
#   t.pensize(20)
#   t.color(cls[i % 3])
#   t.dot()



# import turtle as t
# t.Screen().setup(350, 400)
# t.speed(0)
# t.hideturtle()
#
# def triangle(side):
#   for _ in range(3):
#     t.forward(side)
#     t.left(120)
#
# s = 150
# k = ((s / 3 * 2) ** 2 - (s / 3) ** 2) ** 0.5
# y3 = ((s / 2) * (s / 6)) ** 0.5
# x0 = [0, s, s / 2]
# y0 = [k, k, -y3]
#
# triangle(s)
#
# for i in range(3):
#   t.penup()
#   t.goto(x0[i%3], y0[i%3])
#   t.pendown()
#   t.pensize(25)
#   t.dot()
#
# t.penup()
# t.goto(0, k)
# t.right(60)
# t.color('white')
# t.begin_fill()
# triangle(s)
# t.end_fill()


# import turtle as t
# t.speed(0)
# t.hideturtle()
# cls = ["#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF", "#1E56FC", "#4800FF", "#CC00FF", "#FF5099"]
# rad = [i for i in range(150, 0, -15)]
# t.goto(0, -150)
# for i in range(10):
#   t.fillcolor(cls[i % 10])
#   t.begin_fill()
#   t.circle(rad[i])
#   t.end_fill()
#   t.penup()
#   t.goto(0, -rad[i % 10] + 15)
#   t.pendown()


# import turtle as t
# t.Screen().setup(300, 500)
# t.Screen().bgcolor('darkblue')
# t.speed(0)
# t.up()
# cls = ['yellow', 'darkblue']
#
# def draw_circle(c):
#   t.fillcolor(c)
#   t.begin_fill()
#   t.circle(100)
#   t.end_fill()
#
# draw_circle(cls[0])
# t.forward(30)
# draw_circle(cls[1])
# t.hideturtle()


# import turtle
# turtle.Screen().bgcolor('blue')
# moon = turtle.Turtle()
# moon.hideturtle()
# moon.pencolor('orange')
# moon.dot(200)
# shadow = {0: turtle.Turtle(), 5: turtle.Turtle()}
# for i in [0, 5]:
#   shadow[i].hideturtle()
#   shadow[i].pencolor('blue')
#   shadow[i].penup()
# while 1:
#   for i in range(200, -201, -5):
#     shadow[i % 10].goto(i, 0)
#     shadow[i % 10].dot(200)
#     shadow[(i + 5) % 10].clear()

# import turtle
# import random
# def starUSSR(side):
#   color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
#   turtle.pencolor(color)
#   turtle.pendown()
#   turtle.fillcolor(color)
#   turtle.begin_fill()
#   for i in range(6):
#     turtle.forward(side)
#     turtle.right(144)
#   turtle.end_fill()
#   turtle.penup()
#
# turtle.Screen().setup(400, 400)
# turtle.Screen().bgcolor('white')
# turtle.tracer(5, 0)
# side = 20
# turtle.speed(0)
# for i in range(50):
#   turtle.hideturtle()
#   turtle.penup()
#   turtle.right(random.randint(0, 360))
#   turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
#   starUSSR(random.randint(3, 25))


# import turtle, random, math
#
# turtle.speed()
# turtle.penup()
#
# s = random.randint(4000, 5000)
#
# turtle.goto(-150, 150)
#
# for i in range(5):
#     for j in range(5):
#         turtle.goto(-150 + i * 70, 150 - j * 70)
#
#         n = random.randint(3, 7)
#         a = math.sqrt(s * 4 * math.tan(math.pi / 2 / n) / n)
#         color = tuple(random.randint(0, 255) for _ in '123')
#         turtle.fillcolor(color)
#
#         turtle.begin_fill()
#         for _ in range(n):
#             turtle.pendown()
#             turtle.forward(a)
#             turtle.penup()
#             turtle.right(360 / n)
#         turtle.end_fill()


# import turtle
#
# def sq(side, color):
#   turtle.fillcolor(color)
#   turtle.begin_fill()
#   for i in range(4):
#     turtle.forward(side)
#     turtle.right(90)
#   turtle.end_fill()
#
# side = 50
# n = 8
# canvx = 400
# canvy = 400
# turtle.Screen().setup(canvx, canvy)
# turtle.speed(0)
# positionx = -(canvx // 2)
# positiony = canvy // 2
# turtle.penup()
# turtle.goto(positionx, positiony)
# turtle.pendown()
# colors = ['black', 'white']
# for j in range(n):
#   for i in range(n):
#     sq(side, colors[(i + j)% 2])
#     turtle.forward(side)
#   positiony -= side
#   turtle.penup()
#   turtle.goto(positionx, positiony)
#   turtle.pendown()


# import turtle as t
# t.hideturtle()
# f = ('Times New Roman', 11, 'normal')
# lst = ['Восток', 'Запад', 'Север', 'Юг']
# arr = [[(80, 0), (100, -5)], [(-80, 0), (-140, -5)],
# [(0, 80), (-20, 100)], [(0, -80), (-10, -100)]]
# i = 0
# for a, b in arr:
#   t.goto(a)
#   t.up()
#   t.goto(b)
#   t.write(lst[i], font=f)
#   t.goto(0, 0)
#   t.down()
#   i += 1
#
# t.goto(0, -20)
# t.down()
# t.circle(20)

# import turtle as t, math
#
# t.Screen().bgcolor('black')
# colors = ['#ffff66','#ad5a00','#fd5a0A', 'cyan',
# '#FF6347','#ad5a00','#ad5a00','#20B2AA', '#4169E1','#ad5a00']
# f = ('Times New Roman', 11, 'normal')
# lst = [[(-150, 0), (-170, -20)], [(-80, 80), (-100, 60)],
# [(-40, 20), (-60, 5)], [(-80, -100), (-100, -120)], [(0, -120), (-10, -135)],
# [(60, 60), (40, 40)], [(110, -100), (90, -120)]]
#
# circ = [50, 10, 20, 15, 12, 40, 45]
# plan = ['Солнце', 'Меркурий', 'Венера', 'Эемля', 'Марс', 'Юпитер', 'Сатурн']
# i = 0
# t.up()
# for a, b in lst:
#   t.goto(a)
#   t.fillcolor(colors[i])
#   t.begin_fill()
#   t.circle(circ[i])
#   t.end_fill()
#   t.goto(b)
#   t.fillcolor('white')
#   t.write(plan[i], font=f)
#   i += 1
#
# t.goto(110, -85)
# t.pensize(5)
# t.down()
# t.pencolor('blue')
# a, b = 70, 30
# dx = t.xcor()
# dy = t.ycor()
# for deg in range(361):
#     rad = math.radians(deg)
#     x = a * math.sin(rad) + dx
#     y = -b * math.cos(rad) + b + dy
#     t.goto(x, y)


# import turtle
#
# turtle.speed()
# turtle.penup()
# rad = 50
# color = ['black', 'white', 'red']
#
# for i in range(3):
#     rad += -3
#     turtle.backward(rad / 2)
#
#     turtle.fillcolor(color[i])
#     turtle.begin_fill()
#     for _ in range(8):
#         turtle.forward(rad)
#         turtle.left(360 / 8)
#     turtle.end_fill()
#
#     turtle.forward(rad / 2)
#     turtle.left(90)
#     turtle.forward(3)
#     turtle.left(-90)
#
# turtle.left(90)
# turtle.forward(rad - 3)
# turtle.fillcolor(color[1])
# turtle.write('STOP', move=True, align='center', font=('Verdana', 18, 'bold'))


# import turtle, random
#
# turtle.Screen().bgcolor('black')
# turtle.speed(10)
# turtle.penup()
#
#
# def star():
#     size = random.randint(1, 3)
#     turtle.fillcolor('yellow')
#
#     x = random.randint(-200, 200)
#     y = random.randint(-10, 150)
#     turtle.goto(x, y)
#
#     turtle.begin_fill()
#     turtle.circle(size)
#     turtle.end_fill()
#
#
# for _ in range(random.randint(20, 30)):
#     star()
#
#
# def window(x, y):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.fillcolor('yellow')
#     turtle.begin_fill()
#
#     for _ in range(4):
#         turtle.forward(10)
#         turtle.left(90)
#     turtle.end_fill()
#
#
# turtle.goto(-200, -200)
#
#
# def buiding():
#     w = random.choice((30, 60, 90))
#     h = random.choice((120, 160, 180, 200))
#
#     turtle.fillcolor('blue')
#     turtle.begin_fill()
#     for _ in '12':
#         turtle.forward(w)
#         turtle.left(90)
#         turtle.forward(h)
#         turtle.left(90)
#     turtle.end_fill()
#
#     x = turtle.xcor()
#     y = turtle.ycor()
#
#     for _ in range(random.randint(1, 9)):
#         xw = random.randrange(round(x + 5), round(x + w) - 12, 15)
#         yw = random.randrange(round(y + 5), round(y + h) - 12, 15)
#         window(xw, yw)
#
#     turtle.goto(x + w, y)
#
#
# while buiding() < 200:
#     x = turtle.xcor()


# import turtle, random, math
# turtle.speed()
# turtle.penup()
# max = 2*math.pi/0.01
#
# turtle.fillcolor('red')
# turtle.begin_fill()
# for t in range(round(max)+1):
#   t += 0.01
#   x = 128*(math.sin(t))**3
#   y = 8*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t)-5)
#   turtle.goto(x,y)
# turtle.end_fill()

#
# import turtle
# import random
# def starUSSR(x, y, side):
#   turtle.penup()
#   turtle.goto(x, y)
#   turtle.right(random.randint(0, 360))
#   turtle.pendown()
#   color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
#   turtle.pencolor(color)
#   turtle.pendown()
#   turtle.fillcolor(color)
#   turtle.begin_fill()
#   for i in range(6):
#     turtle.forward(side)
#     turtle.right(144)
#   turtle.end_fill()
#   turtle.penup()
#
# def left_mouse_click(x, y):
#     #draw_circle(x, y, 10)
#     starUSSR(x, y, random.randint(3, 25))
#
# turtle.Screen().setup(400, 400)
# turtle.Screen().bgcolor('black')
# turtle.speed(0)
# turtle.tracer(5, 0)
# turtle.hideturtle()
# #turtle.penup()
# #turtle.right(random.randint(0, 360))
# #turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
#
#
# turtle.Screen().onclick(left_mouse_click)
# turtle.Screen().listen()