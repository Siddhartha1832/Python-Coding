print("\n *** Find the Gravitational Force Acting Between Two Objects *** \n")

mass1 = float(input(" Enter First Mass : "))
mass2 = float(input(" Enter Second Mass : "))
r = float(input(" Enter the Distance Between the Centres of Masses : "))

G = 6.673*(10**-11)
f = (G*mass1*mass2)/(r**2)

print("\n The Gravitational force is {} N".format(round(f,2)))
