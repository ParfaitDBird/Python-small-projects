while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except ValueError:
        print('Please write a number you asshole')
    except ZeroDivisionError:
        print('Stop lying asshole number should be higher than 0')
    else:
        print('Thanks!')
        break
