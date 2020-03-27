class SuperList(list):
    def __len__(self):
        return 1000

    pass

my_super_list = SuperList()
my_super_list.append(5)
print(my_super_list)
print(len(my_super_list))