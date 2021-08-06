'''Тема урока: работа с текстовыми файлами, чтение данных
Открытие и закрытие файлов
Указание кодировки
Чтение данных из файла
Аннотация. Урок посвящен работе с файлами. Изучим функцию open() и метод close(), узнаем как задавать правильную
кодировку и научимся читать информацию с помощью методов read(), readline(), readlines().

Работа с файлами в Python
Высокоуровневый язык программирования Python предоставляет своим пользователям массу полезных средств для
взаимодействия с файлами. Встроенные функции и методы позволяют создавать файлы, читать из них данные, а также
 всячески манипулировать их содержимым.

Открытие файла
Для открытия файлов в Python существует функция open(). Она создает файловый объект и связывает его с файлом на
диске. Общий формат применения функции open():

файловая_переменная = open(имя_файла, режим_доступа)
Здесь

файловая переменная – имя переменной, которая ссылается на файловый объект;
имя_файла – строковый литерал, задающий имя файла;
режим_доступа – строковый литерал, задающий режим доступа (чтение, запись, и т.д.), в котором файл будет открыт.
Ниже представлены строковые литералы (символы), используемые для задания режима доступа.

Стр. литерал

Режим	Описание
'r'
Read (чтение)

Открыть файл только для чтения. Такой файл не может быть изменен.
'w'	Write (запись)	Открыть файл для записи. Если файл уже существует, стереть его содержимое.
Если файл не существует, он будет создан.
'a'	Append (добавление)	Открыть файл для записи. Данные будут добавлены в конец файла. Если файл не существует, он
будет создан.
'r+'	Read + Write	Открыть файл для чтения и записи. В этом режиме происходит частичная перезапись содержимого
 файла.
'x'	Create (создание)	Создать новый файл. Если файл существует, произойдет ошибка.
Предположим, файл students.txt содержит данные о студентах, и мы хотим открыть его для чтения.

Это можно сделать с помощью строки кода:

student_file = open('students.txt', 'r')
По умолчанию режим доступа (второй аргумент функции open()) определен для чтения (литерал 'r'), поэтому файл
students.txt можно открыть для чтения так:

student_file = open('students.txt')   # по умолчанию режим доступа для чтения ('r')
В результате исполнения этой инструкции будет открыт файл students.txt и переменная student_file будет ссылаться на
 файловый объект, который можно использовать для чтения данных из файла.

Обратите внимание, что в переменную student_file в примере выше не попадает содержимое файла students.txt. Фактически
это ссылка на файл, ее еще называют дескриптор файла.

Предположим, надо создать файл с именем sales.txt и записать в него данные о продажах. Это можно сделать с помощью
 строки кода:

sales_file = open('sales.txt', 'w')
После исполнения этого кода будет создан файл sales.txt и переменная sales_file будет ссылаться на файловый объект,
который можно использовать для записи в него данных.

Указание места расположения файла
Когда в функцию open() передается имя файла без указания пути, интерпретатор Python исходит из предположения, что
место расположения файла то же, что у исполняемой программы. Например, программа расположена в папке
C:\Users\Documents\Python. Если программа выполняется и исполняет инструкцию:

customer_file = open('customers.txt', 'r')
то файл customer.txt программа станет искать в папке C:\Users\Documents\Python.

Аналогично, если программа выполняется, и она исполняет инструкцию:

sales_file = open('sales.txt', 'w')
то файл sales.txt создается в той же папке.

Если имя файла не содержит путь, то используется относительный путь, относительно папки, где находится исполняемая
программа.

Если требуется открыть файл, расположенный в другом месте, нужно указать путь и имя файла в аргументе, передаваемом в
 функцию open().

Приведенный ниже код создает файл test.txt в папке C:\Users\temp:

test_file = open('C:\\Users\\temp\\test.txt', 'w')
Обратите внимание: символ \ является специальным символом в Python и его нужно экранировать (\\), чтобы интерпретатор
Python рассматривал обратную косую черту как обычный символ.

Вместо экранирования символов можно использовать сырые строки (raw strings). Для этого следует снабдить строковый
литерал префиксом в виде буквы r.

test_file = open(r'C:\Users\temp\test.txt', 'w')
Приведенный выше код создает файл test.txt в папке C:\Users\temp. Префикс r указывает на то, что строковый литерал
 является сырым (неформатированным).

Механизм сырых строк очень удобен не только при работе с файлами.

Приведенный ниже код:

path = 'C:\new\text.txt'
print(path)
выводит:

C:
ew	ext.txt
поскольку символы \n и \t интерпретируются как перенос строки и табуляция.

Приведенный ниже код:

path = r'C:\new\text.txt'
print(path)
выводит содержимое строки path:

C:\new\text.txt
Чтобы сделать работу с файлами универсальнее, в путях файлов в Windows в Python-программах рекомендуется ставить
прямой слеш (/). В наших примерах мы так и будем делать:

file1 = open(r'C:/Users/temp/test.txt')    # используем прямой слеш / (абсолютный путь)
file2 = open(r'temp/data.txt')             # используем прямой слеш / (относительный путь)
Кодировка
Открыть файл, содержащий только латиницу и цифры, можно так:

file = open('info.txt', 'r')
При работе с текстом на русском языке нужно указать кодировку, для этого служит параметр encoding:

file = open('info.txt', 'r', encoding='utf-8')
   Указание кодировки при открытии файла – хороший тон. Рекомендуем придерживаться этого правила.

Чтобы получить кодировку открытого файла используют файловое свойство encoding.

Приведенный ниже код:

file1 = open('students.txt', 'w')
file2 = open('customers.txt', 'w', encoding='utf-8')

print(file1.encoding)
print(file2.encoding)

file1.close()
file2.close()
выводит на компьютере с операционной системой Windows:

cp1252
utf-8
Закрытие файлов
После окончания работы с файлом его необходимо закрыть. Для этого есть несколько причин:

если файл изменялся, это позволит корректно его сохранить;
если открытый файл потребуется другим программам, ваша программа может его блокировать;
не стоит держать в памяти лишние, уже не нужные, данные;
удалить открытый кем-то файл проблематично.
Для закрытия файла используется файловый метод close():

file = open('info.txt', 'r')    # открываем файл с именем info.txt для чтения

                                # работаем с содержимым файла info.txt

file.close()                    # закрываем файл после окончания работы
Чтобы проверить открыт файл или закрыт можно использовать файловое свойство (атрибут) closed.

Приведенный ниже код:

file1 = open('students.txt', 'w')
file2 = open('customers.txt', 'w')

file1.close()

print(file1.closed)
print(file2.closed)

file2.close()
выводит:

True
False
Обратите внимание на то, что при вызове метода мы используем скобки: close(), а при вызове свойства (атрибута) скобок
 нет closed. Методы совершают действия, а свойства возвращают информацию о объекте (привет ООП 😉).

Чтение содержимого файла
Как уже сказано, при открытии файла с помощью функции open() в файловую переменную попадает не содержимое файла, а
ссылка на файл (дескриптор файла).

Приведенный ниже код:

file = open('info.txt', 'w', encoding='utf-8')    # открываем файл для записи

print(file)
выводит:

<_io.TextIOWrapper name='info.txt' mode='w' encoding='utf-8'>
Для чтения содержимого открытого для чтения файла используются три файловых метода:

read() – читает все содержимое файла;
readline() – читает одну строку из файла;
readlines() – читает все содержимое файла и возвращает список строк.
Предположим, в папке с исполняемой программой есть текстовый файл languages.txt с содержимым:

Python
Java
Javascript
C#
C
C++
PHP
R
Objective-C
Метод read()
Файловый метод read() считывает все содержимое из файла и возвращает строку, которая может содержать символы перехода
 на новую строку '\n'.

Приведенный ниже код:

file = open('languages.txt', 'r', encoding='utf-8')

content = file.read()

file.close()
считывает содержимое файла languages.txt в переменную content. В переменной content будет содержаться строка
'Python\nJava\nJavascript\nC#\nC\nC++\nPHP\nR\nObjective-C'.

Таким образом метод read() считывает все содержимое файла, включая переносы строк:

Если методу read() передать целочисленный параметр, то будет считано не более заданного количества символов.
Например, считывать файл посимвольно можно при помощи метода read(1).

Метод readline()
Файловый метод readline() считывает одну строку из файла (до символа конца строки '\n'), при этом возвращается
считанная строка вместе с символом '\n'. Если считать строку не удалось – достигнут конец файла и больше строк в
нем нет, возвращается пустая строка.

Приведенный ниже код:

file = open('languages.txt', 'r', encoding='utf-8')

language = file.readline()

file.close()
считывает содержимое первой строки файла languages.txt в переменную language. В переменной language будет
 содержаться строка 'Python\n'.

Для удаления символа '\n' из конца считанной строки удобно использовать строковый метод rstrip().

Приведенный ниже код:

line = 'Python\n'
line = line.rstrip()
удаляет символ \n из содержимого строки line, в результате чего в переменной line содержится строка 'Python'.

   Если вдруг вы забыли о строковых методах, освежить знания можно тут, тут и тут 🥰.

Прочитать содержимое всего файла построчно можно двумя способами.

С помощью цикла while:

file = open('languages.txt', 'r', encoding='utf-8')

line = file.readline()         # считываем первую строку

while line != '':              # пока не конец файла
    print(line.strip())        # обрабатываем считанную строку
    line = file.readline()     # читаем новую строку

file.close()
С помощью цикла for (предпочтительный вариант):

file = open('languages.txt', 'r', encoding='utf-8')

for line in file:
    print(line.strip())

file.close()
Метод readline() довольно удобен, когда мы хотим управлять процессом чтения из файла, особенно если файл очень
 большой и его полное считывание может привести к нехватке памяти.

Метод readlines()
Файловый метод readlines() считывает все строки из файла и возвращает список из всех считанных строк (одна строка —
один элемент списка). При этом, каждая строка в списке заканчивается символом переноса строки  '\n'😅.

Приведенный ниже код:

file = open('languages.txt', 'r', encoding='utf-8')

languages = file.readlines()

file.close()
считывает содержимое файла languages.txt в переменную languages. В переменной language будет содержаться список:

['Python\n', 'Java\n', 'Javascript\n', 'C#\n', 'C\n', 'C++\n', 'PHP\n', 'R\n', 'Objective-C']
Чтобы удалить символ '\n' можно использовать списочное выражение:

languages = [line.strip() for line in file.readlines()]
либо функцию map()🤩:

languages = list(map(str.strip, file.readlines()))
либо анонимную функцию:

languages = list(map(lambda line: line.strip(), file.readlines()))
Если передать в функцию list() ссылку на файловый объект list(file) , получим тот же результат, что при вызове метода
file.readlines().

Примечания
Примечание 1. Язык Python позволяет работать не только с текстовыми, но и с бинарными файлами. Ниже представлены
строковые литералы, которые можно использовать для задания режима обработки файла.

    Символ   	Режим	Описание
't'	Текстовый режим (значение по умолчанию)	Работа с текстовым файлом
'b'	Бинарный режим	Работа с бинарными файлами (картинки, звук и т.д.)
Режим обработки файла указывается после режима доступа к файлу.

Приведенный ниже код открывает файл file.dat в режиме чтения как бинарный файл.

file = open('file.dat', 'rb')
По умолчанию функция open() использует литерал 'rt', то есть файл открывается для чтения в текстовом  режиме.

Таким образом, открыть текстовый файл для чтения можно так open('info.txt') или так open('info.txt', 'r') или так
 open('info.txt', 'rt').

Примечание 2. Так как Python — язык с автоматическим управлением памятью, все файлы закрываются автоматически после
успешного завершения программы или когда удаляется последняя ссылка на файловый объект. Но важно все равно закрывать
 файл, как только он перестает быть нужным. Это помогает избегать конфликтов совместного доступа и риска получить
 испорченный файл, если программа завершится аварийно.

   Файл должен быть закрыт сразу после того, как все нужное из него прочитано или в него записано.

Примечание 3. Еще раз обратите внимание на то, что в путях до файла используются прямые слеши /. Можно использовать
и обратные, но тогда их придется экранировать либо применять модификатор сырой строки r. Кроме того, в unix-подобных
 операционных системах принято использовать именно прямой слеш.

Примечание 4. Существуют специальные символы:

\n – перемещает позицию печати на одну строку вниз;
\r – перемещает позицию печати в крайнее левое положение строки.
Приведенный ниже код:

print('aaaaaa\nbb')
выводит:

aaaaaa
bb
 Приведенный ниже код:

print('aaaaaa\rbb')
выводит:

bbaaaa
Приведенный ниже код:

print(ord('\n'))
print(ord('\r'))
выводит:
10
13
Примечание 5. После того, как файл (file) открыт, можно получить различную относящуюся к нему информацию. Три полезных
 атрибута (свойства):

Атрибут (свойство)	Описание
file.closed	возвращает истину (True), если файл закрыт, иначе возвращает ложь (False)
file.mode	возвращает режим доступа с помощью которого был открыт файл
file.name	возвращает имя файла'''