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

print(wizard1.email)

wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(wizard1, Archer))

# introspection - the ability to determine the type of object at runtime
print(dir(wizard1))

