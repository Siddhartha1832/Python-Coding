print("\n *** Geometrical Calculations *** \n")
pi = 3.14 
print(" MainMenu \n 1. Square \t 2. Rectangle \t 3. Triangle \t 4. Sphere \n 5. Cube \t 6. Circle \t 7. Trapezoid \t 8. Cone \t 9. Exit ")

while True:
	choice = int(input("\n Enter your choice : "))
	if choice == 1:
		side = int(input("\n Enter the side value : "))
		print("\n Perimeter of square is ",side*4)
		print("\n Area of square is ",side*side)
	elif choice == 2:
		length = int(input("\n Enter the length value : "))
		width = int(input("\n Enter the width value : "))
		print("\n Perimeter of rectangle is ",(2*(length+width)))
		print("\n Area os rectangle is ",length*width)
	elif choice == 3:
		base = int(input("\n Enter the base value : "))
		height = int(input("\n Enter the height value : "))
		print("\n Area of triangle is ",(float(base+height)/2))
	elif choice == 4:
		radius = int(input("\n Enter the radius value : "))
		print("\n Surface area of sphere is ",float(4*pi*(radius*radius)))
		print("\n Volume of sphere is ",float((4/3)*pi*(radius*radius*radius)))
	elif choice == 5:
		side = int(input("\n Enter the side value : "))
		print("\n Surface area of cube is ",6*side*side)
		print("\n volume of cube is ",side*side*side)
	elif choice == 6:
		radius = int(input("\n Enter the radius value : "))
		print("\n Perimeter of circle is ",float(2*pi*radius))
		print("\n Area of circle is ",float(pi*radius*radius))
	elif choice == 7:
		base1 = int(input("\n Enter the base1 value : "))
		base2 = int(input("\n Enter the base2 value : "))
		height = int(input("\n Enter the height value : "))
		print("\n Perimeter and Area of trapezoid is ",float(height*(base1+base2)/2))
	elif choice == 8:
		radius = int(input("\n Enter the radius value : "))
		height = int(input("\n Enter the height value : "))
		print("\n Surface area of cone is ",(float(pi*radius*height)))
		print("\n Volume of cone is ",(float((1/3)*pi*radius*radius*height)))
	elif choice == 9:
		print("\n Exiting..")
		exit(0)
	else:
		print('\n Invalid Choice, Please try again..')
