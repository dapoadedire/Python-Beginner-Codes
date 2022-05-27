import random


again = True
while again == True:
      round = int(input("How many rounds do you want to play in this session?")) 
      player_score= 0
      comp_score = 0 
      print(f"Player = {player_score} points")
      print(f"Computer = {comp_score} points")
      for i in range(round) :
          print(f"\nRound {i +1}\n")
          player = input("\nPlay\n[\"R\" for Rock, \"P\" for Paper, \"S\" for Scissors]")
          if player.lower() == "r":
            player = "Rock"
          elif player.lower() == "p":
            player = "Paper"
          elif player.lower() == "s":
            player = "Scissors"
          else:
            pass
          comp_list = ["Rock", "Paper", "Scissors"]
          computer = random.choice(comp_list)
          print(f"\nYou play {player}, computer plays {computer}.\n")    
          if player == computer:
             print(f"Both players selected {player}. It's a tie!")
             print(f"Player = {player_score} points")
             print(f"Computer = {comp_score} points")  
    
          elif player == "Rock":       
               if computer == "Scissors":
                  print("Rock smashes Scissors ✂ ! You win!")
                  player_score += 1
                  print(f"Player = {player_score} points")
                  print(f"Computer = {comp_score} points")        
               else:
                  print("Paper covers Rock!")
                  comp_score += 1
                  print(f"Player = {player_score} points")
                  print(f"Computer = {comp_score} points")     
          elif player == "Paper":      
               if computer== "Rock":
                  print("Paper covers rock!")
                  player_score += 1
                  print(f"Player = {player_score} points")
                  print(f"Computer = {comp_score} points")   
               else:
                  print("Scissors cuts paper!")
                  comp_score += 1
                  print(f"Player = {player_score} points")
                  print(f"Computer = {comp_score} points")  
          elif player == "Scissors":      
               if computer == "Paper":
                  print("Scissors cuts paper!")
                  player_score += 1
                  print(f"Player = {player_score} points")
                  print(f"Computer = {comp_score} points")           
               else:
                  print("Rock smashes scissors!")
                  comp_score += 1
                  print(f"Player = {player_score} points")
                  print(f"Computer = {comp_score} points")   
       
      if player_score > comp_score:
            print("\nYou win this session.")   
      elif player_score == comp_score:
            print("\nOops, this session is a tie!")
      else: 
            print("\nYou lose this session")
           
      play_again = input("\nWould you like to play another session?\n[\"Yes\" or \"No\"]\n")
      if "y" == play_again.lower()[0]:
            again == True
      else:
            print("Bye, thanks for playing!")
            break