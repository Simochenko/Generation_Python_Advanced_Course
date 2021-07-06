'''Тема урока: генераторы множеств, frozenset
Генераторы множеств
Неизменяемые множества frozenset
Аннотация. Урок посвящен генераторам множеств и типу данных frozenset.

Генераторы множеств
Пусть требуется создать множество, содержащее цифры введенного числа.

Следующий программный код:

digits = set(int(input()))
приводит к ошибке

TypeError: 'int' object is not iterable
поскольку функция set() принимает в качестве аргумента итерируемый объект, а число (тип данных int) таковым не является.

Следующий программный код:

digits = set(input())
при вводе строки '12345' создает множество символов {'1', '2', '3', '4', '5'}, а не множество цифр {1, 2, 3, 4, 5}.

Для создания требуемого множества, содержащего уникальные цифры введенного числа, нам придется написать код:

digits = set()

for c in input():
    digits.add(int(c))
Такой код хоть и не сложен, однако достаточно громоздок.

Для создания множеств в Python можно использовать специальный синтаксис, как при создании списка.

Приведенный выше код можно переписать с использованием генератора множеств:

digits = {int(c) for c in input()}
Общий вид генератора множеств следующий:

{выражение for переменная in последовательность}

где  выражение — некоторое выражение, как правило, зависящее от использованной в списочном выражении переменной,
 которым будут заполнены элементы множества переменная — имя некоторой переменной, последовательность —
 последовательность значений, которые она принимает (любой итерируемый объект).

Примеры использования генератора множеств
1. Создать множество, заполненное квадратами целых чисел от 0 до 9 можно так:

squares = {i ** 2 for i in range(10)}
2. Создать множество, заполненное кубами целых чисел от 10 до 20 можно так:

cubes = {i ** 3 for i in range(10, 21)}
3. Создать множество, заполненное символами строки можно так:

chars = {c for c in 'abcdefg'}
Условия в генераторе множеств
В генераторах множеств можно использовать условный оператор. Например, если требуется создать множество, заполненное
только цифрами некоторой строки, то мы можем написать такой код:

digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}'''
import os

'''Дополните приведенный код, используя генератор, чтобы получить множество, содержащее уникальные значения списка 
items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.

Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо
 трактовать как числа.

Примечание 2. Чтобы вывести элементы множества в упорядоченном виде используйте следующий код:

print(*sorted(myset))'''

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# mylist = {int(c) for c in items}
# print(*sorted((mylist)))


'''Дополните приведенный код, используя генератор, чтобы получить множество, содержащее уникальные первые символы
 слов (в нижнем регистре) списка words. Результат вывести на одной строке в алфавитном порядке, разделяя элементы 
 одним символом пробела.'''

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
#          'tangerine', 'Watermelon', 'currant', 'Almond']
# mylist = {c.lower()[0] for c in words}
# print(*sorted((list(mylist))))

#
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry,' 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# print(*sorted({word[0].lower() for word in words}))


'''Дополните приведенный код, используя генератор, чтобы получить множество, содержащее уникальные слова 
(в нижнем регистре) строки sentence. Результат вывести на одной строке, в отсортированном по возрастанию виде, 
разделяя элементы одним символом пробела.

Примечание. Учтите, что знаки пунктуации не относятся к словам.'''

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for
#  a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which,
#   if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all
#   know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#   traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# import re
# words = re.sub(r'[:,.!?();]', '', sentence.lower())
# print(*sorted(set(words.split())))


# import re
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for
#  a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which,
#   if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all
#   know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#   traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# print(*sorted(set(re.findall(r'\w+', sentence.lower()))))


'''Дополните приведенный код, используя генератор, чтобы получить множество, содержащее уникальные слова (в нижнем
 регистре) строки sentence длиною меньше 44 символов. Результат вывести на одной строке, в отсортированном по
  возрастанию виде, разделяя элементы одним символом пробела.
Примечание. Учтите, что знаки пунктуации не относятся к словам.'''

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
#  pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
#   you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#   those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#   traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# myset={c.lower().strip('.,():;') for c in sentence.split() if len(c.lower().strip('.,():;'))<4}
# print(*sorted(myset), sep=' ')

# print(*sorted(filter(lambda i: len(i) < 4, {j.lower().strip('( .,: ;)') for j in '''My very photogenic mother died
# in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past,
# nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style
# (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of
# day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the
# bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''.split()})))

'''Дополните приведенный код, используя генератор, чтобы получить множество, содержащее уникальные имена файлов с 
расширением в нижнем регистре, имеющих независимое от регистра расширение .png. Результат вывести на одной строке,
 в отсортированном по возрастанию виде, разделяя элементы одним символом пробела.'''

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']
# mylist = {c.lower() for c in files if c.lower()[-4:]=='.png'}
# print(*sorted((list(mylist))))

# print(*sorted({w[:-4] for w in set(map(str.lower, files)) if w[-4:] == '.png'}))

# myset={ c.lower() for c in files if c[-3::].lower()=='png'}
# print(*sorted(myset))

'''Frozenset
Замороженное множество (frozenset) также является встроенной коллекцией в Python. Обладая характеристиками обычного 
множества, замороженное множество не может быть изменено после создания.

Кортеж (тип tuple) – неизменяемая версия списка (тип list), а замороженное множество (тип frozenset) – неизменяемая
 версия обычного множества (тип set).

Для создания замороженного множества используется встроенная функция frozenset(), которая принимает в качестве
 аргумента другую коллекцию.

Приведенный ниже код:

myset1 = frozenset({1, 2, 3})                         # на основе множества
myset2 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])    # на основе списка
myset3 = frozenset('aabcccddee')                      # на основе строки

print(myset1)
print(myset2)
print(myset3)
выводит:

frozenset({1, 2, 3})
frozenset({1, 2, 3, 4, 5, 6})
frozenset({'e', 'd', 'c', 'b', 'a'})
Операции над замороженными множествами
Над замороженными множествами можно производить все операции, которые можно производить над обычными множествами:

объединение множеств: метод union() или оператор |;
пересечение множеств: метод intersection() или оператор &;
разность множеств: метод difference() или оператор -;
симметрическая разность множеств: метод symmetric_difference() или оператор ^.
Приведенный ниже код:

myset1 = frozenset('hello')
myset2 = frozenset('world')

print(myset1 | myset2)
print(myset1 & myset2)
print(myset1 ^ myset2)
выводит:

frozenset({'l', 'w', 'e', 'h', 'r', 'd', 'o'})
frozenset({'l', 'o'})
frozenset({'d', 'h', 'w', 'e', 'r'})
   Результатом операций над замороженными множествами будут тоже замороженные множества.

Примечания
Примечание 1. Будучи изменяемыми, обычные множества не могут быть элементами других множеств. Замороженные множества 
являются неизменяемыми, а значит могут быть элементами других множеств.

Приведенный ниже код:

sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'

words = sentence.lower().replace('.', '').replace(',', '').split()

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}

print(*consonants, sep='\n')
выводит (порядок элементов может отличаться):

frozenset({'d', 'h'})
frozenset({'h', 't'})
frozenset({'n', 'h', 'g', 't'})
frozenset({'n'})
frozenset({'c', 't'})
frozenset({'n', 'd'})
frozenset({'w', 't'})
frozenset({'s', 'c', 'k', 'd'})
Примечание 2. Методы изменяющие множество отсутствуют у замороженных множеств:

add()
remove()
discard()
pop()
clear()
update()
intersection_update()
difference_update()
symmetric_difference_update()
Примечание 3. Мы можем сравнивать простые (тип set) и замороженные множества (тип frozenset).

Приведенный ниже код:

myset1 = set('qwerty')
myset2 = frozenset('qwerty')

print(myset1 == myset2)
выведет:

True
'''

