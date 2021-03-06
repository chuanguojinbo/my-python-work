#coding:utf-8
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	'''测试name_function.py'''
	def test_first_last_name(self):
		'''能够正确处理想janis joplin这样的姓名吗'''
		formatted_name=get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

	def test_first_last_middle_name(self):
		formatted_name=get_formatted_name('chao','jin','dajiba')
		self.assertEqual(formatted_name,'Chao Dajiba Jin')


unittest.main()