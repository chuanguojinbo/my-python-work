import unittest
from survey import AnonymousSurvey
#重构代码
class TestAnonymousSurvey(unittest.TestCase):
	'''针对AnonymousSurvey类的测试'''

	def setUp(self):
		'''

		创建一个调查对象和一组答案，供使用的测试方法使用
		'''
		question='what is your favorite language?'
		self.my_survey=AnonymousSurvey(question)
		self.responses=['Python','C','Java']

	def test_store_single_response(self):
		'''测试单个答案是否会被妥善储存'''
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)

	def test_store_three_response(self):
		'''测试三个答案是否会被妥善存储'''
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)

unittest.main()