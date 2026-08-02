# NUMBER DETECTIVE

number = int(input("Enter a number: "))


# TO CHECK IF IT IS EVEN OR ODD
print(f"{number} is an {'even' if number % 2 == 0 else 'odd'} number")


# TO CHECK IF IT IS PRIME OR NOT
if number <= 1:
    print(f"{number} is not a prime number")

else:
    is_prime = True
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


# TO CHECK IF IT IS A PERFECT SQUARE OR NOT
if number < 0:
    print(f"{number} is not a perfect square number")
else:
    root = int(number ** 0.5)
    print(f"{number} is {'perfect square' if root*root == number else 'not a perfect square'} number")


# ARMSTRONG NUMBER
if number < 0:
    print(f"{number} is not an Armstrong number")
else:
    digits = str(number)
    power = len(digits)
    total = sum(int(i)**power for i in digits)
    print(f"{number} is {'an Armstrong' if total == number else 'not an Armstrong'} number")


# PALINDROME NUMBER
if number < 0:
    print(f"{number} is not a Palindrome number")
else:
    print(f"{number} is {'a Palindrome' if str(number) == str(number)[::-1] else 'not a Palindrome'} number")

