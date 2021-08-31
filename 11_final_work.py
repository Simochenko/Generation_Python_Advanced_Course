'''Ключом в словаре не может быть'''

# list
# set

'''Выберите верные утверждения:'''


# словари могут содержать словари в качестве значений элементов
# все ключи в словаре должны быть уникальными
# доступ к элементам словаря осуществляется по их ключам
# словари изменяемы

'''Выберите все способы создания словаря'''

# d = {}
# d['foo'] = 100
# d['bar'] = 200
# d['baz'] = 300
#
# d = dict(foo=100, bar=200, baz=300)
#
# d = {'foo': 100, 'bar': 200, 'baz': 300}
#
# d = dict([('foo', 100), ('bar', 200), ('baz', 300)])


'''Выберите способ, позволяющий получить значение 3030 из списка data:

data = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]'''


# data[2]['bar']['z']

'''Что будет выведено в результате выполнения следующего программного кода?

d = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]

print('z' in d[2])'''

# False

'''Какая функция определяет количество элементов, которые хранятся в словаре?'''

# len()

'''Что покажет приведенный ниже фрагмент кода?

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153,
              'Scripps': 131,
              'Social Sciences': 2870}

print(len(recipients))'''

# 7

'''Выберите все способы, с помощью которых можно получить значение по ключу marks:

student = {'name': 'Emma', 'class': 9, 'marks': 75}'''


# student['marks']
#
# student.get('marks')

'''Что покажет приведенный ниже фрагмент кода?

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153,
              'Scripps': 131,
              'Social Sciences': 2870}

print(recipients['Math'])'''

# произойдет ошибка (KeyError) во время выполнения программы

'''Что покажет приведенный ниже фрагмент кода?

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153,
              'Scripps': 131,
              'Social Sciences': 2870}

print(recipients.get('Math'))'''

# None

'''Выберите все способы, с помощью которых можно удалить из словаря элемент с ключом, равным class:

student = {'name': 'Emma', 'class': 9, 'marks': 75}'''

# student.pop('class')

# del student['class']

'''Что нужно вставить вместо ..., чтобы результатом работы кода:

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153,
              'Scripps': 131,
              'Social Sciences': 2870}

for i in ...:
    print(i)
было:

409
1473
1343
1131
153
131
2870'''


# recipients.values()

'''Словарь recipients имеет вид:

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153}
Какая из приведенных ниже строк кода модифицирует словарь к виду

recipients = {'Humanities': 409,
              'Biology': 1473,
              'Engineering': 1343,
              'Physical Sciences': 1131,
              'Medicine': 153,
              'Scripps': 131,
              'Math': 3456}'''


# recipients.update({'Scripps': 131, 'Math': 3456})
#
# recipients.update([('Scripps', 131), ('Math', 3456)])


# Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену. Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке, в формате username@domain.
#
# Примечание. Для сортировки в алфавитном порядке используйте встроенную функцию sorted(), либо списочный метод sort().

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# items = []
# for key, value in emails.items():
#     for el in value:
#         items.append(el + '@' + key)
# print(*sorted(items), sep='\n')

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
# print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# print('\n'.join(sorted(f'{x}@{k}' for k, v in emails.items() for x in v)))


# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# p = []
# for i, j in emails.items():
#     for jj in j:
#         p.append(jj+'@'+i)
# print(*sorted(p), sep='\n')

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# emails_list = []
# for email in emails:
#     for name in emails[email]:
#         emails_list.append(name + '@' + email)
# print(*sorted(emails_list), sep='\n')


'''Минутка генетики
Как известно из курса биологии ДНК и РНК – последовательности нуклеотидов.

Четыре нуклеотида в ДНК:

аденин (A);
цитозин (C);
гуанин (G);
тимин (T).
Четыре нуклеотида в РНК:

аденин (A);
цитозин (C);
гуанин (G);
урацил (U).
Цепь РНК строится на основе цепи ДНК последовательным присоединением комплементарных нуклеотидов:

G \rightarrow→ C;
C \rightarrow→ G;
T \rightarrow→ A;
A \rightarrow→ U.
Напишите программу, переводящую цепь ДНК в цепь РНК.

Формат входных данных
На вход программе подается корректная цепь ДНК в верхнем регистре.

Формат выходных данных
Программа должна вывести соответствующую цепь РНК в верхнем регистре.

Примечание. Подробнее прочитать про ДНК и РНК можно тут и тут.

Sample Input 1:

ACTG
Sample Output 1:

UGAC
Sample Input 2:

CC
Sample Output 2:

GG
Sample Input 3:

GTA
Sample Output 3:

CAU'''
# def compliment(Nucleotide):
#     comp = []
#     for i in Nucleotide:
#         if i == "T":
#             comp.append("A")
#         if i == "A":
#             comp.append("U")
#         if i == "G":
#             comp.append("C")
#         if i == "C":
#             comp.append("G")
#
#     return ''.join(comp)
#
# print(compliment(input()))


# d = str.maketrans({'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'})
# s = input()
# print(s.translate(d))

# d = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
# print(''.join(d[c] for c in input()))

# DNA_dict = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# print(''.join([DNA_dict[i] for i in input()]))

# rnk={'A': 'U' ,'C': 'G' ,'G': 'C','T': 'A'}
# dnk=input()
# for elem in dnk:
# 	print(rnk[elem],end='')
#
# r_d={'G':'C',
#      'C':'G',
#      'T':'A',
#      'A':'U'}
# print(*(r_d[i] for i in input()), sep='')

'''Порядковый номер
Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв, слова разделены одним пробелом или несколькими.

Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с учетом регистра. Для первого вхождения слова программа выведет 11, для второго вхождения того же слова — 22 и т. д.

Формат входных данных
Программа получает на вход единственную строку текста, состоящую только из русских букв и символов пробела. 

Формат выходных данных
Для каждого слова исходного текста программа выводит одно целое число — номер вхождения этого слова в текст. Числа необходимо выводятся на одной строке, через пробел.

Примечание. Количество чисел должно совпадать с количеством слов исходного текста.

Sample Input 1:

прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
Sample Output 1:

1 1 2 1 1 2 1 2 3 1
Sample Input 2:

Привет что делаешь что нового что с работой как там с деньгами
Sample Output 2:

1 1 1 2 1 3 1 1 1 1 2 1'''

# def coun(x):
#     dct[x] = dct.get(x, 0) + 1
#     return dct[x]
#
# dct = {}
# print(*[coun(k) for k in input().split()])

# s = input().split()
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
#     print(d[i], end = ' ')

# d = {}
# for i in input().split():
#     d[i] = d.get(i, 0) + 1
#     print(d[i], end=' ')

'''Scrabble game
В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв. Чем реже буква встречается, тем больше она ценится:

Баллы	Буква
11	AA, EE, II, LL, NN, OO, RR, SS, TT, UU
22	DD, GG
33	BB, CC, MM, PP
44	FF, HH, VV, WW, YY
55	KK
88	JJ, XX
1010	QQ, ZZ
Напишите программу подсчета итоговой стоимости введенного слова.

Формат входных данных
На вход программе подается одно слово в верхнем регистре на английском языке.

Формат выходных данных
Программа должна вывести суммарную стоимость букв введеного слова.

Примечание. Подробнее про игру можно почитать тут.

Sample Input 1:

DANSER
Sample Output 1:

7
Sample Input 2:

FRESHENER
Sample Output 2:

15
Sample Input 3:

ZIP
Sample Output 3:

14'''

# def count_letters(word):
#   count = {}
#   for letter in word:
#     if letter not in count: count[letter] = 0
#     count[letter] += 1
#   return count
#
#
#
# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
#
# def score_word(word):
#   return sum([score[c] for c in word])
#
# print(score_word(input().lower()))

# letters = {1:	'AEILNORSTU', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10:'QZ'}
# scores = {letter: score for score in letters for letter in letters[score]}
# print(sum(scores[l] for l in input()))


#
# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
#
# print(sum([k for i in input() for k, v in d.items() if i in v]))

# print(sum(val for s in input() for key, val in {'AEILNORSTU': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}.items() if s in key))

# d = {
#     "AEILNORSTU": 1,
#     "DG": 2,
#     "BCMP": 3,
#     "FHVWY": 4,
#     "K": 5,
#     "JX": 8,
#     "QZ": 10
# }
# answer = 0
# for ch in input():
#     for key in d:
#         if ch in key:
#             answer += d[key]
#             break
# print(answer)

'''Слияние словарей
Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей переданного списка.

Примечание 1. Следующий программный код:

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
создает словарь:

result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
Примечание 2. Вызывать функцию merge() не нужно, требуется только реализовать. 

Примечание 3. Слияние пустых словарей должно быть пустым словарем.'''

# def merge(values):      # values - это список словарей
#     result = {}
#     for dct in values:
#         for key in dct.keys():
#             if key not in result:
#                 result[key] = {dct[key]}
#             else:
#                 result[key].add(dct[key])
#     return result

# def merge(values):
#     res = {}
#     for d in values:
#         for k, v in d.items():
#             res.setdefault(k, set()).add(v)
#     return res

# def merge(values):
#     res = {}
#     for d in values:
#         for k, v in d.items():
#             res.setdefault(k, set()).add(v)
#     return res

# def merge(values):      # values - это список словарей
#     res = {}
#     for d in values:
#         for k, v in d.items():
#             res[k] = res.get(k, set([v]))
#             res[k].add(v)
#     return res


# def merge(values):      # values - это список словарей
#     result = {}
#     for i in values:
#         for j in i:
#             result[j] = result.get(j, set())
#             result[j].add(i[j])
#     return result

# def merge(values):      # values - это список словарей
#     return {key: {d.get(key) for d in values} - {None} for key in set(i for d in values for i in d)}


'''Опасный вирус 😈
В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал 
контроль прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).
Напишите программу для восстановления контроля прав доступа к файлам. Ваша программа для каждого запроса должна 
будет возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.

Формат входных данных
Программа получает на вход количество файлов nn, содержащихся в файловой системе компьютера. Далее идет nn строк, 
на каждой имя файла и допустимые с ним операции, разделенные символом пробела. В следующей строке записано число 
mm — количество запросов к файлам, и затем mm строк с запросами вида операция файл. Одному и тому же файлу может 
быть адресовано любое количество запросов.

Формат выходных данных
Программа должна вывести для каждого из mm запросов в отдельной строке Access denied или OK.

Sample Input:

5
my_pycode.exe W X
log_n X W R
ave R
lucky_m W R
dnsss.py W
6
execute ave
read dnsss.py
write log_n
execute log_n
read ave
write my_pycode.exe
Sample Output:

Access denied
Access denied
OK
OK
OK
OK'''

# ACTION_PERMISSION = {
#     'read': 'R',
#     'write': 'W',
#     'execute': 'X',
# }
#
# file_permissions = {}
# for i in range(int(input())):
#     file, *permissions = input().split()
#     file_permissions[file] = set(permissions)
#
# for i in range(int(input())):
#     action, file = input().split()
#     if ACTION_PERMISSION[action] in file_permissions[file]:
#         print('OK')
#     else:
#         print('Access denied')

# r = {}
# z = {'W': 'write', 'R': 'read', 'X': 'execute'}
# for i in range(int(input())):
#     x = input().split()
#     r[x[0]] = [z[i] for i in x[1:]]
# for i in range(int(input())):
#     a, b = input().split()
#     print(('Access denied', 'OK')[a in r[b]])


'''Покупки в интернет-магазине 🌶️
Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.

Формат входных данных
На вход программе подается число nn — количество строк в базе данных о продажах интернет-магазина. Далее следует nn 
строк с записями вида покупатель товар количество, где покупатель — имя покупателя (строка без пробелов), товар —
 название товара (строка без пробелов), количество — количество приобретенных единиц товара (натуральное число).

Формат выходных данных
Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого покупателя —
 двоеточие, затем список названий всех приобретенных им товаров в лексикографическом порядке, после названия каждого
  товара — количество единиц товара. Информация о каждом товаре выводится на отдельной строке.

Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает суммарное
 количество товара по данной позиции.

Sample Input 1:

5
Руслан Пирог 1
Тимур Карандаш 5
Руслан Линейка 2
Тимур Тетрадь 12
Руслан Хлеб 3
Sample Output 1:

Руслан:
Линейка 2
Пирог 1
Хлеб 3
Тимур:
Карандаш 5
Тетрадь 12
Sample Input 2:

7
Вячеслав Ручка 1
Филип Ручка 1
Виктория Перо 3
Вячеслав Линейка 4
Виктория Тетрадь 7
Вячеслав Ручка 29
Филип Циркуль 1
Sample Output 2:

Виктория:
Перо 3
Тетрадь 7
Вячеслав:
Линейка 4
Ручка 30
Филип:
Ручка 1
Циркуль 1
Sample Input 3:

5
Максим Пирог 5
Максим Печенье 55
Максим Свеча 3
Максим Тарелки 10
Максим Торт 1
Sample Output 3:

Максим:
Печенье 55
Пирог 5
Свеча 3
Тарелки 10
Торт 1'''

#
# customers = {}
#
# for line in  range(int(input())):
#     name, good, qty = input().strip().split()
#     if name not in customers:
#         customers[name] = {good: int(qty)}
#     elif good not in customers[name]:
#         customers[name].update({good: int(qty)})
#     else:
#         customers[name].update({good: customers[name].get(good) + int(qty)})
#
#
# for name in sorted(customers):
#     print(name + ':')
#     for good in sorted(customers[name]):
#         print(good, customers[name][good])


# data = {}
#
# for _ in range(int(input())):
#     name, item, count = input().split()
#     data.setdefault(name, {})
#     data[name][item] = data[name].get(item, 0) + int(count)
#
# for person, items in sorted(data.items()):
#     print(f'{person}:')
#     for item, count in sorted(items.items()):
#         print(item, count)


# d={}
# for _ in range(int(input())):
#     name, good, count=input().split()
#     d[name][good] = d.setdefault(name, {}).setdefault(good, 0) + int(count)
# for key in sorted(d):
#     print(f'{key}:')
#     for x in sorted(d[key].items()):
#         print(*x)

# inet, read= {}, __import__('sys').stdin
# for _ in range(int(read.readline())):
#     name, tov, n = read.readline().strip().split()
#     inet[name][tov] = inet.setdefault(name, {}).get(tov, 0) + int(n)
# for name in sorted(inet):
#     print(f'{name}:')
#     [print(t, n) for t, n in sorted(inet[name].items())]

# shopping_list = [input().split() for _ in range( int(input()))]
# shopping_dict = dict()
#
# # Собираем словарь
# for item in shopping_list:
#     name, kind, count = item
#     shopping_dict[name] = shopping_dict.get(name, {})
#     shopping_dict[name][kind] = shopping_dict[name].get(kind, 0) + int(count)
#
# # Выводим его в упорядоченном порядке
# for name in sorted(shopping_dict.keys()):
#     print(f"{name}:")
#     for kind in sorted(shopping_dict[name].keys()):
#         print(f"{kind} {shopping_dict[name][kind]}")

# Дополните приведенный код, чтобы в списках значений элементов словаря my_dict  не было чисел, больших 2020. При этом порядок оставшихся элементов меняться не должен.

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# my_dict = {k: [j for j in v if int(j) <= 20] for k, v in my_dict.items()}
# print(my_dict)


# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# for k in my_dict:
#     my_dict[k] = [x for x in my_dict[k] if not x > 20]


# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# my_dict = {x: [n for n in my_dict[x] if n<=20] for x in my_dict}

