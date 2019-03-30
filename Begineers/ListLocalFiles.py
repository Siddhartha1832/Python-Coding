import fnmatch, os

print("\n *** List All Files Under User Defined LocalDrive. *** \n")
drive = input(" Enter the Drive Letter : ").upper()
file_format = input(" Enter the file format : ")
rootPath = drive+":/"
pattern = '*.'+file_format

print("\n")
count = 0
for root, dirs, files in os.walk(rootPath):
	for filename in fnmatch.filter(files, pattern):
		print(os.path.join(root, filename))
		count += 1

print("\n Totally {} files in the .{} format under {} drive.. ".format(count, file_format, drive))
