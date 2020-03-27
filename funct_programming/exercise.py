#1 Capitalize all of the pet names and print the list
from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']

def convert_to_upper(item):
    item = str(item)
    return item.upper()

my_pets = list(map(convert_to_upper, my_pets))

print(my_pets)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort() # or sorted(my_numbers)

zip_list = list(zip(my_strings, my_numbers))

print(zip_list)


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def pass_rate(item):
    return item >= 50

new_scores = list(filter(pass_rate, scores))

print(new_scores)


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))