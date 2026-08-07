my_nums = (10, 5, 100, 0, 40, 5, 0)

print(type(my_nums), my_nums)

print(my_nums.count(5))
print(my_nums.count(7))

print(my_nums.index(0))

my_list = [1, 3, 4, 4, 5, 11, 14, 4]

print(my_list)

my_tuple_list = tuple(my_list)

print(type(my_tuple_list), my_tuple_list)

print(my_tuple_list.index(4))

index_one = my_tuple_list.index(4)
print(my_tuple_list.index(4, index_one + 1))

index_two = my_tuple_list.index(4, index_one + 1)
print(my_tuple_list.index(4, index_two + 1))