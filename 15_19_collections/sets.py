my_first_set = {2, 4, 6, 6, 8}

print("Type of my_first_set is", type(my_first_set))

my_first_set.add(10)

print(my_first_set)

my_second_set = {1, 3, 5, 6, 7, 8}

my_third_set = my_first_set.intersection(my_second_set)
print(my_third_set)

my_list = list(my_third_set)

print(type(my_list))
print(my_list)
