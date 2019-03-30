'''
Install below Python Module before You run this code.
>>> pip install pillow PIL --upgrade 
# place images file in current folder
'''

import PIL, os
from PIL import Image
print("\n Image Size Reducer..")
basewidth = int(input("\n Enter the bandwidth value (Best = 800) : "))
list_files = [x for x in os.listdir() if x.endswith((".jpg", ".png", ".jpeg", ".png", ".gif"))]

for files in list_files:
    img = Image.open(files)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    #output_file_name = "image"+i+".jpg"
    print("\n Before size of file {} : {} bytes.".format(files,os.stat(files).st_size))
    img.save(files)
    print(" After Image Compression , size of file {} : {} bytes.".format(files,os.stat(files).st_size))

print("\n Totally {} Images File Size are Reduced Sucessfully...".format(len(list_files)))
