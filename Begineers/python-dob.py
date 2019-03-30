from datetime import datetime

def age_calculator(dob):
	b_date = datetime.strptime(dob, '%d/%m/%Y')
	age = round(((datetime.today() - b_date).days/365), 2) # 3 decimal points
	print(f"\n ==> Your age is {age}")

if __name__ == '__main__':
	print('\n *** Age Calculator *** \n')
	dob = input(' Enter Your Date-of-Birth (format: dd/mm/yyyy): ')
	age_calculator(dob)
