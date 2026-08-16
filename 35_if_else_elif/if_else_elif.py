def route_info (route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']}"
    elif 'speed' in route and 'time' in route:
        return f"Distance to your destination is {route['speed'] * route['time']}"
    else:
        return "No distance info is available"


print(route_info({'distance': 40}))
print(route_info({'my_speed': 30}))
print(route_info({'speed': 50, 'time': 5}))
print(route_info({'distance': 40.5}))
