my_range = range(0, 10)

print(type(my_range), my_range)
print(list(my_range))

my_new_range = range(5, 16)
print(list(my_new_range))

my_range_with_step = range(0, 11, 2)
print(list(my_range_with_step))

my_second_range_with_step = range(10, 0, -1)
print(list(my_second_range_with_step))

print(type(my_second_range_with_step))

print(my_second_range_with_step[0])
print(my_second_range_with_step[2])
print(my_second_range_with_step[-1])
