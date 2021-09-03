# with open('words.txt', 'w') as file:
#     file.write('delphi+')
#     file.write('java')


# with open('names.txt', 'a') as file:
#     file.write('\n')
#     file.write('Michael\n')
#     file.write('Alexander')

# with open('artists.txt', 'r+') as file:
#     file.write('Mick Jagger\n')
#     file.write('Ace Canon\n')

# with open('words.txt', 'w') as output:
#     print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
#     print('python', file=output)

# with open('beegeek.txt', 'w') as file:
#     file.writelines(['Добро пожаловать в Beegeek!\n', 'Наши курсы самые лучшие! '])
#     file.write('Позвоните нам: (916) 928-92xx')


'''Суммарная стоимость
Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц. На каждой строке файла указано, сколько
 клиент заплатил за товар, в долларах (целое число):

$47
$100
$60
$12
$8
...
Напишите программу для подсчета суммарной месячной выручки фирмы.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести выручку фирмы (сумму всех чисел из файла) в соответствии с примером ниже.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Если бы файл ledger.txt содержал строки:

$37
$44
$19
то результатом будет:

$100
Примечание 3. Указанный файл можно скачать по ссылке.'''

# with open('ledger.txt', 'r') as file:
#     content = [int(line.replace('$', '').strip()) for line in file.readlines()]
#     print(f'${sum(content)}')

# with open('ledger.txt') as f:
#     print(f'${sum([int(i.strip()[1:]) for i in f.readlines()])}')

# with open('ledger.txt') as inp:
#     print('${}'.format(sum(map(lambda x: int(x[1::]), inp))))


# with open('ledger.txt') as ledger:
#     result = sum(map(lambda x: int(x.strip('$')), ledger.readlines()))
#     print('$', result, sep='')
#

'''Goooood students
Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров. Строки файла
 имеют вид: фамилия оценка_1 оценка_2 оценка_3.

Напишите программу для подсчета количества студентов, сдавших все три теста. Тест считается сданным, если количество 
баллов по нему не меньше 6565.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести количество студентов, сдавших все три теста.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Если бы файл grades.txt содержал строки:

Washington 83 77 54
Adams 86 69 90
Jacobson 50 49 71
MacDonald 100 99 100
Berrington 66 67 64
то результатом будет:

2'''

# with open('grades.txt', 'r', encoding='utf-8') as file:
#     content = [[el.strip() for el in line.split()] for line in file.readlines()]
#     count = 0
#     for line in content:
#         if all([bool(int(el) >= 65) for el in line[1:]]):
#             count += 1
#     print(count)

# with open('grades.txt') as f:
#     print(sum(1 for i in f.readlines() if all([int(j) >= 65 for j in i.split(' ')[1:]])))


# def is_good_student(name_and_grades):
#     return all(map(lambda grade: int(grade) > 64, name_and_grades.split()[1:]))
#
# with open('grades.txt') as grades:
#     result = sum(map(is_good_student, grades.readlines()))
#     print(result)

'''Самое длиное слово в файле
Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу, которая находит и 
выводит самые длинные слова этого файла, не меняя порядка их следования.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести самые длинные слова файла words.txt, каждое с новой строки, не меняя их порядка следования.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Словом считайте любую группу символов без пробелов, даже если она включает цифры или знаки препинания.

Примечание 3. Если бы файл words.txt содержал строки:

there are many different holidays on the first of january we celebrate new year on the seventh of january and the
 twenty-fifth of december we have christmas the twenty-third of february is the day of the defenders of the
  motherland or the army day then comes easter and radonitsa the first of may is the labour day the ninth of may 
  is victory day the third of july is independence day then comes the seventh of november the day of the october 
  revolution and so on
то результатом будет:

twenty-fifth
twenty-third
independence'''

# with open('words.txt', 'r', encoding='utf-8') as file:
#     content = [word for word in file.read().split()]
#     max_len = len(max(content, key=len))
#     print(*filter(lambda x: len(x) == max_len, content), sep='\n')


# with open('words.txt') as f:
#     max_len, max_words = 0, []
#     for word in f.read().split():
#         if len(word) > max_len:
#             max_len, max_words = len(word), [word]
#         elif len(word) == max_len:
#             max_words.append(word)
#
#     print(*max_words, sep='\n')

# with open('words.txt') as f:
#     mylist = f.read().split()
#     longest = max(map(len, mylist))
#     print(*list(filter(lambda x: len(x) == longest, mylist)), sep='\n')
#

'''Tail of a File
На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран последние 
10 строк данного файла.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести последние 1010 строк этого файла.

Примечание 1. Считайте, что исполняемая программа и файл находятся в одной папке.

Примечание 2. Если количество строк в файле меньше 1010, необходимо вывести содержимое файла полностью.

Примечание 3. Если бы файл содержал строки:

there are many different holidays
on the first of january we
celebrate new year on the
seventh of january and the
twenty-fifth of december we
have christmas the twenty-third
of february is the day of the
defenders of the motherland
or the army day then comes
easter and radonitsa the
first of may is the labour
day the ninth of may is
victory day the third of july
is independence day then comes
the seventh of november the day
of the october revolution and so on
то результатом будет:

of february is the day of the
defenders of the motherland
or the army day then comes
easter and radonitsa the
first of may is the labour
day the ninth of may is
victory day the third of july
is independence day then comes
the seventh of november the day
of the october revolution and so on
Примечание 4. Подумайте над ситуацией, когда файл очень большой и нерационально считывать все его содержимое в 
память компьютера.'''

# with open(input(), 'r', encoding='utf-8') as file:
#     content = [line.strip() for line in file.readlines()]
#     if len(content) <= 10:
#         print(*content, sep='\n')
#     else:
#         print(*content[-10:], sep='\n')

# with open(input()) as file:
#     print(*file.readlines()[-10:], sep='')

# with open(input()) as file:
#     txt = []
#     for line in file:
#         txt += [line.strip()]
#         if len(txt) > 10:
#             del txt[0]
#     print(*txt, sep='\n')

'''Forbidden words ??
На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран содержимое 
этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).

Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что
 все слова в этом файле записаны в нижнем регистре.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, в котором необходимо заменить 
запрещенные слова звездочками.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались, даже если они встречаются 
в середине другого слова.

Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра. Например, если файл 
forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и подобные должны быть
 заменены на ****.

Примечание 3. Если бы файл forbidden_words.txt содержал слова:

hello email python the exam wor is
а файл в котором заменяются слова имел бы вид:

Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!
то результатом будет:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!
Примечание 4. Файл forbidden_words.txt можно скачать по ссылке. Ваша программа прогоняется на трех файлах 
data.txt, stepik.txt и beegeek.txt.'''

# with open("forbidden_words.txt", encoding="utf-8") as file, open(input()) as infile:
#     text = infile.read()
#     for f in file.read().strip("\n").split():
#         pos = text.lower().find(f)
#         while pos > -1:
#             text = text[:pos] + "*" * len(f) + text[pos+len(f):]
#             pos = text.lower().find(f)
# print(text)


# with open('forbidden_words.txt') as f:
#     forbidden_words = {word: '*' * len(word) for word in f.read().split()}
# with open(input()) as f:
#     s = f.read()
#     s_lower = s.lower()
# for forbidden_word in forbidden_words:
#     s_lower = s_lower.replace(forbidden_word, forbidden_words[forbidden_word])
# print(*map((lambda c1, c2: '*' if c2 == '*' else c1), s, s_lower), sep='')

# with open('forbidden_words.txt') as file_pattern, open(input()) as file_in:
#     pattern, text = file_pattern.read().split(), file_in.read()
#
# text_lower = text.lower()
# for word in pattern:
#     text_lower = text_lower.replace(word, '*' * len(word))
#
# result = ''.join((y, x)[x == '*'] for x, y in zip(text_lower, text))
# print(result)

'''Транслитерация ??
Транслитерация — передача знаков одной письменности знаками другой письменности, при которой каждый знак (или последовательность знаков) одной системы письма передаётся соответствующим знаком (или последовательностью знаков) другой системы письма.

Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для транслитерации этого файла, то есть замены кириллических символов на латинские в соответствии с предложенной таблицей. Все остальные символы надо оставить без изменений. Результат транслитерации требуется записать в файл transliteration.txt.

Кириллица 	Латиница	Кириллица	Латиница	Кириллица	Латиница
а	a	к	k	х	h
б	b	л	l	ц	c
в	v	м	m	ч	ch
г	g	н	n	ш	sh
д	d	о	o	щ	shh
е	e	п	p	ъ	*
ё	jo	р	r	ы	y
ж	zh	с	s	ь	'
з	z	т	t	э	je
и	i	у	u	ю	ju
й	j	ф	f	я	ya
Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем transliteration.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Обратите внимание, что заглавные буквы должны заменяться на соответствующие им заглавные же буквы, 
но если транслитерационная последовательность состоит из нескольких символов, то заглавным будет только первый из
 них: «С» на «S», а «Я» на «Ya».

Примечание 3. Если бы файл cyrillic.txt содержал текст:

Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to
 help him: they don’t want the truth to be exposed.
то содержимое файла transliteration.txt будет:

Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to 
help him: they don’t want the truth to be exposed.
Примечание 4. Указанный файл можно скачать по ссылке.'''

# d = { 'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n',
# 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh',
# 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
# 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N',
# 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh',
# 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya' }
#
# with open('cyrillic.txt', 'r', encoding='utf-8') as file1, open('transliteration.txt', 'w', encoding='utf-8')
# as file2:
#     content = file1.read()
#     for char in content:
#         if char in d:
#             file2.write(d[char])
#         else:
#             file2.write(char)

# d = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
#     }
# with open('cyrillic.txt', encoding='utf-8') as f_input, open('transliteration.txt', 'w') as f_output:
#     f_output.write(''.join(i if i.lower() not in d else d[i] if i.islower() else d[i.lower()].title() for i in f_input.read()))


# trn, text = dict(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', "a b v g d e jo zh z i j k l m n o p r s t u f h c ch sh shh * y ' je ju ya".split())), open('cyrillic.txt').read()
# for s in text:
#     if s.lower() in trn:
#         text = text.replace(s, [trn[s.lower()], trn[s.lower()].title()][s.isupper()])
# print(text, file=open('transliteration.txt', 'w'))

'''Пропущенные комменты ??
При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и возвращаемое
 значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе забывают о них ?.

На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите 
программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать, что
 любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит
  комментарий, если первый символ предыдущей строки - #.


Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.

Формат выходных данных
Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле), каждое на отдельной 
строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют поясняющий комментарий, 
то следует вывести: Best Programming Team.

Примечание 1. Если бы файл содержал код:

def powers(a):
    return a, a**2, a**3

# функция вычисляет сумму всех переданных чисел
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# функция возвращает количество переданных аргументов
def count_args(*args):
    return len(args)

def mean(*args):
    total = 0.0
    count = 0  
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count

def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# функция вычисляет факториал переданного числа
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
то результатом будет:

powers
matrix
mean
greet
Примечание 2. Гарантируется, что в файле есть хотя бы одна функция при этом вложенных функций в файле нет. '''

# with open(input(), 'r') as file:
#     content = file.readlines()
#     without_name = []
#     for i in range(len(content)):
#         if content[i].startswith('def'):
#             if content[i - 1].startswith('#'):
#                 continue
#             else:
#                 without_name.append(content[i][4: content[i].index('(')])
#     if without_name:
#         print(*without_name, sep='\n')
#     else:
#         print('Best Programming Team')

# with open(input(), encoding='utf-8') as inf:
# 	not_commented_funcs, preline = [], ''
# 	for line in inf:
# 		if not preline.startswith('#') and line.startswith('def '):
# 			not_commented_funcs.append(line[4:line.find('(')])
# 		preline = line
# 	print('\n'.join(not_commented_funcs) if not_commented_funcs else 'Best Programming Team')


# s = ''
#
# with open(input()) as fin:
#     t = fin.readlines()
#     for i, row in enumerate(t):
#         if row[:4] == 'def ' and (i == 0 or t[i - 1][0] != '#'):
#             c = row.find('(')
#             s = s + row[4:c] + '\n'
#     print(s[:-1] if s else 'Best Programming Team')


'''Количество строк в файле
На вход программе подается строка текста с именем текстового файла. Напишите программу для вывода на экран
 количества строк данного файла.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла.

Формат выходных данных
Программа должна вывести количество строк файла.

Примечание. Считайте, что исполняемая программа и указанный файл находятся в одной папке.'''

# with open('prices.txt') as f:
#    count = sum(1 for _ in f)
# print(count)


# with open(input(),encoding = "utf-8") as file:
#     sp = file.readlines()
#     print(len(sp))

# with open(f'{input()}') as f:
#     print(len(list(f)))

# print(len(open(input()).readlines()))