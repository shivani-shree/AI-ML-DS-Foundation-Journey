# MINI CALCULATOR + CHECKER FOR TWO NUMBERS
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print()

# PERFORMING ALL ARITHMETIC OPERATIONS
print("ARITHMETIC OPERATIONS")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")  #Returns the result in integer form
print(f"Modulo: {a} % {b} = {a % b}")  #Returns the remainder after performing division
print(f"Exponentiation: {a} ** {b} = {a ** b}")

print()


# PERFORMING ALL COMPARISON OPERATIONS
print("COMPARISON OPERATIONS")
print(f"{a} == {b} -> {a == b}")
print(f"{a} != {b} -> {a != b}")
print(f"{a} > {b} -> {a > b}")
print(f"{a} < {b} -> {a < b}")
print(f"{a} >= {b} -> {a >= b}")
print(f"{a} <= {b} -> {a <= b}")

print()

#PERFORMING LOGICAL OPERATIONS
print("LOGICAL OPERATIONS")
if a>0 and b>0:
    print("Both are positive!")

if a>0 or b>0:
    print("Atleast one number is positive!")

if not a:
    print("First number is zero!")
else:
    print("First number is non zero!")

print()

# USING BITWISE OPERATORS
print("BITWISE OPERATIONS")
print(f"Bitwise AND: {a} & {b} = {a & b}")
print(f"Bitwise OR: {a} | {b} = {a | b}")
print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
print(f"Left Shift: {a} << {b} = {a << b}")
print(f"Right Shift: {a} >> {b} = {a >> b}")

print()

# USING ASSIGNMENT OPERATORS
c = a

print(f"Initially c = {c}")

c += b
print(f"c += b -> c = {c}")

c *= 2
print(f"c *= 2 -> c = {c}")

c //= 3
print(f"c //= 3 -> c = {c}")

      















