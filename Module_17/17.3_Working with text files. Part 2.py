'''Тема урока: работа с текстовыми файлами
Позиция (курсор) в файле
Менеджеры контекста
Аннотация. Урок посвящен работе с файлами: позиция считывания в файле, методы seek(), tell(), а также работа с менеджером контекста.

Позиция в файле
Когда мы читаем текст из файла с помощью методов read() или readlines() происходит перемещение текущей позиции в конец файла. При использовании метода readline() текущая позиция перемещается на следующую строку файла.

При открытии файла текущая позиция всегда равна нулю – указывает на первый символ текста. При прочтении файла до конца с помощью вызова методов read(), readlines() позиция перемещается в конец файла и последующие чтения ничего не дают.

Вызов методов read(), readlines(), readline() перемещает текущую позицию туда, где завершилось чтение. Для методов read() и readlines() это конец файла, для метода readline() – следующая строка после прочитанной.

Текущую позицию обычно называют "курсор".

Предположим, у нас есть файл languages.txt. Когда мы его открываем, курсор находится в начале файла, в нулевой позиции, это выглядит примерно так:



Если мы считаем две строки с помощью метода readline():

file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
line2 = file.readline()

file.close()
курсор переместится в начало третьей строки:



Чтение всегда происходит слева направо от курсора. Таким образом, если после двух вызовов метода readline() вызвать метод read(), он считает не весь файл, а только оставшиеся строки:

file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
line2 = file.readline()
remaining_lines = file.read()    # считывание начинается с 3 строки до конца файла

file.close()
После того, как мы считали все строки файла, курсор находится в конце.



После завершения чтения мы больше не можем считать ни одного символа из файла. Все последующие вызовы методов read() или readline() будут приводить к считыванию пустой строки.

Для повторного чтения данных из файла, можно:

переоткрыть файл, тогда курсор снова попадёт в начало;
переместить курсор с помощью файлового метода seek().
Файловый метод seek()
Файловый метод seek() задаёт позицию курсора в байтах от начала файла. Чтобы перевести курсор в самое начало файла необходимо вызвать метод seek(), передав ему в качестве аргумента значение 00.

Приведенный ниже код:

file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
file.seek(0)               # переводим курсор в самое начало
line2 = file.readline()

print(line1, line2)

file.close()
выводит:

Python
Python
Метод seek() не очень полезен при работе с текстовыми файлами, так как не учитывает разделение текста на строки. А вот при работе с файлами в двоичном режиме умение работать с позицией и смещениями очень важно!

Будьте аккуратны с символами, использующими более 11 байта (кириллица в кодировке utf-8), обращение к "промежуточному" байту может вызвать ошибку.

Если метод seek() устанавливает курсор (текущую позицию), то метод tell() получает ее.

Приведенный ниже код:

file = open('languages.txt', 'r', encoding='utf-8')
print(file.tell())
line1 = file.readline()
print(file.tell())

file.close()
выводит:

0
8
В самом начале курсор (текущая позиция) равен нулю, после считывания первой строки, курсор смещается на 88 байт (по байту на каждый из символов 'P', 'y', 't', 'h', 'o', 'n' и два байта на символ перевода строки '\n').

Менеджер контекста
Как уже сказано, важно своевременно закрывать файлы с помощью метода close(). Закрытие файлов вручную, а также отдача
закрытия на откуп среде исполнения, обладают существенным недостатком: если между открытием файла и его закрытием
произойдёт ошибка, в лучшем случае файл окажется открыт слишком долго, а в худшем случае часть данных не сохранится.

Хочется иметь возможность автоматически закрывать файл сразу после окончания работы с ним и осуществлять закрытие даже при возникновении ошибки. Файловые объекты уже умеют работать в таком режиме, но для этого их нужно использовать как менеджеры контекста.

Менеджер контекста — объект, реализующий одноименный протокол. Объекты, реализующие этот протокол, позволяют использовать следующий специальный синтаксис:

with object as name:
    # Здесь нам доступен ресурс name.
    # Это тело with-блока.
# А здесь ресурс name уже освобождён, даже если в теле with-блока произошла ошибка.
Весь код в теле with-блока работает "в контексте". Чаще всего контекст подразумевает выделение некоего ресурса, например, файла. По выходу из контекста ресурс автоматически освобождается, даже если при выполнении блока возникло исключение.

Как только закончится код, оформленный с отступами в with (аналогичные отступы в циклах или функциях), это будет означать, что контекст закончился, и Python автоматически закроет файл.

Приведенный ниже код:

file = open('languages.txt', 'r', encoding='utf-8')

for line in file:
    print(line)

file.close()              # ручное закрытие файла

print('Файл закрыт')
можно переписать в виде:

with open('languages.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
                          # автоматическое закрытие файла
print('Файл закрыт')
Обратите внимание: при использовании менеджера контекста не требуется использовать метод close().

   При работе с файлами желательно всегда использовать менеджер контекста. Это делает программу надежнее.

Примечания
Примечание 1. Подробнее о файловом методе seek() можно почитать в документации.

Примечание 2. В современных операционных системах файловый ввод-вывод устроен достаточно сложно. Для обеспечения
максимального быстродействия чтения и записи в файлы, а также контроля безопасности этого процесса, большинство
операционных систем не позволяют программам напрямую работать с диском. Операционная система предоставляет программам
специальные объекты — файловые дескрипторы (функция open() возвращает как раз файловый дескриптор). Имея файловый
 дескриптор, можно записывать и читать данные, не задумываясь о файловой системе. Файловые дескрипторы удобны, но на
 создание каждого расходуется достаточно большое количество ресурсов. Поэтому у операционной системы есть общий лимит
 на количество одновременно использующихся файловых дескрипторов. И при этом каждая программа имеет свой собственный лимит. Как только программа исчерпает доступное ей количество дескрипторов, следующая попытка открыть очередной файл закончится с ошибкой. Программисту важно следить за тем, сколько файлов программа открывает в каждый момент и закрывает ли она их своевременно. Используйте менеджер контекста with и жизнь станет проще 😋.

Примечание 3. С помощью менеджера контекста можно работать с несколькими файлами.

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # обработка файлов'''

# with open('input.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')


'''Переворот строки
Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку
 в обратном порядке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строку указанного файла в обратном порядке.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Указанный файл можно скачать по ссылке.'''

# with open('text.txt', encoding='utf-8') as file:
#     for line in file:
#         print(line[::-1])

# with open('text.txt') as f:
#     print(f.read()[::-1])


# with open('text.txt') as f:
#     content = f.read()
# print(content[::-1])

# with open('text.txt', 'r') as f:
#   [print(i[:: -1]) for i in f]

'''Обратный порядок
Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки
 данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла в обратном порядке.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Получить список всех строк файла можно при помощи метода readlines().

Примечание 4. Не забывайте про символ конца строки '\n'.

Примечание 5. Указанный файл можно скачать по ссылке.'''

# with open('data.txt') as f:
#     for line in reversed(f.readlines()):
#         print(line, end='')

# with open('data.txt', encoding='utf-8') as file:
#     print(*file.readlines()[::-1], sep='')


# with open('text.txt') as f:
#     print(*[i.rstrip() for i in f.readlines()][::-1], sep='\n')


# with open('data.txt','r',encoding='utf-8') as file:
#     l = list(map(str.strip,file.readlines()))
#     for i in range(len(l) - 1,-1,-1):
#         print(l[i])

'''Длинные строки
Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все 
строки наибольшей длины из файла, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Если бы файл lines.txt содержал строки:

One
Twenty one
Two
Twenty two
то результатом будет:

Twenty one
Twenty two
Примечание 4. Указанный файл можно скачать по ссылке. '''

# from sys import stdout
#
# with open('lines.txt', 'r') as f:
#     str_len = max(map(len, map(str.rstrip, f)))
#     f.seek(0)
#     for line in filter(lambda s: len(s.rstrip()) == str_len, f):
#         stdout.write(f"{line.rstrip()}\n")


# with open('lines.txt') as f:
#     lines = [line.strip() for line in f.readlines()]
#     longest = max(map(len, lines))
#     print(*filter(lambda x: len(x) == longest, lines), sep='\n')


# with open('lines.txt') as f:
#     max_len, longest = 0, []
#     for line in f:
#         line = line.rstrip('\n')
#         line_len = len(line)
#         if line_len == max_len:
#             longest.append(line)
#         elif line_len > max_len:
#             max_len, longest = line_len, [line]
#
# print('\n'.join(longest))

# with open('lines.txt', encoding='utf-8') as file:
#     text = file.readlines()
#
# n = len(max(text, key=len))
# print(*filter(lambda x: len(x) == n, text), sep='')

'''Сумма чисел в строках
Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел, 
разделенных одним или несколькими пробелами.

Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки 
выводится сумма чисел в этой строке).

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел в каждой строке.

Примечание 1. Если бы файл numbers.txt содержал строки:

2 1
     3    4
 1       7
то результатом было бы:

3
7
8
Примечание 2. Указанный файл можно скачать по ссылке. '''

'''Сумма чисел в файле
Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все, что угодно. Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму всех чисел, записанных в файле.

Примечание 1. Если бы файл nums.txt содержал строки:

 123   jhjk
bhjip456qwerty
1x2y3 4 5 6
sfsd 0 dfgfd
10abc20de30pop5 5 5 5
то результатом было бы:

680'''

# import re
#
# text = open('numss.txt').read()
# total = sum(map(int, re.findall(r'\d+', text)))
# print(total)

# with open('numbers.txt', encoding='utf-8') as file:
#     row = ''.join(c if c.isdigit() else ' ' for c in file.read())
#     print(sum(map(int, row.split())))


# with open('numbers.txt') as file:
#     temp = ''
#     n = 0
#     for c in file.read():
#         if c.isdigit():
#             temp += c
#         elif temp != '':
#             n += int(temp)
#             temp = ''
#     print(n)


# import re
# print(sum(map(int, re.findall(r'\d+', open('numbers.txt').read()))))


# import csv
#
#
# def read_csv():
#     filename = 'data.csv'
#     line_count = 0
#     with open(filename, 'r') as csvfile:
#         csvreader = csv.DictReader(csvfile)
#         for row in csvreader:
#             if line_count == 0:
#                 line_count += 1
#             print(f'{row}, ')
#             line_count += 1
# read_csv()


'''Нумерация строк
Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 11.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Используйте встроенную функцию enumerate().

Примечание 3. Если бы файл input.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
то файл output.txt имел бы вид:

1) Beautiful is better than ugly.
2) Explicit is better than implicit.
3) Simple is better than complex.
4) Complex is better than complicated.
Примечание 4. Указанный файл можно скачать по ссылке.'''

# with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
#     content = input.readlines()
#     for n, string in enumerate(content):
#         output.write(f'{n + 1}) {string}')

# with open('input.txt') as inp, open('output.txt', 'w') as out:
#     data = inp.readlines()
#     out.writelines([f'{i + 1}) {data[i]}' for i in range(len(data))])


# with open('input.txt') as inp, open('output.txt', 'w') as out:
#     for i, j in enumerate(inp, start=1):
#         print(f'{i}) {j}', end='', file=out)

# with open('input.txt') as fin, open('output.txt', 'w') as fout:
#     [fout.write(f'{i}) {line}') for i, line in enumerate(fin, 1)]


# with open('input.txt', 'r') as i, open('output.txt', 'w+') as o:
#   count=1
#   for line in i:
#     o.write(str(count)+") "+line)
#     count+=1


'''Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и
 оценка разделены пробелом). Оценка - целое число от 00 до 100100 включительно.

Напишите программу для добавления 55 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в 
файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл class_scores.txt содержал строки:

Washington 83
Adams 86
Kingsman 100
MacDonald 95
Thomson 98
то файл new_scores.txt имел бы вид:

Washington 88
Adams 91
Kingsman 100
MacDonald 100
Thomson 100'''

# with open('class_scores.txt', 'r', encoding='utf-8') as input, open('new_scores.txt', 'w', encoding='utf-8') as output:
#     content = [(el.strip() for el in line.split()) for line in input.readlines()]
#     for (name, score) in content:
#         if int(score) > 95:
#             output.write(f'{name} 100\n')
#         else:
#             output.write(f'{name} {str(int(score) + 5)}\n')


# open('new_scores.txt', 'w').writelines([f'{s} {min(int(m) + 5, 100)}\n' for r in
#                                         open('class_scores.txt').readlines() for s, m in [r.rstrip().split()]])


# with open('class_scores.txt') as inn:
#     inner = inn.readlines()
# with open('new_scores.txt', 'w') as out:
#     for i in inner:
#         a, b = i.split()
#         out.write(f'{a} {int(b) + 5 if int(b) <= 95 else 100}\n')


# with open('class_scores.txt') as fi, open('new_scores.txt', 'w') as fo:
#     for line in fi:
#         li = line.rstrip().split()
#         score = int(li[1])+5 if int(li[1]) <= 95 else 100
#         fo.write(li[0] + ' ' +str(score) + '\n')


'''Конкатенация файлов 🌶️
На вход программе подается натуральное число n и n строк с названиями файлов. Напишите программу, которая создает файл
 output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число nn и nn строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.'''

# with open('output.txt', 'a', encoding='utf-8') as output:
#     for _ in range(int(input())):
#         with open(input(), 'r', encoding='utf-8') as file:
#             output.writelines(file.readlines())


# with open('output.txt', 'w') as out:
#     for i in range(int(input())):
#         with open(input()) as f:
#             out.write(f.read())


# with open('output.txt', 'a', encoding='utf-8') as file:
#     for _ in range(int(input())):
#         with open(input(), 'r', encoding='utf-8') as others:
#             file.writelines(others)


# names = [input() for _ in range(int(input()))]
# with open('output.txt', 'w') as file:
#     for name in names:
#         with open(name) as el:
#             file.write(el.read())


'''ог файл 🌶️
Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее. Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа, время выхода, где время указано в 2424-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей (не меняя порядка следования), которые были в сети не менее часа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Считайте, что каждый пользователь был только раз в системе, то есть в файле нет двух строк с одинаковым пользователем.

Примечание 3. Если бы файл logfile.txt содержал строки:

Тимур Гуев, 14:10, 15:50
Руслан Гриценко, 12:00, 12:59
Роман Гацалов, 09:10, 17:45
Габолаев Георгий, 11:10, 12:10
то файл output.txt имел бы вид:

Тимур Гуев
Роман Гацалов
Габолаев Георгий'''

# from datetime import datetime
#
# with open('logfile.txt', encoding='utf-8') as logfile, open('output.txt', 'w') as output:
#     for log in logfile.read().split('\n'):
#         name, first_time, second_time = log.split(', ')
#         delta = datetime.strptime(second_time, "%H:%M") - datetime.strptime(first_time, "%H:%M")
#         if delta.seconds >= 3600:
#             print(name, file=output)


# def get_diff_mins(time2, time1):
#     t2 = list(map(int, time2.split(':')))
#     t1 = list(map(int, time1.split(':')))
#     return (t2[0]*60 + t2[1]) - (t1[0]*60 + t1[1])
#
# with open('logfile.txt', encoding='utf-8') as inputf, open('output.txt', 'w') as outputf:
#     for fn in inputf:
#         name, time1, time2 = fn.strip().split(', ')
#         if get_diff_mins(time2, time1) >= 60:
#             print(name, file=outputf)

# from datetime import timedelta
#
# with open('logfile.txt', encoding='utf-8') as file:
#     logs = list(map(lambda x: x.rstrip().split(', '), file.readlines()))
#     with open('output.txt', 'w', encoding='utf-8') as output:
#         for log in logs:
#             name, start, end = log[0], log[1].split(':'), log[2].split(':')
#             t = timedelta(hours=int(end[0]), minutes=int(end[1])) -\
#                 timedelta(hours=int(start[0]), minutes=int(start[1]))
#             if t.seconds >= 3600: output.write(name+'\n')


'''Сумма чисел в строках
Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел, 
разделенных одним или несколькими пробелами.

Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки 
выводится сумма чисел в этой строке).

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел в каждой строке.

Примечание 1. Если бы файл numbers.txt содержал строки:

2 1
     3    4
 1       7
то результатом было бы:

3
7
8
Примечание 2. Указанный файл можно скачать по ссылке. '''


# with open('numbers.txt', 'r') as fin:
#     for c in fin:
#         ans = sum(int(line) for line in c.rstrip('\n\r').split(" ") if line.isnumeric())
#         print(ans)

# with open('numbers.txt') as f:
#     for line in f:
#         print(sum(map(int, line.split())))


# with open('numbers.txt', encoding='utf-8') as file:
#     f = map(lambda x: x.split(), file.readlines())
#     print(*map(lambda x: sum(map(lambda i: int(i), x)), f), sep='\n')

# with open('numbers.txt') as f:
#     print(*(sum(map(int, line.split())) for line in f), sep='\n')


# with open('numbers.txt') as f:
#     ls = f.readlines()
#     for i in ls:
#         print(sum(int(j) for j in i.split()))

'''Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв
 латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
то результатом было бы:

Input file contains:
108 letters 
20 words 
4 lines 
Примечание 2. Словом называется последовательность из непробельных символов. Например, строка

abc a21 67pop    qwert bo7ok 83456
содержит 66 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

Примечание 3. Указанный файл можно скачать по ссылке.'''


# import re
#
# with open('file.txt', 'r') as f:
#     f = f.read().rstrip()
# num_chars = sum([1 for x in f if x.isalpha()])
# num_words = len(re.findall(r"\w+", f))
# num_lines = len(f.split('\n'))
#
# print("Input file contains:")
# print(num_chars, "letters")
# print(num_words, "words")
# print(num_lines, "lines")
#

# with open('lines.txt') as f:
#     txt = f.read()
#     print('Input file contains:')
#     print(sum(map(str.isalpha, txt)), 'letters')
#     print(len(txt.split()), 'words')
#     print(txt.count('\n') + 1, 'lines')

# with open('lines.txt') as f:
#     res = f.readlines()
#     f.seek(0)
#     words = f.read().split()
#     let = sum(len([y for y in x if y.isalpha()]) for x in words)
#
# print('Input file contains:')
# print(f'{let} letters')
# print(f'{len(words)} words')
# print(f'{len(res)} lines')


# with open("file.txt", "r", encoding='utf-8') as file:
#     l = [[j.strip('\n",.-:!?0123456789') for j in i.split()] for i in file]
#     lines = len(l)
#     words = 0
#     letters = 0
#     for i in l:
#         words += len(list(filter(lambda x: x != None, i)))
#         for j in i:
#             if j != None:
#                 letters += len(j)
#     print(f"Input file contains:\n{letters} letters\n{words} words\n{lines} lines")


# with open('file.txt', 'r') as f:
#     data = f.read()
#     print('Input file contains:')
#     print(len([i for st in data for i in st if i.isalpha()]), 'letters')
#     print(len(data.split()), 'words')
#     print(len(data.split('\n')), 'lines')

'''Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 33 случайные пары имя + фамилия, а затем выводит их,
 каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.

Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:

Aaron
Abdul
Abe
Abel
Abraham
Albert
и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein
то результатом могло быть:

Abdul Albertson
Abel Adamson
Albert Einstein'''

# from random import randint
# with open("first_names.txt") as f1, open("last_names.txt") as f2:
#     names = list(map(lambda x: x.strip(),f1.readlines()))
#     lnames = list(map(lambda x: x.strip(),f2.readlines()))
#     for i in range(3):
#         print(f'{names[randint(0,len(names))-1]} {lnames[randint(0,len(lnames))-1]}')


# import random
#
#
# with open('first_names.txt', 'r', encoding='utf-8') as f, open('last_names.txt', 'r', encoding='utf-8') as l:
#     z, x = f.readlines(), l.readlines()
#     for i in range(3):
#         print(random.choice(z).strip(), random.choice(x).strip(), sep=' ')

# with open('first_names.txt') as f, open('last_names.txt') as f2:
#     for i in range(3):
#         file1 = f.readline()
#         file2 = f2.readline()
#         print(file1.strip(), file2.strip())


# from random import choice
#
# with open('first_names.txt') as f_names, open('last_names.txt') as f_surnames:
#     names, surnames = f_names.read().split(), f_surnames.read().split()
#
# for _ in '123':
#     print(choice(names), choice(surnames))

'''Необычные страны
Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом 
табуляции '\t'.

Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых 
больше чем 500000 человек, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести названия стран, удовлетворяющие условиям задачи, каждое на отдельное строке.

Примечание. Указанный файл можно скачать по ссылке.'''

# with open("population.txt") as f:
#     list_s = f.readlines()
#     list_s = list(map(lambda x: x.strip().split("\t"), list_s))
#     list_s = list(filter(lambda x: x[0][0] =="G" and int(x[1]) > 500000, list_s ))
#     for i in list_s:
#         print(i[0])


# with open('population.txt') as f:
#     for line in f:
#         n, p = line.split('\t')
#         if n.startswith('G') and int(p) > 500000:
#             print(n)


# with open('population.txt') as file:
#     [print(' '.join(w[:-1])) for s in file for w in [s.split()] if w[0][0] == 'G' and int(w[-1]) > 5e5]


# with open('population.txt') as f1:
#     ls1 = f1.readlines()
# for i in ls1:
#     a, b = i.split('\t')
#     if a[0] == 'G' and int(b) > 500_000:
#         print(a)

'''CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из
 этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую
  строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функции read_csv не должна принимать аргументов. 

Примечание 2. Подробнее прочитать про CSV-файлы можно тут.

Примечание 3. Считайте, что все ключи и значения по этим ключам в результирующем словаре имеют строковый тип (str).

Примечание 4. Указанный файл можно скачать по ссылке.

Примечание 5. Если бы файл data.csv содержал информацию

name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
то вызов функции read_csv() вернул бы список:

[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, 
{'name': 'John', 'address': '54 Love Ave', 'age': '21'}]'''

# def read_csv():
#     with open('data.csv') as f:
#         i = 0
#         sp = []
#         for line in f:
#             line =line.strip()
#             if i  == 0:
#                 keys = line.split(",")
#             else:
#                 values = line.split(",")
#                 sp.append({keys[i] : values[i] for i in range(len(keys))})
#             i +=1
#         return sp

# def read_csv():
#     with open('data.csv') as csv:
#         key_name = csv.readline().rstrip().split(',')
#         return [dict(zip(key_name, c.rstrip().split(','))) for c in csv]

# def read_csv():
#     with open("data.csv", encoding = "utf-8") as date_csv:
#         date_key = date_csv.readline().rstrip("\n").split(",")
#         result = []
#         for line in date_csv:
#             date_value = line.rstrip("\n").split(",")
#             result.append(dict(zip(date_key,date_value)))
#     return result

# def read_csv():
#     with open('data.csv') as file:
#         keys = file.readline().strip().split(',')
#         return [*map(lambda line: dict(zip(keys, line.strip().split(','))), file)]
# print(read_csv())
#
# **************************************************************


