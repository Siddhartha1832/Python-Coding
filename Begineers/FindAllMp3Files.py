import os, fnmatch
print("\n Find all MP3 files.. \n")
rootPath = '/'
pattern = '*.mp3'
for root, dirs, files in os.walk(rootPath):
	for filename in fnmatch.filter(files, pattern):
		print( os.path.join(root, filename))
