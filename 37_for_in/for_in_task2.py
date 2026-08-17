def filter_list(arg, value_type):
    new_list = []
    for element in arg:
        if type(element) == value_type:
            new_list.append(element)
    return new_list

print(filter_list([35, True, 'abc', 10], int))
print(filter_list([True, False, False, 'abc', 123], bool))
print(filter_list([True, False, False, 'abc', 123], str))
