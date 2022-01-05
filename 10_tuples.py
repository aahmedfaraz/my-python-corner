# Tuples are Immutable - Cannot be Updated
coordinates = (4, 5)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple)

my_list_of_tuples = [(1, 1), (2, 2), (3, 3)]
print(my_list_of_tuples)
my_list_of_tuples[0] = (11, 11)
print(my_list_of_tuples)

# OUTPUT
# (4, 5)
# 4
# 5
# (1, 2, 3, 4, 5, 6)
# [(1, 1), (2, 2), (3, 3)]
# [(11, 11), (2, 2), (3, 3)]
