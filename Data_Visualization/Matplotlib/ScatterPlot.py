'''
Install below Python Module before You run this code.
>>> pip install matplotlib --upgrade 
'''
import matplotlib.pyplot as plt
x, y = [1,2,3,4,5,], [5,2,4,3,1]
plt.scatter(x,y, label='scatter plot', color='blue', s=40, marker="*")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot using Matplotlib')
plt.legend()
plt.show()
