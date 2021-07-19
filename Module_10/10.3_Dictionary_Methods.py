'''Тема урока: методы словарей
Добавление и изменение элементов в словаре
Удаление элементов из словаря
Методы get(), update()
Методы pop(), popitem()
Методы clear(), copy()
Метод setdefault()
Аннотация. В этом уроке мы изучим основные методы словарей.

Методы словарей
Словари как и списки имеют много полезных методов для упрощения работы с ними и решения повседневных задач. В прошлом
 уроке, мы уже познакомились с тремя словарными методами:

метод items() – возвращает словарные пары ключ: значение, как соответствующие им кортежи;
метод keys() – возвращает список ключей словаря;
метод values() – возвращает список значений словаря.
Добавление и изменение элементов в словаре
Чтобы изменить значение по определенному ключу в словаре, достаточно использовать индексацию вместе с оператором
 присвоения. При этом если ключ уже присутствует в словаре, его значение заменяется новым, если же ключ отсутствует,
 то в словарь будет добавлен новый элемент.

Приведенный ниже код:

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher'}

info['name'] = 'Timur'                    # изменяем значение по ключу name
info['email'] = 'timyr-guev@yandex.ru'    # добавляем в словарь элемент с ключом email

print(info)
выводит (порядок элементов может отличаться):

{'name': 'Timur', 'age': 28, 'job': 'Teacher', 'email': 'timyr-guev@yandex.ru'}
Обратите внимание на отличие в поведении словарей и списков:

Если в списке lst нет элемента с индексом 77, то попытка обращения к нему, например, с помощью строки кода
print(lst[7]) приведет к возникновению ошибки. И попытка присвоить ему значение lst[7] = 100 тоже приведет к
возникновению ошибки.
Если в словаре dct нет элемента с ключом name, то попытка обращения к нему, например, с помощью строки кода
print(dct['name']) приведет к возникновению ошибки. Однако попытка присвоить значение по отсутствующему ключу
dct['name'] = 'Timur' ошибки не вызовет.
Решим следующую задачу: пусть задан список чисел numbers , где некоторые числа встречаются неоднократно. Нужно
узнать, сколько именно раз встречается каждое из чисел.

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
Первый код, который приходит в голову имеет вид:

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] += 1
Однако, просто так сделать result[num] += 1 нельзя, так как если ключа num в словаре еще нет, то возникнет ошибка
KeyError.

Следующий программный код, полностью решает поставленную задачу:

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1
Цикл for перебирает все элементы списка numbers и для каждого проверяет, присутствует ли он уже в качестве ключа в
словаре result. Если значение отсутствует, значит число встретилось впервые и мы инициируем значение result[num] = 1.
 Если значение уже присутствует в словаре, увеличим result[num] на единицу.

Этот код можно улучшить с помощью метода get().

Метод get()
Мы можем получить значение в словаре по ключу с помощью индексации, то есть квадратных скобок. Однако как мы знаем, в
случае отсутствия ключа будет происходить ошибка KeyError.

Приведенный ниже код:

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

print(info['name'])
выводит:

Bob
Приведенный ниже код:

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

print(info['salary'])
приводит к возникновению ошибки:

KeyError: 'salary'
Для того, чтобы избежать возникновения ошибки в случае отсутствия ключа в словаре можно использовать метод get(),
способный кроме ключа принимать и второй аргумент — значение, которое вернется, если заданного ключа нет. Когда второй
аргумент не указан, то метод в случае отсутствия ключа возвращает None.

Приведенный ниже код:

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

item1 = info.get('salary')
item2 = info.get('salary', 'Информации о зарплате нет')

print(item1)
print(item2)
выводит:

None
Информации о зарплате нет
   С помощью словарного метода get(), можно упростить код в задаче о повторяющихся числах.

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
Цикл for перебирает все элементы списка numbers и для каждого элемента с помощью метода get() мы получаем либо его
значение из словаря, либо значение по умолчанию, равное 00. К данному значению прибавляется единица, и результат
 записывается обратно в словарь по нужному ключу.

Метод update()
Метод update() – реализует своеобразную операцию конкатенации для словарей. Он объединяет ключи и значения одного
 словаря с ключами и значениями другого. При совпадении ключей в итоге сохранится значение словаря, указанного в
 качестве аргумента метода update().

Приведенный ниже код:

info1 = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info2 = {'age': 30,
        'city': 'New York',
        'email': 'bob@web.com'}

info1.update(info2)

print(info1)
выводит (порядок элементов может отличаться):

{'name': 'Bob', 'age': 30, 'job': 'Dev', 'city': 'New York', 'email': 'bob@web.com'}
В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей.

Приведенный ниже код:

info1 = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info2 = {'age': 30,
        'city': 'New York',
        'email': 'bob@web.com'}

info1 |= info2

print(info1)
аналогичен предыдущему коду.

Метод setdefault()
Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря,
 если он отсутствует.

Метод принимает два аргумента:

 key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
 default: значение, которое будет использовано при добавлении нового элемента в словарь.
В зависимости от значений параметров key и default возможны следующие сценарии работы данного метода.

Сценарий 1. Если ключ key присутствует в словаре, то метод возвращает значение по заданному ключу (независимо от того,
передан параметр default или нет).

Приведенный ниже код:

info = {'name': 'Bob',
        'age': 25}

name1 = info.setdefault('name')           # параметр default не задан
name2 = info.setdefault('name', 'Max')    # параметр default задан

print(name1)
print(name2)
выводит:

Bob
Bob
Сценарий 2. Если ключ key отсутствует в словаре, то метод вставляет переданное значение default по заданному ключу.

Приведенный ниже код:

info = {'name': 'Bob',
        'age': 25}

job = info.setdefault('job', 'Dev')
print(info)
print(job)
выводит:

{'name': 'Bob', 'age': 25, 'job': 'Dev'}
Dev
При этом если значение default не передано в метод, то вставится значение None.

Приведенный ниже код:

info = {'name': 'Bob',
        'age': 25}

job = info.setdefault('job')
print(info)
print(job)
выводит:

{'name': 'Bob', 'age': 25, 'job': None}
None
Удаление элементов из словаря
Существует несколько способов удаления элементов из словаря:

оператор del;
метод pop();
метод popitem();
метод clear().
Оператор del
С помощью оператора del можно удалять элементы словаря по определенному ключу.

Следующий программный код:

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

del info['email']    # удаляем элемент имеющий ключ email
del info['job']      # удаляем элемент имеющий ключ job

print(info)
выводит (порядок элементов может отличаться):

{'name': 'Sam', 'age': 28}
​   Если удаляемого ключа в словаре нет, возникнет ошибка KeyError.

Метод pop()
Оператор del удаляет из словаря элемент по заданному ключу вместе с его значением. Если требуется получить само
значение удаляемого элемента, то нужен метод pop().

Следующий программный код:

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение

print(email)
print(job)
print(info)
выводит:

timyr-guev@yandex.ru
Teacher
{'name': 'Sam', 'age': 28}
Единственное отличие этого способа удаления от оператора del — он возвращает удаленное значение. В остальном этот
способ идентичен оператору del. В частности, если удаляемого ключа в словаре нет, возникнет ошибка KeyError.

​Чтобы ошибка не появлялась, этому методу можно передать второй аргумент. Он будет возвращен, если указанного
ключа в словаре нет. Это позволяет реализовать безопасное удаление элемента из словаря:

surname = info.pop('surname', None)
Если ключа surname в словаре нет, то в переменной surname будет храниться значение None.

Метод popitem()
Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа
(ключ, значение).

Следующий программный код:

info = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

info['surname'] = 'Sinclar'

item = info.popitem()

print(item)
print(info)
выводит:

('surname', 'Sinclar')
{'name': 'Bob', 'age': 25, 'job': 'Dev'}
  В версиях Python ниже 3.6 метод popitem() удалял случайный элемент.

Метод clear()
Метод clear() удаляет все элементы из словаря.

Следующий программный код:

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info.clear()

print(info)
выведет:

{}
Метод copy()
Метод copy() создает поверхностную копию словаря.

Следующий программный код:

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info_copy = info.copy()

print(info_copy)
выведет:

{'name': 'Bob', 'age': 25, 'job': 'Dev'}
Не стоит путать копирование словаря (метод copy()) и присвоение новой переменной ссылки на старый словарь.

Следующий программный код:

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

new_info = info
new_info['name'] = 'Tim'

print(info)
выводит:

{'name': 'Tim', 'age': 25, 'job': 'Dev'}
Оператор присваивания (=) не копирует словарь, а лишь присваивает ссылку на старый словарь новой переменной.



Таким образом, когда мы изменяем словарь new_info, меняется и словарь info. Если необходимо изменить один словарь,
не изменяя второй, используют метод copy().

Следующий программный код:

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

new_info = info.copy()
new_info['name'] = 'Tim'

print(info)
print(new_info)
выводит:

{'name': 'Bob', 'age': 25, 'job': 'Dev'}
{'name': 'Tim', 'age': 25, 'job': 'Dev'}
Примечания
Примечание 1. Словарь можно использовать вместо нескольких вложенных условий, если вам нужно проверить число на
 равенство. Например вместо

num = int(input())

if num == 1:
    description = 'One'
elif num == 2:
    description = 'Two'
elif num == 3:
    description = 'Three'
else:
    description = 'Unknown'

print(description)
можно написать

num = int(input())

description = {1: 'One', 2: 'Two', 3: 'Three'}

print(description.get(num, 'Unknown'))
На практике, такой код встречается достаточно часто. Особенно если в программе необходимо часто осуществлять проверку
указанного типа.

'''

'''
get()
update()
pop()
popitem()
clear()
copy()
items()
keys()
values()
получает значение в словаре по ключу
объединяет словари
возвращает значение по указанному ключу, удаляя из словаря пару (ключ, значение)
возвращает последнюю добавленную пару (ключ, значение), удаляя её из словаря
удаляет все элементы из словаря
создает копию словаря
возвращает элементы словаря в виде пар (ключ, значение)
возвращает список ключей словаря
возвращает список значений словаря'''

'''Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 1 до 15 
(включительно), а значения представляют собой квадраты ключей.

Примечание. Выводить содержимое словаря result не нужно.'''

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + num**2
# print(result)

# result = {}
# result = {i: i**2 for i in range(1, 16)}

# result = dict(zip(range(1, 16), [i * i for i in range(1, 16)]))
# print(result)

'''Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, складывая 
значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий словарь 
необходимо присвоить переменной result.

Примечание. Выводить содержимое словаря result не нужно.'''

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
#
# def task(d1, d2):
#     k = set(list(d1.keys()) + list(d2.keys()))
#
#     for a in k:
#         v1 = d1.get(a)
#         v2 = d2.get(a)
#         if v1 == None:
#             v = v2
#         elif v2 == None:
#             v = v1
#         else:
#             v = v1 + v2
#         result[a] = v
#     return  result
#
# print(task(dict1,dict2))


# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {i: dict1.get(i, 0) + dict2.get(i, 0) for i in set(dict1.keys() | dict2.keys())}


# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
# result.update(dict1)
# for i in dict2:
#     result[i] = result.get(i, 0) + dict2[i]

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = dict1.copy()
#
# for i in dict2:
#     result[i] = result.get(i, 0) + dict2[i]


# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = dict1.copy()
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {i: dict1.get(i, 0) + dict2.get(i, 0) for i in set(dict1.keys()) | set(dict2.keys())}


'''Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки 
text будет подсчитано количество его вхождений.

Примечание. Выводить содержимое словаря result не нужно.'''

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for num in text:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
# print(result)

# result = {elem: text.count(elem) for elem in set(text)}


# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for symbol in text:
#     result[symbol] = result.get(symbol, 0) + 1

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for s in set(text):
#     result[s] = text.count(s)

'''Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, 
должно быть выведено то, что меньше в лексикографическом порядке.'''
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
#     'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
#     'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate ' \
#     'barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot' \
#     ' currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince ' \
#     'currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# counter = {}
# line = s.split()
# for word in line:
#     counter[word] = counter.get(word, 0) + 1
#
# max_count = max(counter.values())
# most_frequent = [k for k, v in counter.items() if v == max_count]
# print(min(most_frequent))

# s = 'orange strawberry gooseberry apple apricot currant orange melon pomegranate banana banana orange apricot ' \
#     'plum grapefruit banana quince strawberry grapefruit banana grapes melon strawberry apricot currant currant ' \
#     'gooseberry raspberry apricot currant orange lime quince grapefruit banana melon pomegranate banana orange ' \
#     'apricot plum banana quince lime grapefruit strawberry gooseberry apple apricot currant orange melon pomegranate' \
#     ' banana banana orange apricot plum banana grapefruit banana quince currant orange melon pomegranate plum ' \
#     'banana quince lime grapefruit pomegranate'.split()
# d={}
# for c in s:
#     d[c]=d.get(c,0)+1
# d=sorted(d.items(),key=lambda para:(-para[1],para[0]))
# print(d[0][0])

# from collections import Counter
# s = 'orange strawberry gooseberry apple apricot currant orange melon pomegranate banana banana orange apricot plum grapefruit banana quince strawberry grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit banana melon pomegranate banana orange apricot plum banana quince lime grapefruit strawberry gooseberry apple apricot currant orange melon pomegranate banana banana orange apricot plum banana grapefruit banana quince currant orange melon pomegranate plum banana quince lime grapefruit pomegranate'
# res = Counter(s.split()).most_common(1)[0][0]
# print(res)


'''Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж
 вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).

Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут
 перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список
  кличек собак (сохранив исходный порядок следования).

Примечание 1. Не забывайте: кортежи являются неизменямыми, поэтому могут быть ключами словаря.

Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.

Примечание 3. Выводить содержимое словаря result не нужно.'''
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
#
#
# def dog_owners(pets):
#     val = []
#     for el in pets:
#         val.append(el[0])
#     m_key = []
#     for el in pets:
#         m_key.append(el[1:4])
#     for x, y in zip(val, m_key):
#         result.setdefault(y, []).append(x)
#     return result
#
#
# print(dog_owners(pets))


# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for pet in pets:
#     result.setdefault(pet[1:], []).append(pet[0])
#
# print(result)

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for i in pets:
#     result[i[1:]] = result.get(i[1:], []) + i[0].split()


# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {o : [p[0] for p in pets if p[1:] == o] for o in set(d[1:] for d in pets)}


# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for i in pets:
#     result[i[1::]] = (result.get(i[1::], []) + (i[0] + " ").split())

'''Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, 
без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как 
одинаковые.

Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки
 препинания .,!?:;-. Других символов в тексте нет.

Sample Input 1:

home sweet home
Sample Output 1:

sweet
Sample Input 2:

home sweet home sweet.
Sample Output 2:

home'''

# s = input()
# counter = {}
#
# text=s.lower()
# for c in ',/.!?+=-':
#     text = text.replace(c, '')
# print(text)
#
# for word in text.split():
#     counter[word] = counter.get(word, 0) + 1
#
# max_count = min(counter.values())
# most_frequent = [k for k, v in counter.items() if v == max_count]
# print(min(most_frequent))


# d = {}
# for w in input().split():
#     w = w.strip('.,!?:;-').lower()
#     d[w] = d.get(w, 0) + 1
# print(min(d.items(), key=lambda x: (x[1], x[0]))[0])


# st = [i.strip('.,!?:;-') for i in input().lower().split()]
#
# print(min(st, key=lambda x: (st.count(x), x)))


# dct = {}
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# for word in lst:
#     dct[word] = dct.get(word, 0) + 1
# lst = [(value, key) for key, value in dct.items()]
# lst.sort()
# print(lst[0][1])

# (lambda s: print(sorted({c: s.count(c) for c in set(s)}.items(), key=lambda x: (x[1], x[0]))[0][0]))(__import__('re').findall(r'\w+', input().lower()))


'''Исправление дубликатов 🌶️
На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, 
чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам
 постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.

Формат входных данных
На вход программе подается строка текста, содержащая строк-идентификаторов, разделенные символом пробела.

Формат выходных данных
Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.

Sample Input 1:

a b c a a d c
Sample Output 1:

a b c a_1 a_2 d c_1
Sample Input 2:

a b c
Sample Output 2:

a b c
Sample Input 3:

i am i r o n m a n
Sample Output 3:

i am i_1 r o n m a n_1
Sample Input 4:

a a a a a
Sample Output 4:

a a_1 a_2 a_3 a_4'''

# ids = input().split()
# def fix_duplicates(ids):
#     result = []
#     for i, e in enumerate(ids):
#         count = ids[:i].count(e)
#         appendix = f'_{count}' if count else ''
#         result.append(f'{e}{appendix}')
#     return result
#
# print(*fix_duplicates(ids))


# lst = input().split()
# res = {}
# for c in lst:
#     if c in res:
#         print(f'{c}_{res[c]}', end=' ')
#     else:
#         print(c, end=' ')
#     res[c] = res.get(c, 0) + 1


# print(*[l[i] + (l[i] in l[:i]) * ('_' + str(l[:i].count(l[i]))) for l in [input().split()] for i in range(len(l))])


# d, res = {}, []
# for w in input().split():
#     n = d[w] = d.get(w, -1) + 1
#     res.append(f'{w}_{n}' if n > 0 else w)
# print(*res)


# a=input().split()
# for i in range(len(a)):
#     if a[i] not in a[:i]:
#         print(a[i],end=' ')
#     else:
#         print(f"{a[i]}_{a[:i].count(a[i])}", end=' ')


# text = input().split()
# d_text, new_text = {}, []
# for sym in text:
#     if sym not in d_text:
#         new_text.append(sym)
#         d_text[sym] = 0
#     else:
#         d_text[sym] += 1
#         new_text.append(f"{sym}_{d_text[sym]}")
# print(*new_text)