# m = int(input())
# print(*sorted(set.intersection(*({input() for _ in range(int(input()))} for _ in range(m)))), sep="\n")

# m = int(input()) # Считываем число листков M
# print(* # Оператор разыменовывания итератора полученного пересечения множеств (блоков строчек)
#     set.intersection( # Выводим построчно пересечение следующих множеств:
#     * # Оператор разыменовывания итератора генерируемых множеств (блоков строчек)
#     (
#         # Считываем очередной блок фамилий во множество:
#         {input() # Считываем очередную фамилию в блоке (после того, как считали количество фамилий в блоке)
#         for _ in range(int(input())) # Считываем количество фамилий в блоке, затем итерируем N строк
#         } # Ввод окончен
#         for _ in range(m) # Итерируем M блоков
#     )), sep="\n" # Наш сепаратор - перевод строки
# )

# a = int(input())
# b = int(input())
# z = set()
# x = set()
# count= 0
# for v in range(a):
#     c = input()
#     z.add(c)
# for n in range(b):
#     s = input()
#     x.add(s)
# count = len(z ^ x)
# print(count if count > 0 else 'NO')

# myset1 = set(input())
# myset2 = set(input())
# if myset2 == myset1:
#     print("YES")
# else:
#     print("NO")

#
# a = int(input())
# b = int(input())
# z = set()
# x = set()
#
# for v in range(a):
#     c = input()
#     z.add(c)
# for n in range(b):
#     s = input()
#     x.add(s)
#
# count = len(z ^ x)
# print(count if count > a else 'NO')

'''Странное увлечение
Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса. Каждый день Тимур
решает ровно две сложные математические задачи. Решая первую задачу, он записывает на первом листочке все числа,
 которые в ней встречаются. Далее он делает паузу и берется за вторую задачу. Затем записывает на втором листочке
 все числа, которые в ней встречаются. После этого он берет еще один листок и выписывает на него все совпадающие
 числа из первых двух листочков. Если такие числа есть, день удался, если общих чисел нет, Тимур считает день неудачным.

Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏

Формат входных данных
На вход программе подаются две строки с числами: в первой строке числа с первого листочка, во второй со второго.

Формат выходных данных
Программа должна вывести числа, встретившиеся на обоих листках в отсортированном по убыванию порядке, либо
словосочетание BAD DAY, если таких чисел нет.

Sample Input 1:

6 56 7 34 14
675 45 246 2 1
Sample Output 1:

BAD DAY
Sample Input 2:

1 2 3 4 5 6 12
6 5 4 3 2 1
Sample Output 2:

6 5 4 3 2 1
Sample Input 3:

24 6 14 7
7 24 6 98 53
Sample Output 3:

24 7 6'''

# z = set(map(int, input().split()))
# x = set(map(int, input().split()))
# y = (x&z)
#
# print(*['BAD DAY'] if len(x.intersection(z)) <= 0 else sorted(y,reverse=True))

# a=set(list(map(int, input().split())))
# b=set(list(map(int, input().split())))
# print(*sorted(a&b,reverse=True) if not a.isdisjoint(b) else ['BAD DAY'])
#
#
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if len(a&b) == 0: print('BAD DAY')
else: print(*sorted((a&b), reverse=True))


# a = int(input())
# b = int(input())
# z = set()
# x = set()
#
# for v in range(a):
#     c = input()
#     z.add(c)
# for n in range(b):
#     s = input()
#     x.add(s)
#
# count = len(z ^ x)
# print(count if count > 0 else 'NO')


'''Онлайн-школа BEEGEEK 5 🌶️
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета.
У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников перемешались.

Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.

Формат входных данных
На вход программе в первых двух строках подаются числа mm и nn – количества учеников, изучающих математику и
информатику соответственно. Далее идут m+nm+n строк — фамилии учеников, изучающих математику и информатику, в
произвольном порядке.

Формат выходных данных
Программа должна вывести количество учеников, которые изучают только один предмет. Если таких учеников не окажется,
то необходимо вывести NO.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

Sample Input 1:

2
3
Хохлов
Фадеев
Ершов
Ушаков
Хохлов
Sample Output 1:

3
Sample Input 2:

5
1
Игнатов
Мухин
Сафонов
Калашников
Демин
Рыбаков
Sample Output 2:

6'''

# num1 = int(input())
# num2 = int(input())
# eng = set()
# ger = set()
#
# for i in range(num1):
#     c = input()
#     eng.add(c)
# for i in range(num2):
#     c = input()
#     ger.add(c)
#
# eng_ger = eng.union(ger)
# german = len(eng_ger) - num1
# english = len(eng_ger) - num2
# english_german = german + english
#
# if english_german > 0:
#     print(english_german)
# else:
#     print('NO')

# n, m = int(input()), int(input())
# a = [input() for _ in range(n+m)]
# if len(set(a)) - (len(a) - len(set(a))) != 0: print(len(set(a)) - (len(a) - len(set(a))))
# else: print('NO')


# n, m = int(input()), int(input())
# set1 = [input() for row in range(n + m)]
#
# temp = set(set1)
# count = 0
# for i in temp:
#     if set1.count(i) == 1:
#         count += 1
# if count == 0:
#     print('NO')
# else:
#     print(count)


# m,n=int(input()),int(input())
# s=[input() for i in range(n+m)]
# s1=set()
# for i in s:
#     if i not in s1:
#         s1.add(i)
#     else:
#         s1.remove(i)
# print(("NO",len(s1))[len(s1)!=0])


'''Восход
На спутнике «Восход» установлен прибор для измерения солнечной активности. Каждую минуту он передаёт в обсерваторию по 
каналу связи положительное целое число — количество энергии солнечного излучения. Для правильного анализа результатов
 нет необходимости держать повторяющиеся данные. Напишите программу, которая выводит максимальное количество показаний 
 спутника, при удалении которых результат будет правильно проанализирован.

Формат входных данных
На вход программе подаётся одна строка, содержащая числа – показания спутника «Восход». Числа указываются через пробел.

Формат выходных данных
Программа должна вывести максимальное количество показаний, после удаления которых анализ результатов будет произведен
 верно.

Sample Input 1:

10 20 30 10 40
Sample Output 1:

1
Sample Input 2:

1 2 3 4 5 6 7 8 9 1 2 3
Sample Output 2:

3
Sample Input 3:

100 100 100 100 100 100 100
Sample Output 3:

6'''

# m=input().split()
# s=set(i for i in m)
# s1=[i for i in m]
# print(len(s1)-len(s))

# l = input().split()
# print(len(l) - len(set(l)))


# ls = [int(_) for  _ in input().split()]
# print(len(ls) - len(set(ls)))

# [print(len(nums)-len(set(nums))) for nums in [input().split()]]
