import fnmatch, os

print("\n *** Search Specific File under LocalDrive *** \n")

file_name = input(" Enter the File name to Search: ")
file_format = input(" Enter the File Format : ")
rootPath = '/'
pattern = file_name + '.' + file_format
count = 0

print("\n Search Results... \n")
start_time = time.clock()
for root, dirs, files in os.walk(rootPath):
	for filename in fnmatch.filter(files, pattern):
		print(os.path.join(root, filename))
		count+=1

print("\n Totally {} files in the .{} format.".format(count, file_format))