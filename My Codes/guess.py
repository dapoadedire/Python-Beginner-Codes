import random

num = random.randint(1,20)
guess = int(input("\nGuess a number between 1 and 20\n"))
while num!= "guess":
  if (guess > num):
   print("\nYour guess is too high \n")
   guess = int(input("\nGuess a number between 1 and 20\n"))
  elif (guess < num):
   print("\nYour guess is too low \n")
   guess = int(input("\nGuess a number between 1 and 20\n"))
  else:
   print("\nYou're correct\n")
   break 