def route_info (dict):
    if ('distance' in dict) and (type(dict['distance']) == int):
        return f"Distance to your destination is {dict['distance']}"
    elif 'speed' in dict and 'time' in dict:
        return f"Distance to your destination is {dict['speed'] * dict['time']}"
    else:
        return "No distance info is available"


print(route_info({'distance': 40}))
print(route_info({'my_speed': 30}))
print(route_info({'speed': 50, 'time': 5}))
print(route_info({'distance': 40.5}))
