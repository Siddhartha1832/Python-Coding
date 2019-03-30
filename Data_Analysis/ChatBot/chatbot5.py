'''
Install Chatterbot Python module before you run this code
>>> pip install chatterbot
'''

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

'''
ChatterBot’s preprocessors are simple functions that modify the input 
statement that a chat bot receives before the statement gets processed by 
the logic adaper.
'''

chatbot = ChatBot('CHATBOT',
	preprocessors = [
		'chatterbot.preprocessors.clean_whitespace',
		'chatterbot.preprocessors.unescape_html',
		'chatterbot.preprocessors.convert_to_ascii'
		]
	)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

while True:
	try:
		user_input = input("\n User: ")
		if user_input.casefold() == 'quit' or user_input.casefold() == 'bye':
			print(f" CHATBOT: Bye..")
			break
		else:
			print(f" CHATBOT: {chatbot.get_response(user_input)}")
	## Press ctrl-c or ctrl-d on the keyboard to exit
	except(KeyboardInterrupt, EOFError, SystemExit):
		break
