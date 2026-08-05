# FUNCTION DATA PIPELINES

from functools import reduce

def data_filter(raw_data):

    valid = list(filter(lambda x: is_number(x), raw_data))
    valid_nums = list(map(lambda x: float(x.strip()), valid))
    print(f"Cleaned numbers: {valid_nums}")

    total_nums = reduce(lambda x,y: x+y, valid_nums, 0)
    print(f"Sum: {total_nums}")

    try:
        avg = total_nums / len(valid_nums)
        print(f"Average: {avg}")
    except ZeroDivisionError:
        print(f"Average: None")
    

def is_number(n):

    try:
        float(n.strip())
        return True    
    except ValueError:
        return False

data_filter(['12', '7', 'abc', '45.5', '', 'nine', '3', '-2', '  8  '])
data_filter(['1.2.3', '--5', '12-3', '.', '-'])