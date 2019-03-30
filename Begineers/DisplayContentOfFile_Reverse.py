print("\n *** Display Contents of File in Reverse Order *** \n")

file_name = input(" Enter the File Name : ")
file_format = input(" Enter the File Format : ")
file = file_name + "." + file_format

print("\n Content of file ({}) : ".format(file))
for line in open(file):
	print(line)

print("\n Content of file ({}) in Reverse Order: ".format(file))
count = 0
for line in reversed(list(open(file))):
	print(line.rstrip())
	count += 1

print("\n Content of file ({}) with capatalize first letter of every word: ".format(file))
with open(file, 'r') as f:
	for line in f:
		print(line.title())

print("\n Total lines in the file ({}) is {} ".format(file, count))