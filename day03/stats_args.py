# STATS FROM UNLIMITED ARGS (*args)

def get_stats(*args):

    if len(args) == 0:
        return {'mean': None, 'min':None, 'max':None}
    
    mean_args = sum(args) / len(args)
    min_args = min(args)
    max_args = max(args)

    return {'mean': mean_args, 'min':min_args, 'max':max_args}

# Sample Cases
print(get_stats(1,2,3))
print(get_stats(4, 8, 15, 16, 23, 42))
print(get_stats(10))
print(get_stats())