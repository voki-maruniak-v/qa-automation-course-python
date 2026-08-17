def dict_to_list (arg):
    list_convert = []
    for k, v in arg.items():
        if type(v) == int:
            v *= 2
        list_convert.append((k, v))
    return list_convert

print(dict_to_list({"id": 345}))
