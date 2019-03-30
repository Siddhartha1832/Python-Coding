'''
- Coinbase: Secure online platform for buying, selling, transferring, and storing digital currency.
- Coinbase URL: https://www.coinbase.com/
- Reference: https://github.com/coinbase/coinbase-python
# Signup Coinbase account to get API key & Secret-> https://www.coinbase.com/

- Install Coinbase Python Module in CMD or Terminal.
>>> pip install coinbase --upgrade
'''

from coinbase.wallet.client import Client
print("\n *** CoinBase Using Python *** \n")
api_key = input(' Enter API Key : ')
api_secret = input(' Enter API Secret : ')
client = Client(api_key, api_secret)
print('\n Current User information : {}'.format(client.get_current_user()))
print('\n Coinbase Accounts Information : {}'.format(client.get_accounts()))
print('\n Coinbase Primary Account Information : {}'.format(client.get_primary_account()))
print('\n Get supported native currencies : {}'.format(client.get_currencies()))
print('\n Get exchange rates : {}'.format(client.get_exchange_rates()))
print('\n Buy Prices : {}'.format(client.get_buy_price(currency_pair = 'BTC-USD')))
print('\n Sell Price : {}'.format(client.get_sell_price(currency_pair = 'BTC-USD')))
print('\n Spot Price : {}'.format(client.get_spot_price(currency_pair = 'BTC-USD')))
print('\n Current Server Time : {}'.format(client.get_time()))
print('\n Get Authorization Information: {}'.format(client.get_auth_info()))
print('\n Get Transaction : {}'.format(account.get_transactions()))
print('\n Get Reports : {}'.format(client.get_reports()))
print('\n Get Buys : {}'.format(account.get_buys()))
print('\n Get Sells : {}'.format(account.get_sells()))
print('\n Get Sells: {}'.format(account.get_deposits()))
print('\n Get Withdrawls : {}'.format(account.get_withdrawals()))
print('\n Get Orders : {}'.format(client.get_orders()))
print('\n Get Checkouts : {}'.format(client.get_checkouts()))
