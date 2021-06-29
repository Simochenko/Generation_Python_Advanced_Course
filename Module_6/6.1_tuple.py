"""Тема урока: кортежи
Тип данных tuple
Особенности работы с кортежами
Аннотация. Урок посвящен кортежам (тип данных tuple).

Мы изучили списки и строки. Списки – изменяемые коллекции, строки – неизменяемымые последовательности Unicode символов.
В Python имеются и неизменяемые последовательности содержащие, в отличие от строк, абсолютно произвольные данные.
Такие коллекции называются кортежами (tuple, читается "тюпл").

Кортежи
Рассмотрим следующий программный код:

my_list = [1, 2, 3, 4, 5]
Мы объявили список чисел и присвоили его переменной my_list. Содержимое списка можно изменять.

Следующий программный код:

my_list = [1, 2, 3, 4, 5]
my_list[0] = 9
my_list[4] = 7
print(my_list)
выведет:

[9, 2, 3, 4, 7]
Заменив квадратные скобки при объявлении списка на круглые, мы объявляем кортеж:

my_tuple = (1, 2, 3, 4, 5)
Кортежи по своей природе (задумке) – неизменяемые аналоги списков. Поэтому программный код:

my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 9
my_tuple[4] = 7
print(my_tuple)
приводит к ошибке

TypeError: 'tuple' object does not support item assignment
   Кортеж (tuple) – ещё один вид коллекций в Python. Похож на список, но, в отличие от списка, неизменяемый.

В литеральной форме кортеж записывается в виде последовательности элементов в круглых скобках, а список – в квадратных.

Примеры кортежей
empty_tuple = ()                                      # пустой кортеж
point = (1.5, 6.0)                                    # кортеж из двух чисел
names = ('Timur', 'Ruslan', 'Roman')                  # кортеж из трех строк
info = ('Timur', 'Guev', 28, 170, 60, False)          # кортеж из 6 элементов разных типов
nested_tuple = (('one', 'two'), ['three', 'four'])    # кортеж из кортежа и списка
в переменной empty_tuple хранится пустой кортеж;
в переменной point хранится кортеж, состоящий из двух вещественных чисел (такой кортеж удобно использовать для
представления точки на координатной плоскости);
в переменной names хранится кортеж, содержащий три строковых значения;
в переменной info содержится кортеж, содержащий 66 элементов разного типа (строки, числа, булевы переменные);
в переменной nested_tuple содержится кортеж, содержащий другой кортеж и список.
Кортежи могут хранить и содержать в себе объекты любых типов (даже составных) и поддерживают неограниченное количество
уровней вложенности.

Кортеж с одним элементом
Для создания кортежа с единственным элементом после значения элемента ставят замыкающую запятую:

my_tuple = (1,)
print(type(my_tuple))     # <class 'tuple'>
Если запятую пропустить, то кортеж создан не будет. Например, приведенный ниже код просто присваивает переменной
my_tuple целочисленное значение 1:

my_tuple = (1)
print(type(my_tuple))     # <class 'int'>
Зачем использовать кортеж вместо списка?
Списки могут делать то же, что кортежи, и даже больше. Но неизменяемость кортежей обеспечивает им особые свойства:

скорость – кортежи быстрее работают, так как из-за неизменяемости хранятся в памяти иначе, и операции с их элементами
выполняются заведомо быстрее, чем с компонентами списка. Одна из причин существования кортежей  – производительность.
 Обработка кортежа выполняется быстрее, чем обработка списка, поэтому кортежи удобны для обработки большого объема
  неизменных данных.
безопасность – неизменяемость превращает их в идеальные константы. Заданные кортежами константы делают код более
читаемым и безопасным. Кроме того, в кортеже можно безопасно хранить данные, не опасаясь, что они будут случайно
или преднамеренно изменены в программе.
В Python существуют операции, требующие применения кортежа. По мере освоения языка Python вы будете чаще сталкиваться
с кортежами.

Примечания
Примечание 1. Мы уже  сталкивались с кортежами, когда изучали функции, возвращающие несколько значений. Такие функции
 возвращают именно кортежи.

Рассмотрим функцию get_powers(), которая принимает в качестве аргумента число и возвращает его 2, 3 и 4 степень.

def get_powers(num):
    return num**2, num**3, num**4
Результатом выполнения следующего кода:

result = get_powers(5)
print(type(result))
print(result)
будет:

<class 'tuple'>
(25, 125, 625)
Примечание 2. Списки предназначены для объединения неопределенного количества однородных сущностей. Кортежи, как
правило, объединяют под одним именем несколько разнородных объектов, имеющих различный смысл.

Примечание 3. Тот факт, что кортеж является неизменяемым вовсе не означает, что мы не можем поменять содержимое
списка в кортеже.

Приведенный ниже код:

my_tuple = (1, 'python', [1, 2, 3])
print(my_tuple)
my_tuple[2][0] = 100
my_tuple[2].append(17)
print(my_tuple)
выводит:

(1, 'python', [1, 2, 3])
(1, 'python', [100, 2, 3, 17])
При этом важно понимать: меняется список, а не кортеж. Списки являются ссылочными типами данных, поэтому в кортеже
хранится ссылка на список, которая не меняется при изменении самого списка."""
