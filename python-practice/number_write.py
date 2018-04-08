import json
a=[2*x-1 for x in range(1,7)]
print(a)
file_name='numbers.json'
with open(file_name,'w') as f_object:
	json.dump(a,f_object)
