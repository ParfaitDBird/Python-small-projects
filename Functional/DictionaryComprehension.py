simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}

# ITEM IS THE KEY AND THE ITEM * 2 IS THE VALUE

my_dict2 = {item: item*2 for item in [1, 2, 3]}

print(my_dict2)
