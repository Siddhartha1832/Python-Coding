'''
Install below Python Module before You run this code.
>>> pip install matplotlib --upgrade 
'''

import matplotlib.pyplot as plt
x, y = [1,2,3,4], [4,6,1,7] 
x2, y2 = [1,2,3,4], [10,15,12,18]
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
plt.xlabel('X axis Name: Plot Number')
plt.ylabel('Y axis name: values')
plt.title('Interesting Graph \n Check it out')
plt.legend()
plt.show()
