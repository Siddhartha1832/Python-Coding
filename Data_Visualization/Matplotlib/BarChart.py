'''
Install below Python Module before You run this code.
>>> pip install matplotlib --upgrade 
'''

import matplotlib.pyplot as plt
x, y = [1,3,5,7,9],[5,2,7,8,2]
x2, y2 = [2,4,6,8,10],[8,6,2,5,6]
plt.bar(x, y, label='First Line', color='blue')
plt.bar(x2, y2, label='Second Line', color='red')
plt.xlabel('X axis Name: Bar Number')
plt.ylabel('Y axis name: values')
plt.title('Bar Chart using Matplotlib')
plt.legend()
plt.show()