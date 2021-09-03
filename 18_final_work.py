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
#     file.writelines(['����� ���������� � Beegeek!\n', '���� ����� ����� ������! '])
#     file.write('��������� ���: (916) 928-92xx')


'''��������� ���������
��� �������� ��������� ���� ledger.txt � ������� � �������� ����� �� �����. �� ������ ������ ����� �������, �������
 ������ �������� �� �����, � �������� (����� �����):

$47
$100
$60
$12
$8
...
�������� ��������� ��� �������� ��������� �������� ������� �����.

������ ������� ������
�� ���� ��������� ������ �� ��������.

������ �������� ������
��������� ������ ������� ������� ����� (����� ���� ����� �� �����) � ������������ � �������� ����.

���������� 1. ��������, ��� ����������� ��������� � ��������� ���� ��������� � ����� �����.

���������� 2. ���� �� ���� ledger.txt �������� ������:

$37
$44
$19
�� ����������� �����:

$100
���������� 3. ��������� ���� ����� ������� �� ������.'''

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
��� �������� ��������� ���� grades.txt, ���������� ������ �������� �� ��� ����� � ������ �� ����������. ������ �����
 ����� ���: ������� ������_1 ������_2 ������_3.

�������� ��������� ��� �������� ���������� ���������, ������� ��� ��� �����. ���� ��������� �������, ���� ���������� 
������ �� ���� �� ������ 6565.

������ ������� ������
�� ���� ��������� ������ �� ��������.

������ �������� ������
��������� ������ ������� ���������� ���������, ������� ��� ��� �����.

���������� 1. ��������, ��� ����������� ��������� � ��������� ���� ��������� � ����� �����.

���������� 2. ���� �� ���� grades.txt �������� ������:

Washington 83 77 54
Adams 86 69 90
Jacobson 50 49 71
MacDonald 100 99 100
Berrington 66 67 64
�� ����������� �����:

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

'''����� ������ ����� � �����
��� �������� ��������� ���� words.txt �� �������, ������������ ��������. �������� ���������, ������� ������� � 
������� ����� ������� ����� ����� �����, �� ����� ������� �� ����������.

������ ������� ������
�� ���� ��������� ������ �� ��������.

������ �������� ������
��������� ������ ������� ����� ������� ����� ����� words.txt, ������ � ����� ������, �� ����� �� ������� ����������.

���������� 1. ��������, ��� ����������� ��������� � ��������� ���� ��������� � ����� �����.

���������� 2. ������ �������� ����� ������ �������� ��� ��������, ���� ���� ��� �������� ����� ��� ����� ����������.

���������� 3. ���� �� ���� words.txt �������� ������:

there are many different holidays on the first of january we celebrate new year on the seventh of january and the
 twenty-fifth of december we have christmas the twenty-third of february is the day of the defenders of the
  motherland or the army day then comes easter and radonitsa the first of may is the labour day the ninth of may 
  is victory day the third of july is independence day then comes the seventh of november the day of the october 
  revolution and so on
�� ����������� �����:

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
�� ���� ��������� �������� ������ ������ � ������ ���������� �����. �������� ���������, ��������� �� ����� ��������� 
10 ����� ������� �����.

������ ������� ������
�� ���� ��������� �������� ������ ������ � ������ ������������� ���������� �����.

������ �������� ������
��������� ������ ������� ��������� 1010 ����� ����� �����.

���������� 1. ��������, ��� ����������� ��������� � ���� ��������� � ����� �����.

���������� 2. ���� ���������� ����� � ����� ������ 1010, ���������� ������� ���������� ����� ���������.

���������� 3. ���� �� ���� �������� ������:

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
�� ����������� �����:

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
���������� 4. ��������� ��� ���������, ����� ���� ����� ������� � ������������� ��������� ��� ��� ���������� � 
������ ����������.'''

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
�� ���� ��������� �������� ������ ������ � ������ ���������� �����. �������� ���������, ��������� �� ����� ���������� 
����� �����, �� � ������� ���� ����������� ���� ����������� * (���������� ��������� ����� ���������� ���� � �����).

����������� �����, ����������� �������� �������, �������� � ��������� ����� forbidden_words.txt. �������������, ���
 ��� ����� � ���� ����� �������� � ������ ��������.

������ ������� ������
�� ���� ��������� �������� ������ ������ � ������ ������������� ���������� �����, � ������� ���������� �������� 
����������� ����� �����������.

������ �������� ������
��������� ������ ������� ����� � ������������ � �������� ������.

���������� 1. ���� ��������� ������ �������� ����������� �����, ��� �� ��� �� �����������, ���� ���� ��� ����������� 
� �������� ������� �����.

���������� 2. ��������� ������ �������� ����������� ����� ���������� �� �� ��������. ��������, ���� ���� 
forbidden_words.txt �������� ����������� ����� exam, �� ����� exam, Exam, ExaM, EXAM � �������� ������ ����
 �������� �� ****.

���������� 3. ���� �� ���� forbidden_words.txt �������� �����:

hello email python the exam wor is
� ���� � ������� ���������� ����� ���� �� ���:

Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!
�� ����������� �����:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!
���������� 4. ���� forbidden_words.txt ����� ������� �� ������. ���� ��������� ����������� �� ���� ������ 
data.txt, stepik.txt � beegeek.txt.'''

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

'''�������������� ??
�������������� � �������� ������ ����� ������������ ������� ������ ������������, ��� ������� ������ ���� (��� ������������������ ������) ����� ������� ������ ��������� ��������������� ������ (��� ������������������� ������) ������ ������� ������.

��� �������� ��������� ���� cyrillic.txt, ���������� �����. �������� ��������� ��� �������������� ����� �����, �� ���� ������ ������������� �������� �� ��������� � ������������ � ������������ ��������. ��� ��������� ������� ���� �������� ��� ���������. ��������� �������������� ��������� �������� � ���� transliteration.txt.

��������� 	��������	���������	��������	���������	��������
�	a	�	k	�	h
�	b	�	l	�	c
�	v	�	m	�	ch
�	g	�	n	�	sh
�	d	�	o	�	shh
�	e	�	p	�	*
�	jo	�	r	�	y
�	zh	�	s	�	'
�	z	�	t	�	je
�	i	�	u	�	ju
�	j	�	f	�	ya
������ ������� ������
�� ���� ��������� ������ �� ��������.

������ �������� ������
��������� ������ ������� ���� � ������ transliteration.txt � ������������ � �������� ������.

���������� 1. ��������, ��� ����������� ��������� � ��������� ����� ��������� � ����� �����.

���������� 2. �������� ��������, ��� ��������� ����� ������ ���������� �� ��������������� �� ��������� �� �����, 
�� ���� ������������������ ������������������ ������� �� ���������� ��������, �� ��������� ����� ������ ������ ��
 ���: �ѻ �� �S�, � �߻ �� �Ya�.

���������� 3. ���� �� ���� cyrillic.txt �������� �����:

��������� ��� ������� ����� ��������� ����� �������� � ������������ ����.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to
 help him: they don�t want the truth to be exposed.
�� ���������� ����� transliteration.txt �����:

Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to 
help him: they don�t want the truth to be exposed.
���������� 4. ��������� ���� ����� ������� �� ������.'''

# d = { '�': 'a', '�': 'k', '�': 'h', '�': 'b', '�': 'l', '�': 'c', '�': 'v', '�': 'm', '�': 'ch', '�': 'g', '�': 'n',
# '�': 'sh', '�': 'd', '�': 'o', '�': 'shh', '�': 'e', '�': 'p', '�': '*', '�': 'jo', '�': 'r', '�': 'y', '�': 'zh',
# '�': 's', '�': "'", '�': 'z', '�': 't', '�': 'je', '�': 'i', '�': 'u', '�': 'ju', '�': 'j', '�': 'f', '�': 'ya',
# '�': 'A', '�': 'K', '�': 'H', '�': 'B', '�': 'L', '�': 'C', '�': 'V', '�': 'M', '�': 'Ch', '�': 'G', '�': 'N',
# '�': 'Sh', '�': 'D', '�': 'O', '�': 'Shh', '�': 'E', '�': 'P', '�': '*', '�': 'Jo', '�': 'R', '�': 'Y', '�': 'Zh',
# '�': 'S', '�': "'", '�': 'Z', '�': 'T', '�': 'Je', '�': 'I', '�': 'U', '�': 'Ju', '�': 'J', '�': 'F', '�': 'Ya' }
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
#     '�': 'a', '�': 'k', '�': 'h', '�': 'b', '�': 'l', '�': 'c', '�': 'v', '�': 'm', '�': 'ch',
#     '�': 'g', '�': 'n', '�': 'sh', '�': 'd', '�': 'o', '�': 'shh', '�': 'e', '�': 'p', '�': '*',
#     '�': 'jo', '�': 'r', '�': 'y', '�': 'zh', '�': 's', '�': "'", '�': 'z', '�': 't', '�': 'je',
#     '�': 'i', '�': 'u', '�': 'ju', '�': 'j', '�': 'f', '�': 'ya'
#     }
# with open('cyrillic.txt', encoding='utf-8') as f_input, open('transliteration.txt', 'w') as f_output:
#     f_output.write(''.join(i if i.lower() not in d else d[i] if i.islower() else d[i.lower()].title() for i in f_input.read()))


# trn, text = dict(zip('��������������������������������', "a b v g d e jo zh z i j k l m n o p r s t u f h c ch sh shh * y ' je ju ya".split())), open('cyrillic.txt').read()
# for s in text:
#     if s.lower() in trn:
#         text = text.replace(s, [trn[s.lower()], trn[s.lower()].title()][s.isupper()])
# print(text, file=open('transliteration.txt', 'w'))

'''����������� �������� ??
��� ��������� ����������� ������� ������������� � ����������� ��������� ���������� �������, �� ��������� � ������������
 ��������. ����� ������������ ����������� ��������� ����� ������������ ����������, � ����� � ����� �������� � ��� ?.

�� ���� ��������� �������� ������ ������ � ������ ���������� �����, � ������� ������� ��� �� ����� Python. �������� 
���������, ��������� �� ����� ����� ���� ������� ��� ������� ����������� ���������� �����������. ����� �������, ���
 ����� ������, ������������ �� ����� def � �������, �������� ������� ����������� �������. ������� ��������
  �����������, ���� ������ ������ ���������� ������ - #.


������ ������� ������
�� ���� ��������� �������� ������ ������, ���������� ��� ������������� ���������� ����� � ����� �� ����� Python.

������ �������� ������
��������� ������ ������� �������� ���� ������� (�� ����� ������� �� ���������� � �������� �����), ������ �� ��������� 
������, ��� ������� ����������� ���������� �����������. ���� ��� ������� � ����� ����� ���������� �����������, 
�� ������� �������: Best Programming Team.

���������� 1. ���� �� ���� �������� ���:

def powers(a):
    return a, a**2, a**3

# ������� ��������� ����� ���� ���������� �����
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# ������� ���������� ���������� ���������� ����������
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

# ������� ��������� ��������� ����������� �����
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
�� ����������� �����:

powers
matrix
mean
greet
���������� 2. �������������, ��� � ����� ���� ���� �� ���� ������� ��� ���� ��������� ������� � ����� ���. '''

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


'''���������� ����� � �����
�� ���� ��������� �������� ������ ������ � ������ ���������� �����. �������� ��������� ��� ������ �� �����
 ���������� ����� ������� �����.

������ ������� ������
�� ���� ��������� �������� ������ ������, ���������� ��� ������������� ���������� �����.

������ �������� ������
��������� ������ ������� ���������� ����� �����.

����������. ��������, ��� ����������� ��������� � ��������� ���� ��������� � ����� �����.'''

# with open('prices.txt') as f:
#    count = sum(1 for _ in f)
# print(count)


# with open(input(),encoding = "utf-8") as file:
#     sp = file.readlines()
#     print(len(sp))

# with open(f'{input()}') as f:
#     print(len(list(f)))

# print(len(open(input()).readlines()))