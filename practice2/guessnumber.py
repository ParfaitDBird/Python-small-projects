from random import randint
import sys
mini = sys.argv[1]
mx = sys.argv[2]
numero = randint(int(mini), int(mx))
print(numero)
while True:
    try:
        guess = int(input(f'Write a number between {mini} - {mx} : '))
        if guess == numero:
            print('You won!')
            break
        else:
            print('Try again =]')
    except ValueError:
        print('Please write a number you asshole')
        
