# REWRITING 5 LOOP-BASED LIST BUILDING TASKS IN COMPREHENSIONS

# 1. Square of numbers 

nums = list(map(int, input("Enter values for list: ").split()))

# loop version
squared_nums_loop = []
for num in nums:
    squared_nums_loop.append(num ** 2)

# list comprehension version
squared_nums = [num**2 for num in nums]
print(f"SQUARE OF NUMBERS: {squared_nums}")


# 2. Even numbers

nums = list(map(int, input("Enter values for list: ").split()))

# loop version
even_numbers_loop = []
for num in nums:
    if num % 2 == 0:
        even_numbers_loop.append(num)

# list comprehension version
even_numbers = [num for num in nums if num % 2 == 0]
print(f"EVEN NUMBERS: {even_numbers}")


# 3. Uppercase Words
words = ["hello", "world", "python", "code"]

# loop version
words_upper_loop = []
for word in words:
    words_upper_loop.append(word.upper())

# list comprehension version
words_upper = [word.upper() for word in words]
print(f"UPPERCASE CONVERSION: {words_upper}")


# 4. String lengths
words = ["apple", "fig", "banana", "kiwi", "pomegranate"]

# loop version
words_len_loop = []
for word in words:
    words_len_loop.append(len(word))

# list comprehension version
words_len = [len(word) for word in words]
print(f"WORDS LENGTH: {words_len}")


# 5. filter() + transform 
nums = [4, -2, 7, -9, 15, -1, 22]

# loop version
positive_double_loop = []
for num in list(filter(lambda x: x > 0, nums)):
    positive_double_loop.append(num * 2)

# list comprehension version
positive_double = [num*2 for num in list(filter(lambda x: x > 0, nums))]
print(f"POSITIVE SQUARES: {positive_double}")