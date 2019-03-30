'''
Install below Python Module before You run this code.
>>> pip install matplotlib numpy --upgrade 
'''

import matplotlib.pyplot as plt
import numpy as np
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Loading Data from File using Numpy')
plt.legend()
plt.show()
