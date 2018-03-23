#/usr/bin/env python
#-*-coding:utf-8-*-
import os 
import time
source=['/home/chuanguojinbo/backup/readme']#需要备份的文件和目录，放在一个列表中（list）
target_dir='/home/chuanguojinbo/backup'#这个是备份文件的储存地址
target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'
#备份文件将打包压缩成zip格式，文件名将根据当前时间和日期构成，加上‘.zip’扩展名
#os.sep根据操作系统给出相应的分隔符，存储在target_dir目录中
if not os.path.exists(target_dir):#如果用于储存的地址不存在
	os.mkdir(target_dir)#则创建新的地址
zip_command='zip -r {0} {1}'.format(target,' '.join(source))
#以上使用zip命令将文件打包成zip格式
#-r用于指定将zip命令应用于所有的子文件夹和其中的文件
#后面跟着的是将要创建的zip文件的名称
#再后面是需要备份的文件和目录的地址
#join函数用于在储存地址和原地址之间添加空格，并通过format函数将其转化成字符串
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:#os.system命令可以在shell中执行zip_command,
	print('successful backup to',target)#如果执行成功则返回0，失败则返回一个错误代码
else:
	print('backup failed')
