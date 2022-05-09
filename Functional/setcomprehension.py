#my_list= [param for param in iterable]

my_set = {char for char in 'hello'}

my_set2 = {num for num in range(100)}

my_set3 = {num*2 for num in range(100)}

my_set4 = {num**2 for num in range(100) if num % 2 == 0}

print(my_set4)
