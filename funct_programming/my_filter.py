def only_odd(item):
    return item % 2 !=0

new_list = list(filter(only_odd, [0,1,2,3,4,5,6,7,8,9]))

print(new_list)