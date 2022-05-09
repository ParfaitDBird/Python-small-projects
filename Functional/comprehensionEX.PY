lista = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
'''
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
for letra in lista:
  if(lista.count(letra)>1):
    lista.remove(letra)
print (sorted(lista))
'''
# my_list4 = [num**2 for num in range(100) if num % 2 == 0]item

duplicates = list(set([item for item in lista if(lista.count(item) > 1)]))
print(duplicates)
