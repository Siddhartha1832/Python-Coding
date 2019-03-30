'''
Install below Python Module before You run this code.
>>> pip install oxforddictionaries 
# API Base URL - https://od-api.oxforddictionaries.com/api/v1

'''

from oxforddictionaries.words import OxfordDictionaries
print("\n *** Oxford Dictionary *** \n")

word = input(' Enter word : ')

app_id, api_key = '86bad9b7', 'b36d710e0a1ea7cbf4080c46e66fa8db'

od = OxfordDictionaries(app_id, app_key)
relax1 = od.get_synonyms("absorb").json()
synonyms = relax1['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
relax2 = od.get_antonyms("small").json()
antonyms = relax2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['antonyms']

res1 = [res['text'] for res in synonyms]
res2 = [res['text'] for res in antonyms]

print(f" Meaning : {res1}")
print(f" Opposite : {res2}")