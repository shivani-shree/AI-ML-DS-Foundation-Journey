# TEXT ANALYZER

paragraph = input("Enter your paragraph: ").lower()

keep = []
for char in paragraph:
    if char.isalpha() or char.isspace() or char == "\'":
        keep.append(char)

paragraph_l = ("".join(keep)).split()

# Word Count
word_count = len(paragraph_l)
print(f"Total number of words: {word_count}")

# Unique Words
unique_words = set(paragraph_l)
print(f"Number of unique words: {len(unique_words)}")

# Most common word
freq = {}

for word in paragraph_l:
    freq[word] = freq.get(word, 0) + 1

most_common = max(freq.items(), key = lambda item: item[1])
print(f"Most common word: {most_common[0]}")

# Average word length
word_len = 0

for word in paragraph_l:
    word_len += len(word)

avg_word_len = word_len / word_count

print(f"Average word length: {avg_word_len:.2f}")


