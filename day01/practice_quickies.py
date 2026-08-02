# 1. SWAP TWO VARIABLES (INTEGERS) WITHOUT A TEMP VARIABLE

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
orig_a, orig_b = a, b

print(f"Before swapping: a = {a} and b = {b}")

# USING TUPLE UNPACKING METHOD 
a,b = b,a
print(f"Tuple Method: a = {a} and b = {b}")


# USING ARITHMETIC METHOD
a, b = orig_a, orig_b
a = a + b
b = a - b
a = a - b
print(f"Arithmetic Method: a = {a} and b = {b}")

# USING XOR METHOD
a, b = orig_a, orig_b
a = a ^ b
b = a ^ b  # a ^ b ^ b -> a
a = a ^ b
print(f"XOR Method: a = {a} and b = {b}")


# 2. TERNARY EXPRESSION TO FIND MAX OF 3 NUMBERS
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

maximum = a if (a >= b and a >= c) else b if (b >= a and b >= c) else c
print(f"Maximum of three: {maximum}")

# 3. LEAP YEAR
year = int(input("Enter the year: "))


if year % 4 == 0:
    if year % 400 == 0:
        print("Leap Year!")
    elif year % 100 == 0:
        print("Not a Leap Year!")
    else:
        print("Leap Year!")
else:
    print("Not a Leap Year!")


# 4. CELSIUS <-> FAHRENHEIT CONVERTER

choice = int(input('''Enter Your Choice
1. Celcius to Fahrenheit
2. Fahrenheit to Celcius
Choice: '''))

if choice == 1:
    celcius = float(input("Enter the Temperature in Celcius: "))
    fahrenheit = (celcius * (9/5)) + 32
    print(f"Celcius: {celcius:.2f} -> Fahrenheit: {fahrenheit:.2f}")

elif choice == 2:
    fahrenheit = float(input("Enter the Temperature in Fahrenheit: "))
    celcius = (fahrenheit - 32) * (5/9)
    print(f"Fahrenheit: {fahrenheit:.2f} -> Celcius: {celcius:.2f}")

else:
    print("Invalid Choice!")

# 5. MULTIPLICATION TABLE USING FORMATTED STRINGS

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# 6. PALINDROME CHECK

num = int(input("Enter a number: "))

if num < 0:
    print(f"{num} is not a Palindrome number")
else:
    print(f"{num} is {'a Palindrome' if str(num) == str(num)[::-1] else 'not a Palindrome'} number")





    

