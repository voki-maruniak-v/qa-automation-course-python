import json

new_dict = {"Name": "Vadya", "age": 30, "itIsOld": True}

json_str = json.dumps(new_dict, indent=1)

print(json_str)
print(type(json_str))

new_json_dict = json.loads(json_str)
print(new_json_dict)
print(type(new_json_dict))
