def highes_even(lista):
    for numero in lista:
        if(numero % 2 == 0):
            npar = numero
            if(numero > npar):
                npar = numero
            pass
    return npar


lista = [1, 2, 3, 4, 6, 8, 10, 101]
resultado = highes_even(lista)
print(resultado)
x = int(5)
print(x)
