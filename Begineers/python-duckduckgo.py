'''
Install below Python Module before You run this code.
>>> pip install duckduckpy --upgrade

# DuckDuckPy is a Python library for querying DuckDuckGo API and 
render results either to Python dictionary or namedtuple.
'''

from duckduckpy import query
print("\n *** DuckDuckGo Search *** \n")
search = input(' Enter text to Search in DuckDuckGo: ')
response = query(search)
print(f'\n Response -> {response}')
print(f'\n Response.related_topics[0] -> {response.related_topics[0]}')