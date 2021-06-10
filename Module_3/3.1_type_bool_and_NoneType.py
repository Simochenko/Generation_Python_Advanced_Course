# # Что будет выведено на экран в результате выполнения следующей программы?
#
# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)
#
# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#
#     res = res + (num % 2 == 1 and num > 1)
# print('res ', res) # 5 res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
#
# # то же самое, что и следующий код
#
# res = 0
# for num in numbers:
#     if (num % 2 == 1) and (num > 1):
#         res += 1
#

# объявление функции
# def func(num1, num2):
#     if num1 % num2 == 0:
#         return True
#
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# if func(num1, num2):
#     if func:
#         print("делится")
# else:
#     print("не делится")
#
# ''' Предикат делимости '''
# def func(num1, num2):
#     return not num1 % num2
#
#
# print(f"{'не ' * (not func(int(input()), int(input())))}делится")

