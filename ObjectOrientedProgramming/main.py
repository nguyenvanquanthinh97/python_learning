# OOP
class PlayerCharacter:
    membership = True  # static attributes

    def __init__(self, name="Anonymous", age=0):
        if PlayerCharacter.membership:
            self.name = name  # attributes
            self.age = age  # attributes

    def run(self):
        print(f'{self.name} run')

    def implement_in_future(self):
        pass

    @classmethod
    # cls - class
    # use class method when you need to access class to do something
    # And it is not common use
    def adding_things(cls, num1, num2):
        return cls("Anonymous", num1 + num2)

    @staticmethod
    # it's already clear by its name - use it when you don't care much about instance attributes
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter()
player2 = PlayerCharacter("John", 26)
player2.attack = 50

print(player2.attack)
player2.run()

player1.run()

player3 = PlayerCharacter.adding_things(10, 9)
print(f'Age of player3: {player3.age}')

