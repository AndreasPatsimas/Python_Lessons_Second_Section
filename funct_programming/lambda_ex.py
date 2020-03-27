#square
import math

my_list = [5,4,3]

print( list( map( lambda item: int( math.pow(item, 2 ) ), my_list ) ) )

#sort based on second number

a = [(0,2), (4,3), (9,9), (10, -1)]

a.sort(key=lambda item: tuple(item).__getitem__(1))

print(a)