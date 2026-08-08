# 1. PYTHAGOREAN TRIPLES UNDER 50

pythagorean_triplets = [(a,b,c) for c in range(1,50) for b in range(1,c) for a in range(1,b) 
                        if c**2 == a**2 + b**2 and a<b<c]
print(pythagorean_triplets)


# 2. DICT COMPREHENSION MAPPING WORDS TO THEIR LENGTHS

sentence = input("Enter a sentence: ").split()
word_length = {word : len(word) for word in sentence}
print(word_length)


# 3. FLATTEN A MATRIX USING NESTED COMPREHENSION

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_matrix1 = [num for row in matrix1 for num in row]
print(list_matrix1)

# Irregular matrix
matrix2 = [[1, 2], [3, 4, 5], [6]]
list_matrix2 = [num for row in matrix2 for num in row]
print(list_matrix2)


# 4. SET COMPREHENSION FOR UNIQUE FILE EXTENSIONS

filenames = ["report.pdf", "photo.jpg", "notes.txt", "data.csv", "image.jpg", "summary.pdf", "readme"]
extension = {file.partition('.')[2] for file in filenames if '.' in file}
print(extension)

