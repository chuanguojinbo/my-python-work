import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	'''针对AnonymousSurvey类的测试'''

	def test_store_single_response(self):
		'''测试单个答案会被妥善储存'''
		question='what is your favorite language?'
		my_survey=AnonymousSurvey(question)
		my_survey.store_response('English')

		self.assertIn('English',my_survey.responses)

	def test_store_three_responses(self):
		'''测试三个答案是否被妥善储存'''
		question='what is your favorite language?'
		my_survey=AnonymousSurvey(question)
		responses=['PYthon',"C","Java"]
		for response in responses:
			my_survey.store_response(response)
		for response in responses:
			self.assertIn(response,my_survey.responses)

unittest.main()