import random


again = True
while again == True:
      round = int(input("How many rounds do you want to play in this session?")) 
      player_score= 0
      comp_score = 0 
      print(f"\nScore : Player {player_score}—{comp_score} Computer") 
      for i in range(round) :
          print(f"\nROUND {i +1}\n")
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
          print(f"\nPlay: Player [{player}] —[{computer}] Computer\n")    
          if player == computer:
             print(f"\nScore : Player {player_score}—{comp_score} Computer") 
    
          elif player == "Rock":       
               if computer == "Scissors":
                  player_score += 1
                  print(f"\nScore : Player {player_score}—{comp_score} Computer")        
               else:
                  comp_score += 1
                  print(f"\nScore : Player {player_score}—{comp_score} Computer")   
          elif player == "Paper":      
               if computer== "Rock":
                  player_score += 1
                  print(f"\nScore : Player {player_score}—{comp_score} Computer") 
               else:
                  comp_score += 1
                  print(f"\nScore : Player {player_score}—{comp_score} Computer") 
          elif player == "Scissors":      
               if computer == "Paper":
                  player_score += 1
                  print(f"\nScore : Player {player_score}—{comp_score} Computer")         
               else:
                  comp_score += 1
                  print(f"\nScore : Player {player_score}—{comp_score} Computer") 
       
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