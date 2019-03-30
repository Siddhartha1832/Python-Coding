'''
Install below Python Module before You run this code.
>>> pip install matplotlib csv --upgrade 
'''

import matplotlib.pyplot as plt
import csv

"""
save below values in 'example.txt' & put in same folder 
where this python code reside,

1,5
2,3
3,4
4,7
5,4
6,3
7,5
8,7
9,4
10,6
"""

x, y = [], []
with open('example.txt','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Loading Data from File!')
plt.legend()
plt.show()
