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


