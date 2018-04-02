#coding:utf-8
filename='programming.txt'
with open(filename,'a') as file_object:#以写入的方式打开文件，如果文件不存在就创建一个
	file_object.write('\nI also love C-language')#写入内容会覆盖原有内容
'''有'w','r','a','r+'，默认只读'''