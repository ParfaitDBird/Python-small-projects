from functools import reduce

my_list = [1, 2, 3, 4, 5]
your_list = [6, 7, 8, 9, 10]
# map - filter - zip - reduce


def Multyply_By2(item):
    return item*2


def Only_Odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


# Map example
print(list(map(Multyply_By2, my_list)))

# Filter example
print(list(filter(Only_Odd, my_list)))

# zip example
print(list(zip(my_list, your_list)))

# Reduce example
print(reduce(accumulator, my_list, 0))
