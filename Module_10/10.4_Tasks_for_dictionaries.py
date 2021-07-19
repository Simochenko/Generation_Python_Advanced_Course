'''Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово
(или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.

Sample Input 1:

thing
night
Sample Output 1:

YES
Sample Input 2:

cat
rat
Sample Output 2:

NO
Sample Input 3:

tea
eat
Sample Output 3:

YES'''

# a=input()
# b=input()
#
# def anagram(a,b):
#     arra=split(a)
#     arrb=split(b)
#     arra.sort()
#     arrb.sort()
#     if (len(arra)==len(arrb)):
#
#             if(arra==arrb):
#                 print ("YES")
#             else:
#                 ana=0
#                 print ("NO")
#
#     else:
#         print ("NO")
#
#
# def split(x):
#     x=x.replace(' ','').lower()
#     temp=[]
#     for i in x:
#         temp.append(i)
#     return temp
#
# anagram(a,b)


# dict1, dict2 = {}, {}
# for i in input():
#     dict1[i] = dict1.setdefault(i, 0) + 1
# for i in input():
#     dict2[i] = dict2.setdefault(i, 0) + 1
# print('YES' if dict1 == dict2 else 'NO')



# d1 = {}
# d2 = {}
# for c in input():
#     d1[c] = d1.get(c, 0) + 1
# for c in input():
#     d2[c] = d2.get(c, 0) + 1
# print(['NO', 'YES'][d1 == d2])


# s1=input()
# s2=input()
# print('YES' if {x:s1.count(x) for x in s1}=={x:s2.count(x) for x in s2} else 'NO')



# string1, string2 = input(), input()
# word1 = {i: string1.count(i) for i in string1}
# word2 = {i: string2.count(i) for i in string2}
# print('YES' if word1 == word2 else 'NO')


# dcts = ({}, {})
# for d in dcts:
#     for c in input().lower():
#         d[c] = d.get(c, 0) + 1
#
# print(('NO', 'YES')[dcts[0] == dcts[1]])


# print('YES' if sorted(input()) == sorted(input()) else 'NO')


# print('YES' if sum([ord(i) for i in input()]) == sum([ord(i) for i in input()]) else 'NO')

'''Анаграммы 2
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. 
Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

Формат входных данных
На вход программе подаются два предложения, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.

Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.

Sample Input:

Вижу зверей
Живу резвей
Sample Output:

YES'''


# a=input()
# b=input()
#
# def anagram(a,b):
#     arra=split(a)
#     arrb=split(b)
#     arra.sort()
#     arrb.sort()
#     if (len(arra)==len(arrb)):
#
#             if(arra==arrb):
#                 print ("YES")
#             else:
#                 ana=0
#                 print ("NO")
#     else:
#         print ("NO")
#
#
# def split(x):
#     x=x.replace(' ','').lower()
#     for c in '.,!?:;-':
#         x = x.replace(c, '')
#
#
#     temp=[]
#     for i in x:
#         temp.append(i)
#     return temp
#
#
# anagram(a,b)


# a, b = [sorted([i for i in input().lower() if i.isalpha()]) for _ in "ab"]
# print(["NO", "YES"][a == b])


# d1, d2 = {}, {}
# for c in input():
#     if c not in '.,!?:;- ':
#         d1[c.lower()] = d1.get(c, 0) + 1
# for c in input():
#     if c not in '.,!?:;- ':
#         d2[c.lower()] = d2.get(c, 0) + 1
# print('YES' if d1 == d2 else 'NO')


# {print(('NO', 'YES')[a == o]) for o, a in [({c: s.count(c) for c in s if c.isalpha()} for _ in 'oa' for s in [input().lower()])]}


# sentences = [
#     sorted(x for x in input().lower() if x not in ' .,!?:;-')
#     for _ in range(2)
# ]
#
# print('YES' if sentences[0] == sentences[1] else 'NO')


# l = {}
# for ch in input().lower():
#     if ch in l:
#         l[ch] += 1
#     else:
#         l[ch] = 1
# for ch in input().lower():
#     if ch in l:
#         l[ch] += -1
#     else:
#         l[ch] = 1
# for ch in '.,!?:;- ':
#     l.pop(ch, None)
# print("YES" if min(l.values()) == 0 and max(l.values()) == 0 else "NO")

'''Словарь синонимов
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для 
одного данного слова определяет его синоним.

Формат входных данных
На вход программе подается количество пар синонимов nn. Далее следует nn строк, каждая строка содержит два 
слова-синонима. После этого следует одно слово, синоним которого надо найти.

Формат выходных данных
Программа должна вывести одно слово, синоним введенного.

Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.

Примечание 2. Все слова в словаре начинаются с заглавной буквы.

Sample Input 1:

4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty
Sample Output 1:

Beautiful
Sample Input 2:

3
Kind Affable
Intellect Mind
Popular Celebrated
Popular
Sample Output 2:

Celebrated'''

# n = int(input())
# p = dict(input().split() for j in range(n))
# k = input()
# for key, value in p.items():
#     if k == value:
#         print(key)
#     if k == key:
#         print(value)

# words = {}
# for _ in range(int(input())):
#     a, b = input().split()
#     words[a], words[b] = b, a
# print(words[input()])

# print({w[i]: w[not i] for _ in range(int(input())) for w in [input().split()] for i in (0, 1)}[input()])


# d = {i[0]: i[1] for i in [input().split() for _ in range(int(input()))]}
# word = input()
# for key, value in d.items():
#     if value == word:
#         print(key)
#     elif key == word:
#         print(value)

# d = dict((input().split() for i in range(int(input()))))
# ad = {v: k for k, v in d.items()}
# key = input()
# print(ad.get(key, d.get(key)))


'''Страны и города
На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу,
 которая для каждого города выводит, в какой стране он находится.

Формат входных данных
Программа получает на вход количество стран nn. Далее идет nn строк, каждая строка начинается с названия страны, 
затем идут названия городов этой страны. В следующей строке записано число mm, далее идут mm запросов — названия 
каких-то mm городов, из перечисленных выше.

Формат выходных данных
Программа должна вывести название страны, в которой находится данный город в соответствии с примером.

Sample Input:

2
Германия Берлин Мюнхен Гамбург Дортмунд
Нидерланды Амстердам Гаага Роттердам Алкмар
4
Амстердам
Алкмар
Гамбург
Гаага
Sample Output:

Нидерланды
Нидерланды
Германия
Нидерланды'''

# d = {}
# for i in range(int(input())):
#     country, *city = input().split()
#     d[country] = city
# list2 = []
# for j in range(int(input())):
#     city = input()
#     list2.append(city)
#     for key, value in d.items():
#         if list2[j] in value:
#             print(key)


# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     for c in cities:
#         d[c] = country
# for _ in range(int(input())):
#     print(d[input()])


# dct = {}
# for _ in range(int(input())):
#     a, *b = input().split()
#     dct.update(dict.fromkeys(b, a))
# for _ in range(int(input())):
#     print(dct[input()])



# d={}
# for _ in range(int(input())):
#     a=input().split()
#     for c in a[1:]:
#         d[c]=a[0]
# for _ in range(int(input())):
#     print(d[input()])


# d = {}
# for _ in range(int(input())):
#     a = input().split(' ', 1)
#
#     for i in range(len(a[1].split())):
#         d[a[1].split()[i]] = d.get(a[1].split()[i], a[0])
#
# for _ in range(int(input())):
#     print(d[input()])

'''Словарь программиста
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. 
Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу
 создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из 
 этого словаря.

Формат входных данных
В первой строке задано одно целое число nn — количество слов в словаре. В следующих nn строках записаны слова и их 
определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число mm — количество 
поисковых слов, чье определение нужно вывести. В следующих mm строках записаны сами слова, по одному на строке.

Формат выходных данных
Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его 
определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.

Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут.

Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (:), следом за которым идёт 
пробел.

Sample Input 1:

5
Змея: язык программирования Python
Баг: от англ. bug — жучок, клоп, ошибка в программе
Конфа: конференция
Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
Бета: бета-версия, приложение на стадии публичного тестирования
3
Змея
Жаба
костыль
Sample Output 1:

язык программирования Python
Не найдено
код, который нужен, чтобы исправить несовершенство ранее написанного кода
Sample Input 2:

7
Бэкенд: программно-аппаратная или серверная часть приложения
Бэкап: резервная копия или процесс создания резервной копии приложения
Галера: компания, в которой платят низкие зарплаты и не ценят разработчиков
Гит: система контроля версий Git или сервис GitHub
Г****окод: плохой, некачественный код
Жаба: язык программирования Java
Жабаскрипт: язык программирования JavaScript
6
Жаба
Змея
Костыль
Бета
БЭКЕНД
Г****окод
Sample Output 2:

язык программирования Java
Не найдено
Не найдено
Не найдено
программно-аппаратная или серверная часть приложения
плохой, некачественный код'''

# vocab = {key.lower(): value for key, value in [input().split(': ') for _ in range(int(input()))]}
# print(*[vocab.get(key.lower(), 'Не найдено') for key in [input() for _ in range(int(input()))]], sep='\n')

# prog = {}
# for _ in range(int(input())):
#     descr = input().split(': ')
#     prog[descr[0].lower()] = descr[1]
# for _ in range(int(input())):
#     print(prog.get(input().lower(), 'Не найдено'))

# [print(d.get(input().lower(), 'Не найдено')) for d in [{s[0].lower(): s[1] for _ in range(int(input())) for s in [input().split(': ')]}] for _ in range(int(input()))]


# d = {k.lower(): v for _ in range(int(input())) for k, v in [input().split(': ', 1)]}
# print(*(d.get(input().lower(), 'Не найдено') for _ in range(int(input()))), sep='\n')


# result = {}
# for _ in range(int(input())):
#     m = [i for i in input().split(': ')]
#     result[m[0].lower()] = result.get(m[0].lower(),'') + m[1]
# for _ in range(int(input())):
#     print(result.get(input().lower(),'Не найдено'))


# lst = [input().split(':') for _ in range(int(input()))]
# d = {i[0].lower(): i[1] for i in lst}
# s = [input().lower() for i in range(int(input()))]
# [print('Не найдено') if i not in d else print(d[i].strip()) for i in s ]

# word={}
# for i in range(int(input())):
#     l=input().split(': ')
#     word[l[0].lower()]=l[1]
# m=int(input())
# s=[input().lower() for i in range(m)]
# for c in s:
#     if c in word:
#         print(word[c])
#     else:
#         print('Не найдено')


'''Телефонная книга
Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру 
находить все номера определённого друга.

Формат входных данных
В первой строке задано одно целое число nn — количество номеров телефонов, информацию о которых Тимур сохранил в 
телефонной книге. В следующих nn строках заданы телефоны и имена их владельцев через пробел. В следующей строке 
записано целое число mm — количество поисковых запросов от Тимура. В следующих mm строках записаны сами запросы, по 
одному на строке. Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти.

Формат выходных данных
Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем. Если в 
телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «абонент не найден» 
(без кавычек).

Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во 
входных данных.

Примечание 2. Количество строк в ответе должно быть равно числу mm.

Примечание 3. Телефон — это несколько цифр, записанных подряд, а имя может состоять из букв русского или английского
 алфавита. Записи не повторяются.

Sample Input:

3
79184219577 Женя
79194249271 Руслан
79281234567 Женя
3
Руслан
Женя
Рустам
Sample Output:

79194249271
79184219577 79281234567
абонент не найден'''


# dict = {}
# for i in range(int(input())):
#     value, key = input().split()
#     if key in dict:
#         dict[key].append(value)
#     else:
#         dict[key] = [value]
#
# for i in range(int(input())):
#     key = input()
#     if key in dict:
#         print(*dict[key])
#     else:
#         print('абонент не найден')

# book = {}
# for _ in range(int(input())):
#     line = input().split()
#     if line[1] not in book:
#         book[line[1]] = [line[0]]
#     else:
#         book[line[1]].append(line[0])
# for _ in range(int(input())):
#     print(*book.get(input(), (['абонент не найден'])))


# d = {}
# for _ in range(int(input())):
#     a = input().split()
#     d[a[1]] = d.get(a[1], []) + [a[0]]
# for _ in range(int(input())):
#     print(*d.get(input(), ['абонент не найден']))

d = {}
for i in [input().split() for _ in range(int(input()))]:
    d.setdefault(i[1], []).append(i[0])
for key in [input() for _ in range(int(input()))]:
    print(*d[key] if key in d else ['абонент не найден'])