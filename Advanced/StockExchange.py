'''
Install below Python Module before You run this code.
>>> pip install pandas pandas_datareader --upgrade 
'''
import pandas_datareader.data as web
from datetime import datetime, timedelta
print("\n *** Stock Exchange using Python *** \n")

company_codes = ['AAPL', 'MSFT', 'FB', 'AMZN', 'SBUX', 'GOOG', 'BABA', 'JNJ', 'JPM', 'BAC', 'WMT', 'WFC', 'INTC', 'VZ', 'ORCL', 'HON']
start_date = (datetime.now() - timedelta(days=5)).strftime('%d-%m-%Y')

for code in company_codes:
    df = web.DataReader(code, "yahoo", start_date, datetime.now())
    code_high = round(df['High'].tail(5)[-1], 2)
    code_low =  round(df['Low'].tail(5)[-1], 2)
    code_open = round(df['Open'].tail(5)[-1], 2)
    code_close = round(df['Close'].tail(5)[-1], 2)
    code_volume = round(df['Volume'].tail(5)[-1], 2)
    code_adj_close = round(df['Adj Close'].tail(5)[-1], 2)
    print(f" Code: {code} || High: {code_high} || Low: {code_low} || Open: {code_open} || Close: {code_close} || Volume: {code_volume} || Adj Close: {code_adj_close} ")
