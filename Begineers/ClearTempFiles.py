'''
Install below Python Module before You run this code.
>>> pip install getpass
'''
import shutil, getpass
paths = [r"C:\TEMP", r"c:\windows\temp", r"C:\Users\{}\AppData\Local\Temp".format(getpass.getuser())]
for path in paths:
	shutil.rmtree(path, ignore_errors=True)
	print("Cleared Temp files under directory ({}) sucessfully!! ".format(path))