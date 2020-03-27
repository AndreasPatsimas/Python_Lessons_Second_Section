class Human:
    def __init__(self, name, age, height):
        self._name = name #private
        self._age = age #private
        self.height = height #public

    def walk(self):
        print("Walk")


class Footballer(Human):
    def __init__(self, team, name, age, height):
        super().__init__(name, age, height)
        self.team = team

    def shoot(self):
        print("Scores goal")

    def describe(self):
        print("My height is {} and my team is {}"
              .format(self.height, self.team)) # here i cannot touch name and age because they are private in super class

class Basketballer(Human):
    def shoot(self):
        print("Scores")

    def guard(self):
        print("guard")

    pass

footballer = Footballer(name="Patsimas", age=27, height=1.78, team="Aris")
# footballer.walk()
# footballer.shoot()
footballer.describe()

basketballer = Basketballer(name="Bolosis", age=29, height=1.85)

for char in [footballer, basketballer]:
    char.shoot()
    pass

class Fan(Footballer, Basketballer):
    def __init__(self, name, age, height, team):
        Footballer.__init__(self, team, name, age, height)

    def shout(self):
        print("Aris Ole!")

    def __str__(self):
        return "height: {}, team: {}".format(self.height, self.team)

    pass

fan = Fan(name="S.Patsimas", age=23, height=1.78, team="Aris")

print(fan)
fan.describe()
fan.guard()
fan.walk()