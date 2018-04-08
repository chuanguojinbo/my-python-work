from survey import AnonymousSurvey

#设定问题，创建一个新的实例
question='what is your favorite language?'
my_survey=AnonymousSurvey(question)

#先输出问题
my_survey.show_question()

#储存回答
while True:
	response=input('Language: ')
	if response=='q':
		break
	else:
		my_survey.store_response(response)

#输出问题和答案
print('\nThanks to everyone who participated the survey.')
my_survey.show_results()
