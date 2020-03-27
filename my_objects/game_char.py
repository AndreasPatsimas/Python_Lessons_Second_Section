class GameCharacter: #camelcase in name of classes
    def __init__(self, name = "anonymous", age = 0):
        if age > 18:
            self.name = name
            self.age = age

    def attack(self):
        print("Attack!!!!")

    @staticmethod #use this method wthout instatiation
    def add_things(num1, num2):
        return num1 + num2

    @classmethod#use this method wthout instatiation
    def dif_instant(cls, name, bitrh_year):
        return cls(name, 2020 - bitrh_year)


player1 = GameCharacter("Andreas", 27)

print("{} is {} years old. He is a champion son of the bitches!!".format(player1.name, player1.age))

player1.attack()

player2 = GameCharacter(age = 20)

print("{} is {} years old. He is a mother fucker!!".format(player2.name, player2.age))

print(GameCharacter.add_things(2, 3))

player3 = GameCharacter.dif_instant("Sotiris", 1997)

print("{} is {} years old. He is a champion son of the bitches!!".format(player3.name, player3.age))


# Class method vs Static Method
#
# * A class method takes cls as first parameter while a static method needs no specific parameters.
# * A class method can access or modify class state while a static method can’t access or modify it.
# * In general, static methods know nothing about class state. They are utility type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as parameter.
# * We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
#
#
#
# When to use what?
#
# * We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases.
# * We generally use static methods to create utility functions.