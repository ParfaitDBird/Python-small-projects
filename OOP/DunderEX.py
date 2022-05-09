class SuperList(list):
    def __len__(self):
        return 1000


superlist1 = SuperList()

print(len(superlist1))
print(superlist1.append(5))
print(len('hola'))
