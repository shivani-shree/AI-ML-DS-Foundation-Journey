# 1. REVERSE A STRING WITHOUT USING [::-1]

s = input("Enter a string: ")
reverse_s = ''

for i in range(len(s) - 1, -1, -1):
    reverse_s += s[i]

print(f"Reversed string: {reverse_s}")


# 2. REMOVE DUPLICATES FROM A LIST WHILE PRESERVING THE ORDER

initial = list(map(int, input("Enter values for the list: ").split()))
seen = set()
final = []

for i in initial:
    if i not in seen:
        seen.add(i) # O(1) lookup time
        final.append(i)

print(f"Updated List: {final}")


# 3. FIND THE MOST FREQUENT ELEMENT IN THE LIST

nums = list(map(int, input("Enter values for the list: ").split()))

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

max_freq = max(freq.items(), key = lambda item: item[1])

print(f"The number with maximum frequency is {max_freq[0]}")


# 4. MERGE TWO DICTIONARIES

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = dict1 | dict2
print(merged_dict)

# Method 2
merge_dict = dict(dict1)
for key in dict2:
    merge_dict[key] = dict2[key]
print(merge_dict)


# 5. INTERSECTION AND SYMMERTIC DIFFERENCE OF TWO SETS

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(f"Intersection: {set1 & set2}")
print(f"Symmetric Difference: {set1 ^ set2}")


# 6. SORT A LIST OF TUPLES BY THE SECOND ELEMENT

list_of_tuples = [(1, 5), (2, 2), (3, 8), (4, 1)]
sorted_list = sorted(list_of_tuples, key = lambda x: x[1])
print(sorted_list)


# 7. COUNT VOWELS/CONSONANTS IN A STRING USING DICTIONARY
s = input("Enter a String: ")
vowels = {'a','e','i','o','u'}
d = {'vowels':0, 'consonants':0}

for char in s:
    if char.isalpha():
        if char.lower() in vowels:
            d['vowels'] += 1
        else:
            d['consonants'] += 1

print(f"Number of Vowels: {d['vowels']}")
print(f"Number of Consonants: {d['consonants']}")



