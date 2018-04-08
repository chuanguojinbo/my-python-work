#coding:utf-8
import json

#如果有json文件就直接读取
def get_stored_username():
	'''重构'''
	filename='username.json'
	try:
		with open(filename) as f_obj:
			username=json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

#如果没有json文件就创建并且储存一个
def get_new_username():
	filename='username.json'
	username=input('Please enter your name: ')
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username

#根据是否存在json文件打不一样的招呼
def greet_user():
	username=get_stored_username()
	if username:
		print('Welcome back, '+username+'!')
	else:
		username=get_new_username()
		print('We will remember you when you come back, '+username+'!')

greet_user()
		
