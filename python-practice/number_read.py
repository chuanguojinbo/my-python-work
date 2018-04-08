import json
file_name='numbers.json'
with open(file_name,'r') as f_obj:
	numbers=json.load(f_obj)
print(numbers)