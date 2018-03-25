#/usr/bin/env python
#-*-coding:utf-8-*-
import os
import time
source=['/home/chuanguojinbo/文档/python-work/python-practice']
target_dir='/home/chuanguojinbo/backup'
if not os.path.exists(target_dir):
	os.mkdir(target_dir)
today=target_dir+os.sep+time.strftime('%Y%m%d')#日期作为子目录
now=time.strftime('%H%M%S')#时间作为文件夹名称
target=today+os.sep+now+'.zip'
if not os.path.exists(today):
	os.mkdir(today)
	print('successfully created directory today',today)
zip_command='zip -r {0} {1}'.format(target,''.join(source))
print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
	print('successful backup to',target)
else:
	print('backup failed')
