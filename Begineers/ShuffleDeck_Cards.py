import itertools, random
print("\n *** Shuffle Deck of Cards *** \n")

draw_cards = int(input(" How many Cards you want to Draw : "))
# Make a Deck of Cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# Shuffle the Cards
random.shuffle(deck)
# Draw Five Cards
print("\n You got : \n")
for i in range(draw_cards):
	print(" {} of {} ".format(deck[i][0], deck[i][1]))
