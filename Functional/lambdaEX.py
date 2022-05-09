my_list = [5, 4, 3]
# square pow my list using lambda
print(list(map(lambda item: item*item, my_list)))
# sorting based on the second value. (10,-1) will be first cuz -1

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#print(list(zip(sorted(my_numbers), my_strings)))
print(list(sorted(a, key=lambda item: item[1])))
