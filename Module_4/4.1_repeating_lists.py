list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g']
list3 = list1 + list2
print(list3)

zeros = [0] * 10
print(len(zeros))  #10

# Что выведет следующий код?

numbers = [10, 20, 30, 40, 50]
print(numbers[-2])
print(numbers[-4:-1])   #40[20, 30, 40]

# Что выведет следующий код?

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2:5])
print(numbers[:4])
print(numbers[3:])

# [30, 40, 50]
# [10, 20, 30, 40]
# [40, 50, 60, 70, 80]

numbers = [4, 8, 12, 16, 34, 56, 100]
numbers[1:4] = [20, 24, 28]
print(numbers)

# [4, 20, 24, 28, 34, 56, 100]

numbers = [5, 10, 15, 25]
print(numbers[::-2])

# [25, 10]

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)

numbers.append(60)
print(numbers)

# [10, 20, 30, 40, 50, 60]
# [10, 20, 30, 40, 50, 60, 60]

numbers = [10, 20, 30, 40, 50]
numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)

# [10, 20, 30, 40]
# [10, 20, 40]

letters = ['a', 'b', 'c', 'd']
new_letters = list(letters)
new_letters1 = letters[:]
new_letters2 = letters.copy()
print(new_letters)
print(new_letters1)
print(new_letters2)

words = ['Hello', 'Python']
print('-'.join(words))  # Hello-Python


numbers = [10, 20, 30, 40]
del numbers[0:6]
print(numbers) # []

words = ['xyz', 'zara', 'beegeek']
print(max(words))   # zara


numbers = [1, 2, 3, 4, 5, 6, 7]
new_numbers = [2 * x for x in numbers]
print(new_numbers)