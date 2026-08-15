def image_info(parameters):
    if ('image_id' not in parameters) or ('image_title' not in parameters):
        print(parameters)
        raise TypeError("Keys image_id and image_title must be present")
        
    print(parameters)    
    return f"Image {parameters['image_title']} has id {parameters['image_id']} "
    

try:
    print(image_info({'image_id': 453, 'image_title': 'Dog'}))
except TypeError as e:
    print(e)

print()    

try:
    print(image_info({'name': 'Vadya'}))
except TypeError as e:
    print(e)
