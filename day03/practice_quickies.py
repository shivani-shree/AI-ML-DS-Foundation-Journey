# 1. CONFIG DICTIONARY VIA **kwargs

def build_config(env = 'dev',debug = False, verbose = False, **kwargs):

    d = {'debug':debug, 'verbose':verbose, 'env':env} | kwargs
    return d

print(build_config(env='prod', timeout=30))
print(build_config())
print(build_config(debug=True, region='us-east'))


# 2. USING map()+lambda TO SQUARE ALL THE ELEMENTS

def square_all(nums):
    return list(map(lambda n: n**2, nums))

nums = list(map(int, input("Enter some numerical values: ").split()))
print(square_all(nums))


# 3. CLOSURE THAT MAINTAINS A RUNNING TOTAL

def make_counter():
    total = 0

    def add(n):
        nonlocal total
        total += n
        return total

    return add

counter = make_counter()
print(counter(5))   
print(counter(3))   
print(counter(10))  

counter2 = make_counter()
print(counter2(100))


# 4. USING zip() TO COMBINE THREE LISTS INTO LIST OF TUPLES

def combine_three(list1, list2, list3):
    return list(zip(tuple(list1), tuple(list2), tuple(list3)))

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NY', 'LA', 'SF']

print(combine_three(names, ages, cities))
print(combine_three(['A', 'B', 'C'], [1, 2], ['X', 'Y', 'Z']))


# 5. COVERTING A FOR LOOP BASED DATA PIPELINE INTO CHAINED map/filter/reduce

from functools import reduce

def process_pipeline(nums):

    positive = list(filter(lambda n: n >= 0, nums))
    double = list(map(lambda n: n*2, positive))
    total = reduce(lambda x,y: x+y, double,0)

    return total

nums = list(map(int, input("Enter values of a list: ").split()))
print(f"Total: {process_pipeline(nums)}")



