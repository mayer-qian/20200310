import json

numbers = [2, 3, 5, 7, 11, 13]
file = 'number.json'
with open(file, 'w') as f_obj:
    json.dump(numbers, f_obj)