#pip install nltk - install nltk module in command prompt.
#nltk.download() - use after install nlk modul in python shell.
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

print("\n Natural Language Processing - NLTK using Python")
example_text = "Hello Mr. Eminem, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

sentence_tokens = sent_tokenize(example_text)
word_tokens = word_tokenize(example_text)
stop_words = set(stopwords.words('english'))

filtered_sentence = [w for w in word_tokens if w not in stop_words]

print("\n Using String Split() : {}".format(example_text.split(' ')))
print("\n Sentence Tokenize : {}".format(sentence_tokens))
print("\n Word Tokenize : {}".format(word_tokens))
print("\n Stop Words : {}".format(stop_words))
print("\n After Filtering Stop_Words from sentence : {}".format(filtered_sentence))
