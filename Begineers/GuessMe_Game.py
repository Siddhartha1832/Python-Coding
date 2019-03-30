import random

print("\n *** Guess My Number! *** \n")
answer = random.randint(1,50)

while True:
  question = int(input("\n Guess My number : "))
  if question == "":
    print("\n Exiting..")
    exit(0)
  elif question == answer:
    print("\n {} was Correct!".format(answer))
    print(" Thank you for playing this game.. \n Exiting..")
    exit(0)
  elif question < answer:
    print("\n {} is lesser than my number, Try again..".format(question))
  else:
    print("\n {} is greater than my number, Try again..".format(question))
