'''
Install below Python Module before You run this code.
>>> pip install pyspeedtest --upgrade 

# Test your Internet connection bandwidth to locations around the world with this interactive broadband
# The Global Broadband Speed Test - https://www.speedtest.net/
'''

import speedtest
print("\n *** Internet SpeedTest using Python *** \n")
st = speedtest.Speedtest()
st.get_servers()
st.get_best_server()
st.download()
st.upload()
print(f" Result => \n {st.results.dict()}")