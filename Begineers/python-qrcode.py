'''
Install below Python Module before You run this code.
>>> pip install qrcode 
'''

import qrcode
print("\n *** Convert Text to QRCode *** \n")

def convert_text_to_qrcode(input_string):
	qr.add_data(input_string)
	qr.make(fit=True)
	qrcode_image = qr.make_image(fill_color="black", back_color="yellow")
	qrcode_image.show()

if __name__ == '__main__':
	qr = qrcode.QRCode(box_size=10, border=4)
	input_string  = input(' Enter Input String : ')
	convert_text_to_qrcode(input_string)