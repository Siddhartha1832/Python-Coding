'''
Install below Python Module before You run this code.
>>> pip install PIL Image --upgrade 
'''
import PIL, os
from PIL import Image
print("\n Convert All Images into PDFs..")

list_files = [x for x in os.listdir() if x.endswith(".jpg") or x.endswith(".png") or x.endswith(".jpeg") or x.endswith(".png") or x.endswith(".tiff") or x.endswith(".gif")]
basewidth = 800
for files in list_files:
    img = Image.open(files)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    #output_file_name = "image"+i+".jpg"
    print("\n Before size of file {} : {} bytes.".format(files,os.stat(files).st_size))
    img.save(files+".pdf")
    print("\n File Size NOW : {} bytes.".format(os.stat(files).st_size))

list_files1 = [x for x in os.listdir() if x.endswith(".pdf")]
print("\n Listing All PDFs.. \n")
for files1 in list_files1:
    print(files1)
