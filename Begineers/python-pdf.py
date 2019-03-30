# importing required modules 
import PyPDF2 

filename = input('\n enter PDF filename with extension (eg: sample.pdf): ')  

# creating a pdf file object 
pdfFileObj = open(filename, 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
print(pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() 