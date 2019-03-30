import random
print("\n *** Rolling the Dices *** \n")
minimum, maximum = 1, 6
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
	print(" Dice1 => {} || Dice2 => {} ".format(random.randint(minimum, maximum), random.randint(minimum, maximum)))
	roll_again = input("\n Roll the Dices again (yes/y) : ").lower()
