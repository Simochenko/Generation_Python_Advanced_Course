'''Тема урока: словари в Python
Новый тип коллекции
Отличия словарей от списков
Создание словарей
Обращение по ключу
Встроенная функция dict()
Создание словарей на основе списков и кортежей
Пустой словарь
Вывод словаря
Особенности словарей
Аннотация. В этом уроке мы начнем изучение словарей в Python, тип данных – dict. Этот тип данных похож на списки и
применяется при решении многих задач.

Словари
В прошлых уроках мы изучили четыре типа коллекций в Python:

списки – изменяемые коллекции элементов, индексируемые;
строки – неизменяемые коллекции символов, индексируемые;
кортежи – неизменяемые коллекции элементов, индексируемые;
множества – изменяемые коллекции уникальных элементов, неиндексируемые.
Следующий тип – словари – изменяемые коллекции элементов с произвольными индексами – ключами. Если в списках элементы
индексируются целыми числами, начиная с 0, то в словарях — любыми ключами, в том числе в виде строк.

Как нам уже известно, списки — удобный и самый популярный способ хранения большого количества данных в одной
переменной. Списки индексируют все хранящиеся в них элементы, что позволяет быстро обращаться к элементу, зная его
индекс.

Приведенный ниже код:

languages = ['Python', 'C#', 'Java', 'C++']

print(languages[0])
print(languages[2])
выводит:

Python
Java
Допустим, мы хотим хранить имя создателя каждого языка программирования. Это можно сделать несколькими способами.

Способ 1. Хранить еще один список, где по соответствующему индексу будет находиться имя создателя языка
программирования.

Приведенный ниже код:

languages = ['Python', 'C#', 'Java', 'C++']
creators = ['Гвидо ван Россум', 'Андерс Хейлсберг', 'Джеймс Гослинг', 'Бьёрн Страуструп']

print('Создателем языка', languages[0], 'является', creators[0])
выводит:

Создателем языка Python является Гвидо ван Россум
Подход рабочий, но хранить данные в двух коллекциях не очень удобно.

Способ 2. Хранить список кортежей с парами значений "язык - имя создателя" в каждом.

Приведенный ниже код:

languages = [('Python', 'Гвидо ван Россум'),
             ('C#', 'Андерс Хейлсберг'),
             ('Java', 'Джеймс Гослинг'),
             ('C++', 'Бьёрн Страуструп')]

print('Создателем языка', languages[2][0], 'является', languages[2][1])
выводит:

Создателем языка Java является Джеймс Гослинг
Тоже рабочий подход, однако не очень эффективный. Придется написать цикл for для поиска по всем элементам списка
languages кортежа, первый элемент которого равен искомому (названию языка). Чтобы найти автора языка C++ , нужно
 будет в цикле пройти мимо Python, C# и Java. Угадать заранее, что язык C++ лежит после них, не получится.

Приведенный ниже код:

languages = [('Python', 'Гвидо ван Россум'),
             ('C#', 'Андерс Хейлсберг'),
             ('Java', 'Джеймс Гослинг'),
             ('C++', 'Бьёрн Страуструп')]

for item in languages:
    if item[0] == 'C++':
        print('Создателем языка', item[0], 'является', item[1])
выводит:

Создателем языка C++ является Бьёрн Страуструп
Списки индексируются целыми числами, но в этом случае удобно было бы находить информацию не по числу, а по строке —
названию языка программирования. В списках строки не могут быть индексами, однако в словарях это возможно.

Словарь (тип данных dict), как и список, позволяет хранить много данных. В отличие от списка, в словаре для каждого
элемента можно произвольно определить «индекс» — ключ, по которому он будет доступен.

Словарь — реализация структуры данных "ассоциативный массив" или "хеш таблица". В других языках аналогичная структура
называется map, HashMap, Dictionary.

Создание словаря
Чтобы создать словарь, нужно перечислить его элементы, пары ключ—значение, через запятую в фигурных скобках, как и
элементы множества. Первым указывается ключ, после двоеточия — значение, доступное в словаре по этому ключу.

Приведенный ниже код:

languages = {'Python': 'Гвидо ван Россум',
             'C#': 'Андерс Хейлсберг',
             'Java': 'Джеймс Гослинг',
             'C++': 'Бьёрн Страуструп'}
создает словарь, в котором ключом служит строка — название языка программирования, а значением — имя создателя языка.

Обращение к элементу словаря
Извлечь значение элемента словаря можно обратившись к нему по его ключу. Чтобы получить значение по заданному ключу,
как и в списках, используем квадратные скобки [] , индексируем по ключу.

Способ 3. Приведенный ниже код:

languages = {'Python': 'Гвидо ван Россум',
             'C#': 'Андерс Хейлсберг',
             'Java': 'Джеймс Гослинг',
             'C++': 'Бьёрн Страуструп'}

print('Создателем языка C# является', languages['C#'])
выводит:

Создателем языка C# является Андерс Хейлсберг
В отличие от списков, номеров позиций в словарях нет.

Приведенный ниже код:

languages = {'Python': 'Гвидо ван Россум',
             'C#': 'Андерс Хейлсберг',
             'Java': 'Джеймс Гослинг',
             'C++': 'Бьёрн Страуструп'}

print('Создателем языка C# является', languages[1])
приводит к возникновению ошибки KeyError.

Ошибка KeyError возникнет и при попытке извлечь значение по несуществующему ключу. В качестве ключа можно указать
выражение, Python вычислит его значение, и обратится к искомому элементу.

Способ 4. Приведенный ниже код:

languages = {'Python': 'Гвидо ван Россум',
             'C#': 'Андерс Хейлсберг',
             'Java': 'Джеймс Гослинг',
             'C++': 'Бьёрн Страуструп'}

print('Создателем языка C# является', languages['C' + '#'])
выводит:

Создателем языка C# является Андерс Хейлсберг
Создание словаря с помощью функции dict()
Если ключи словаря — строки, без каких-либо специальных символов, то для создания словаря можно использовать функцию
 dict() .

Приведенный ниже код:

info = dict(name = 'Timur', age = 28, job = 'Teacher')
создает словарь с тремя элементами, ключами которого служат строки 'name', 'age', 'job', а значениями: 'Timur', 28,
'Teacher'.

Создание словаря на основании списков и кортежей
Создавать словари можно на основе списков кортежей или кортежей списков. Первый элемент списка или кортежа станет
ключом, второй — значением.

Приведенный ниже код:

info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей

info_dict = dict(info_list)  # создаем словарь на основе списка кортежей
создает словарь с тремя элементами, где ключи — строки name, age, job, а соответствующие им значения — 'Timur',
28, 'Teacher'.

Аналогично работает приведенный ниже код:

info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков

info_dict = dict(info_tuple)  # создаем словарь на основе кортежа списков
Если необходимо создать словарь, каждому ключу которого соответствует одно и то же значение, можно воспользоваться
методом fromkeys().

Приведенный ниже код:

dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')
создает словарь с тремя элементами, где ключи — строки 'name', 'age', 'job', а соответствующие им значения: 'Missed
information', 'Missed information', 'Missed information'.

   Если методу fromkeys() не передать второй параметр, то по умолчанию присваивается значение None.

Приведенный ниже код:

dict1 = dict.fromkeys(['name', 'age', 'job'])
создает словарь с тремя элементами, в которых ключи — строки 'name', 'age', 'job', а значения — None, None, None.

Пустой словарь
Пустой словарь можно создать двумя способами:

с помощью пустых фигурных скобок;
с помощью функции dict().
Приведенный ниже код:

dict1 = {}
dict2 = dict()


print(dict1)
print(dict2)
print(type(dict1))
print(type(dict2))
создает два пустых словаря и выводит:

{}
{}
<class 'dict'>
<class 'dict'>
Вспомните, что создать пустое множество можно, только используя функцию set() , потому что пустые фигурные скобки
зарезервированы для создания словаря.

Вывод словаря
Для вывода всего словаря можно использовать функцию print():

languages = {'Python': 'Гвидо ван Россум',
             'C#': 'Андерс Хейлсберг',
             'Java': 'Джеймс Гослинг'}

info = dict(name = 'Timur', age = 28, job = 'Teacher')

print(languages)
print(info)
Функция print() выводит на экран элементы словаря, в фигурных скобках, разделенные запятыми:

{'Python': 'Гвидо ван Россум', 'C#': 'Андерс Хейлсберг', 'Java': 'Джеймс Гослинг'}
{'name': 'Timur', 'age': 28, 'job': 'Teacher'}
Начиная с версии Python 3.6 словари являются упорядоченными, то есть сохраняют порядок следования ключей в порядке их
 внесения в словарь.

Примечания
Примечание 1. Словари принципиально отличаются от списков по структуре хранения в памяти. Список — последовательная
область памяти, то есть все его элементы (указатели на элементы) действительно хранятся в указанном порядке,
 расположены последовательно. Благодаря этому и можно быстро «прыгнуть» к элементу по его индексу. В словаре же
 используется специальная структура данных — хеш-таблица. Она позволяет вычислять числовой хеш от ключа и использовать
 обычные списки, где в качестве индекса элемента берется этот хеш.

Примечание 2. В рамках одного словаря каждый ключ уникален.

Примечание 3. Словари удобно использовать для хранения различных сущностей. Например, если нужно работать с
информацией о человеке, то можно хранить все необходимые сведения, включающие такие разные сущности как "возраст",
 "профессия", "название города", "адрес электронной почты" в одном словаре  info и легко обращаться к его элементам
 по ключам:

info = {'name': 'Timur',
        'age': 28,
        'job': 'Teacher',
        'city': 'Moscow',
        'email': 'timyr-guev@yandex.ru'}

print(info['name'])
print(info['email'])


Примечание 4. Создать словарь на основании двух списков (кортежей) можно с помощью встроенной функции-упаковщика zip(),
 о которой расскажем позже.

Приведенный ниже код:

keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']

info = dict(zip(keys, values))

print(info)
выводит (порядок элементов может отличаться):

{'name': 'Timur', 'age': 28, 'job': 'Teacher'}
   В случае несовпадения длины списков, функция самостоятельно отсечет лишние элементы.'''

# my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
#
# print(my_dict[2][1])


'''Особенности словарей
Словари (тип данных dict) довольно просты, но о нескольких моментах следует помнить при их использовании.

Ключи должны быть уникальными
Словарь не может иметь два и более значений по одному и тому же ключу. Если при создании словаря (в литеральной форме) 
указать дважды один и тот же ключ, будет использовано последнее из указанных значений.

Приведенный ниже код:

info = {'name': 'Ruslan',
        'age': 28,
        'name': 'Timur'}

print(info['name'])
выводит:

Timur
Ключи должны быть неизменяемым типом данных
Ключом словаря могут быть данные любого неизменяемого типа:

число;
строка;
булево значение;
кортеж;
замороженное множество (frozenset);
...
Приведенный ниже код создает словарь, ключами которого являются неизменяемые типы данных:

my_dict = {198: 'beegeek', 'name': 'Bob', True: 'a', (2, 2): 25}
Ключ словаря не может относиться к изменяемому типу данных:

список;
множество;
словарь;
...
Приведенный ниже код приводит к возникновению ошибки:

my_dict = {[2, 2]: 25, {1, 2}: 'python', 'name': 'Bob'}
Значения могут относиться к любому типу данных, их тип данных произволен
Нет никаких ограничений для значений, хранящихся в словарях. Значения в словарях могут принадлежать к произвольному 
типу данных и повторяться для разных ключей многократно.

my_dict1 = {'a': [1, 2, 3], 'b': {1, 2, 3}}           # значения – изменяемый тип данных 

my_dict2 = {'a': [1, 2], 'b': [1, 2], 'c': [1, 2]}    # значения повторяются'''