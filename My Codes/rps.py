import random 
score = 0 
print(f"Score = {score}") 

 
user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random. choice(possible_actions)
  
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
 
if user_action == computer_action:
     print(f"Both players selected {user_action}. It's a tie!")
         score += 0
         print(f"Score = {score}")
    
      elif user_action == "rock":
        
         if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            score += 5
            print(f"Score = {score}")  
            
         else:
            print("Paper covers rock! You lose.")
            score -= 1
            print(f"Score = {score}") 
      
      elif user_action == "paper":
        
         if computer_action == "rock":
            print("Paper covers rock! You win!")
            score += 5
            print(f"Score = {score}") 
            
         else:
            print("Scissors cuts paper! You lose.")
            score -= 1
            print(f"Score = {score}") 
    
      elif user_action == "scissors":
        
         if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            score += 2
            print(f"Score = {score}") 
            
         else:
            print("Rock smashes scissors! You lose.")
            score -= 1
            print(f"Score = {score}") 
            
      else:
            break    
            
            
       
      if score >= 10:
            print("You win")
            
            
          