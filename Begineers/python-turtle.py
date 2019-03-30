'''
Install below Python Module before You run this code.
>>> pip install turtle --upgrade

# Turtle - Python Library which lets you command a turtle to draw all over it! 
'''

import turtle
window = turtle.Screen() # creates a graphics window
window.title('Python Turtle') # setthe title of window
window.bgcolor('light green') # set window color as light green
turtle.shape("turtle") # set turtle shape
tom = turtle.Turtle() # create a turtle named tom
tom.color('red') # set turtle tom color as red
tom.circle(100, 360) # set wradius of circle and degree
tom.hideturtle() # hide the turtle arrow head
turtle.done() # complete the program