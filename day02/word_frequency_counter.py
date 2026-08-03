# WORD FREQUENCY COUNTER

def freq_counter(sentence):

    sentence_list = sentence.split()
    freq = {}
    for word in sentence_list:
        freq[word] = freq.get(word, 0) + 1

    return freq

sentence = input("Enter a sentence: ").lower()

kept_char = []
for char in sentence:
    if char.isalpha() or char.isspace() or char == "\'":
            kept_char.append(char)

sentence = "".join(kept_char)

print(freq_counter(sentence))

