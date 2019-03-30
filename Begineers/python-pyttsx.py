'''
Install below Python Module before You run this code.
>>> pip install pyttsx3 
# Pyttsx is a Good Text-to-Speech Conversion library in python 
'''

import pyttsx3
engine = pyttsx3.init() # create pyttsx engine instance
input_text = input('\n Enter Text to Convert into Speech : ')
engine.say(input_text) # The speech is output according to the properties set before this command in the queue.
engine.runAndWait() # Blocks while processing all currently queued commands.
print('\n Thank you!')