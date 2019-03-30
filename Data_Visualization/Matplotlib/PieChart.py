'''
Install below Python Module before You run this code.
>>> pip install matplotlib --upgrade 
'''

import matplotlib.pyplot as plt
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['red','blue','green','pink']
plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow= True, explode=(0,0.1,0,0), autopct='%1.1f%%')
plt.title('Pie Chart using Matplotlib')
plt.show()
