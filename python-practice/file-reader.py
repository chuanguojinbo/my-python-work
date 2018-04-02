#/usr/bin/env python
#coding:utf-8
file_path='/home/chuanguojinbo/文档/python-work/inheritance.py'
with open(file_path) as file_object:
	lines=file_object.readlines()#将文件的各行储存在一个列表中，可以在with代码块之外使用
py_string=''
for line in lines[:4]:
	py_string+=line.strip()
print(py_string)
print(len(py_string))
