'''
Install below Python Module before You run this code.
>>> pip install forex_python --upgrade 
'''

from forex_python.converter import CurrencyRates,CurrencyCodes
from forex_python.bitcoin import BtcConverter
import datetime
 
storage = {}
cr = CurrencyRates()
bc = BtcConverter()
cc = CurrencyCodes()

currency_code = ['AUD','BGN','BRL','CAD','CHF','CNY','DKK','CZK','GBP','HKD','HRK','HUF','IDR','ILS','INR','JPY','KRW','MXN','MYR','NOK','NZD','PHP', 'PLN','RON','RUB','SEK','SGD','THB','TRY','USD','ZAR','EUR']
print("\n Currency codes : {} ".format(currency_code))

def allCurrencyRates(source):
	if source.upper() in currency_code:
		storage = cr.get_rates(source.upper())
	print("\n Listing latest currecnt rates for {} \n".format(source.upper()))
	for key,value in storage.items():
		print(" {} -> {} ".format(key,value))

def specificCurrencyRates(source,dest,value):
	if source.upper() in currency_code:
		if dest.upper() in currency_code:
			#print("\n One {} in {} => {} ".format(source.upper(),dest.upper(),cr.get_rate(source.upper(),dest.upper())))
			print("\n One {} in {} {} => {} ".format(source.upper(),value,dest.upper(),cr.convert(source.upper(),dest.upper(),value)))

def bitcoinsPrice(source,value):
	if source.upper() in currency_code:
		print("\n Latest Bitcoin price for {} is {} ".format(source.upper(),bc.get_latest_price(source.upper())))
		print("\n Convert Amount {} into Bitcoins ({}) is {} ".format(value,source.upper(),bc.convert_to_btc(value,source.upper())))

def currencySymbol(source):
	if source.upper() in currency_code:
		print("\n Currency symbol for code ({}) is {} ".format(source.upper(),cc.get_symbol(source.upper())))

source_curr_code = input("\n Enter the currency code to list of other country latest rates : ")
print("\n Currency Rates \n 1. All Currency Rates \n 2. Specific Currency Rate \n 3. Latest Bitcoin Price \n 4. Currency Symbol \n 0. Exit")
choice = int(input("\n Enter your choice : "))
if choice==1:
	allCurrencyRates(source_curr_code)
elif choice==2:
	dest_curr_code = input("\n Enter Opponent Currency Code : ")
	amount = int(input("\n Enter the amount : "))
	specificCurrencyRates(source_curr_code,dest_curr_code,amount)
elif choice==3:
	amount = int(input("\n Enter the amount : "))
	bitcoinsPrice(source_curr_code,amount)
elif choice==4:
	currencySymbol(source_curr_code)
else:
	print("\n Invalid choice.. \n Exiting..")
