
  
import random

def roll():
  
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  print(die1, die2)
  print("")
  if die1 == die2 == 6 :
    roll()


print("Your Favorite Dice Game is Loading")
print("")


question = input('Would you like to roll the dice \n[Yes or No]?\n').lower()

while 'n' not in question:
    if 'y' in question.lower():
      
        roll()
        
        question = input('Would you like to roll the dice \n[Yes or No]?\n')
            

    else:
      
        print('Invalid response. Please type "Yes" or "No".\n')
        question = input('Would you like to roll the dice \n[Yes or No]?\n')        

print('Thanks for playing \nGood-bye and have a nice day')