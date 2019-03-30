'''
Install Chatterbot Python module before you run this code
>>> pip install chatterbot
'''

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response

'''
Response selection methods determines which response should be used 
in the event that multiple responses are generated within a logic adapter.

ChatterBot comes with a corpus data and utility module that makes it easy 
to quickly train your bot to communicate.
'''

chatbot = ChatBot('CHATBOT',
	response_selection_method = get_most_frequent_response)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Now we can export the data to a file
trainer.export_for_training('./my_export.json')

# # train data based on the english greetings and conversations 
# trainer.train(
#     "chatterbot.corpus.english.greetings",
#     "chatterbot.corpus.english.conversations"
# )

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
