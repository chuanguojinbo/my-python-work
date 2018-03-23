import sys
print('the command-line arguments are:')
for i in sys.argv:
	print(i)
	print('\n')

print('\n\nTHE PYTHON PATH IS :',sys.path,'\n')
print('------------------------------')
import os
print(os.getcwd())
#check the location of this program