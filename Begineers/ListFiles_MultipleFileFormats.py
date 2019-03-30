import fnmatch, os, time

print("\n *** List All Files Under Multiple File Formats. *** \n")
drive = input(" Enter the Drive Letter : ").upper()
drive_letter = drive + "://"
file_formats = ['*.jpg', '*.jpeg', '*.png']
matches = []

count, start_time = 0, time.process_time()
for root, dirnames, filenames in os.walk(drive_letter):
	for extensions in file_formats:
		for filename in fnmatch.filter(filenames, extensions):
			matches.append(os.path.join(root, filename))
			count += 1

end_time = time.process_time()

for data in matches:
	print(" -> {}".format(data))

print("\n Scanning completed : {} secs".format(abs(start_time - time.process_time())))
print("\n Totally {} files under {} Drive.".format(count, drive))
