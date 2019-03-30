'''
Install below Python Module before You run this code.
>>> pip install chatterbot 
'''

import os # allow us to work with directories
from chatterbot import ChatBot # methos to train chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot("BOT")

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")

chatbot.set_trainer(ListTrainer)
conversation = [
	"Hello",
	"Hi there!",
	"How are you doing?",
	"I'm doing great.",
	"That is good to hear",
	"Thank you.",
	"You're welcome."
	]
chatbot.train(conversation)

while True:
	try:
		input_string = str(input('\n User: ')) # takes the input of messages typed by user.
		if input_string.casefold() == 'exit' or input_string.casefold() == 'bye':
			print(' Exiting..')
			break
		else:
			response = chatbot.get_response(input_string) # searches the responses for given message.
			print(' Chatbot: {}'.format(response))
	except (KeyboardInterrupt, EOFError, SystemExit):
		break
