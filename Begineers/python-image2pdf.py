'''
Install below Python Module before You run this code.
>>> pip install img2pdf 
'''

import img2pdf
print("\n *** Convert Image to PDF File. *** \n")

# Replace Image file path to Convert into PDF file.
file_name = r'C:\APT\Programming\Python\sample.jpg'
dest_file_name = file_name.split('\\')[-1].split('.')[0].upper() + ".pdf"

with open(dest_file_name, "wb") as f:
    f.write(img2pdf.convert(file_name))

print(f"\n Converted from {file_name.upper()} to {dest_file_name} Sucessfully! ")
