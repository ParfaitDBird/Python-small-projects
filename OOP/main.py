# Private sadly they do not exist here so please be respectful of the _ in the vars ;)
class PlayerCharacter():
    # Class Object Attribute
    membership = True

    def __init__(self, name='Anonymous', age=0):
        # if (age > 18):
        self._name = name  # Constructor attributes
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(
            f'My igt is {self._name} and I am {self._age} years old and stfu')

    @classmethod  # Decorator
    def adding_things(cls, num1, num2):
        return num1+num2


player1 = PlayerCharacter('Lietail', 20)
#print(player1.adding_things(2, 7))
player1.speak()
