'''
Install below Python Module before You run this code.
>>> pip install matplotlib --upgrade 
'''
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sleeping, eating = [7,8,6,11,7], [2,3,4,3,2]
working, playing =  [7,8,7,2,2], [8,5,7,8,13]
plt.stackplot(days, sleeping, eating, working, playing, colors=['r','b','g','y'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Stack Plot using Matplotlib')
plt.legend()
plt.show()
