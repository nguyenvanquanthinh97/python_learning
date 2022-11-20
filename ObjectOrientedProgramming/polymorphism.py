class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("sign in")

    def attack(self):
        print("Do nothing!")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard("Merlin", 50, "merlin@email.com")
archer1 = Archer("Robin", 50, "robin@email.com")

def invoke_player_attack(*args):
    # We apply polymorphism in here
    # The Wizard class and User class all inheritance from class User
    # Class User already define attack method and those 2 classes override it
    # So it means Wizard and User instances always have attack method
    # Each class has its attack version by overriding attack base method from class User
    for player in args:
        player.attack()


invoke_player_attack(wizard1, archer1)