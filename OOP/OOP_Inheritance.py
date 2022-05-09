class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        #User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"arrows left {self.num_arrows-1}")


wizard1 = Wizard('Merlin', 50, 'CokWizard@Bustermeme.ck')
archer1 = Archer('Emiya', 68)
archer1.attack()
print(isinstance(wizard1, User))
