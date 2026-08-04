# LEADERBOARD PRINTER USING zip() + enumerate()

def print_leaderboard(names, scores):

    names_scores = list(zip(names, scores))
    lead = sorted(names_scores, key=lambda i: i[1], reverse = True)

    for i, person in enumerate(lead, start = 1):
        print(f"{i}. {person[0]} - {person[1]}")

# Sample 1
names = ['Alice', 'Bob', 'Charlie']
scores = [88, 95, 72]
print_leaderboard(names, scores)
print()

# Sample 2
names = ['Dev', 'Ravi', 'Meena', 'Anu']
scores = [50, 90, 90, 60]
print_leaderboard(names, scores)
