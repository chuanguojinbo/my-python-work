def get_formatted_name(first,last,middle=''):
	'''generate a neatly formmatted name'''
	if middle:
		fullname=first+' '+middle+' '+last
	else:
		fullname=first+' '+last
	return fullname.title()
