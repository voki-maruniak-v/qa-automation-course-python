new_dict = {}

new_key = input("Enter the key ")
new_content = input("Enter the content ")

new_dict[new_key] = new_content

new_key = input("Enter the key ")
new_content = int(input("Enter the content "))

new_dict[new_key] = new_content

new_key = input("Enter the key ")
new_content = int(input("Enter quantity "))

new_dict[new_key] = new_content

print(new_dict)

new_dict['country'] = 'Germany'

print(new_dict)

del new_dict['quantity']

print(new_dict)
