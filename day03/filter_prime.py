# USING filter()+lambda TO EXTRACT PRIMES

def prime_check(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def get_primes(nums):
    return list(filter(lambda n: prime_check(n), nums))

nums = list(map(int, input("Enter values for a list: ").split()))
print(get_primes(nums))