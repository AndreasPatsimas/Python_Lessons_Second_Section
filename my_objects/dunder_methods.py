class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "YO",
            "is_brand": False
        }

    def __str__(self):
        return "Toy -> color: {}, age: {}".format(self.color, self.age)

    def __call__(self):
        return "yes??"

    def __getitem__(self, item):
        return self.my_dict[item]

    pass

toy = Toy("yellow", 5)
print(toy.__str__())

#del toy

print(toy)

print(toy())

print(toy.__getitem__("name"))