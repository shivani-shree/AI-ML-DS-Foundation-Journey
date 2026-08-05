# FACTORIAL VIA reduce()

from functools import reduce

def factorial(n):
    if n == 0:
        return 1
    factorial_list = [x for x in range(n, 0, -1)]
    return reduce(lambda x,y: x*y, factorial_list)

n = int(input("Enter the number: "))
print(factorial(n))