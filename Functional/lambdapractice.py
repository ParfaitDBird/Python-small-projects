from functools import reduce
'''
LAMBDA FUNCTIONS
Are one time anonymous functions
order used: lambda param: action(param)
'''

my_list = [1, 2, 3, 4, 5]
your_list = [6, 7, 8, 9, 10]


def accumulator(acc, item):
    return acc + item


# Map example
print(list(map(lambda item: item*2, my_list)))

# Filter example
#print(list(filter(Only_Odd, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))

# zip example
print(list(zip(my_list, your_list)))

# Reduce example
print(reduce(lambda accumulator, item: accumulator + item, my_list, 0))
