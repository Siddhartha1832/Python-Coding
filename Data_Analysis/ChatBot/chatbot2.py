'''
Install Chatterbot Python module before you run this code
>>> pip install chatterbot
'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('CHATBOT',
	storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
	database_uri = 'sqlite:///chatbot2.sqlite3'
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
	except(KeyboardInterrupt, EOFError, SystemExit):
		break