# LOOP BASED TASKS USING map()/filter()

# 1. SQUARE EVERY NUMBER IN A LIST
nums = [1, 2, 3, 4, 5]

# loop version
squares_loop = []
for num in nums:
    squares_loop.append(num ** 2)

# map() version
squares_map = list(map(lambda num: num ** 2,nums))

assert squares_loop == squares_map, "They do not match!"
print(f"SQUARING:\nBefore: {nums} -> After: {squares_map}")
print()


# 2. FILTER OUT EVEN NUMBERS FROM A LIST
nums = [10, 15, 22, 33, 40, 7, 8]

# loop version
even_loop = []
for num in nums:
    if num % 2 == 0:
        even_loop.append(num)

# filter() version
even_filter = list(filter(lambda num: num % 2 == 0, nums))

assert even_loop == even_filter, "They do not match!"
print(f"FILTERING EVEN NUMBERS:\nBefore: {nums} -> After: {even_filter}")
print()


# 3. CONVERT A LIST OF STRINGS TO UPPERCASE
s = ['python', 'is', 'fun']

# loop version
upper_loop = []
for word in s:
    upper_loop.append(word.upper())

# map() version
upper_map = list(map(lambda word: word.upper(), s))

assert upper_loop == upper_map, "They do not match!"
print(f"CONVERTING LIST OF STRINGS TO UPPERCASE:\nBefore: {s} -> After: {upper_map}")
print()


# 4. GET LENGTH OF EVERY STRING
words = ['data', 'science', 'ai', 'ml']

# loop version
len_loop = []
for word in words:
    len_loop.append(len(word))

# map() version
len_map = list(map(lambda word: len(word), words))

assert len_loop == len_map, "They do not match!"
print(f"LENGTH OF EVERY STRING:\nWords: {words} -> Words_Length: {len_map}")
print()


# 5. FILTER OUT WORDS LONGER THAN 4 CHARACTERS
words = ['cat', 'python', 'ai', 'machine', 'ml', 'data']

# loop version
long_loop = []
for word in words:
    if len(word) <= 4:
        long_loop.append(word)

# filter() version
long_filter = list(filter(lambda word: len(word) <= 4, words))

assert long_loop == long_filter, "They do not match!"
print(f"FILTERING WORDS WHOSE LENGTH IS GREATER THAN 4:\nBefore: {words} -> After: {long_filter}")
print()