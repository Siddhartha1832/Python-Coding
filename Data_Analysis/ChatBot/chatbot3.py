'''
Install Chatterbot Python module before you run this code
>>> pip install chatterbot
'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

## adding logic adapters like math, time etc.
chatbot = ChatBot('CHATBOT',
	storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
	logic_adapters = [
		'chatterbot.logic.MathematicalEvaluation',
		'chatterbot.logic.TimeLogicAdapter',
		'chatterbot.logic.BestMatch'
		],
	database_uri = 'sqlite:///chatbot3.sqlite3'
    )

conversation = [ 
	"Hello", 
	"Hi there!", 
	"How are you doing?", 
	"I'm doing great.", 
	"That is good to hear", 
	"Thank you.", 
	"You're welcome."
]

trainer = ListTrainer(chatbot)
# training the chatbot with above conversations.
trainer.train(conversation)

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