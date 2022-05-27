import random
import tkinter as tk
from PIL import Image,ImageTk


window=tk.Tk()
window.geometry("500x700")
window.title("Rock Paper Scissors Game by twitter.com/dapo_adedire ")

player = ""
computer = ""
player_score = 0
computer_score= 0


text_area=tk.Text(master=window,height=12,width=32, bg="blue")
text_area.grid(column=15,row=4)



def result(play, comp):
    global player_score
    global computer_score
    if player == computer:
       player_score +=0
       computer_score +=0
       print("It's a tie")
    elif (player == "rock") and (computer=="scissors"):
       player_score +=1
       print("You win")
    elif (player== "paper") and (computer == "rock"):
       player_score +=1
       print("You win")
    elif (player=="scissors") and (computer == "paper"):
       player_score +=1
       print("You win")
    else:
       computer_score+=1
       print("You lose")
       
   
       
    final= "Play: \nUser : {p}\nComputer : {c}\nScore:\nUser : {ps}\nComputer : {cs}  ".format(p =     player.upper() , c = computer.upper(), ps=player_score, cs=computer_score, font=('arial', 18,'bold', "red"))
    
    text_area=tk.Text(master=window,height=12,width=32, bg="blue")
    text_area.grid(column=15,row=4)
    text_area.insert(tk.END,final)
   
"""                                    
def yes():
    global again
    again == True
def no():
    global again 
    again == False
"""
#event

def rock():
    global player
    global computer   
    player='rock'
    computer= random.choice(['scissors','paper','rock'])
    result(player, computer)

def paper():
    global player
    global computer  
    player='paper'
    computer= random.choice(['scissors','paper','rock'])
    result(player, computer)

def scissors():
    global player
    global computer  
    player='scissors'
    computer= random.choice(['scissors','paper','rock'])
    result(player, computer)

    

 
#buttons
button1=tk.Button(text="       Rock         ",bg="red",command=rock, height=1,width=12,font=('arial',15,'bold'))
button1.grid(column=15,row=1)

button2=tk.Button(text="        Paper         ",bg="pink",command=paper, height=1,width=12,font=('arial',15,'bold'))
button2.grid(column=15,row=2)

button3=tk.Button(text="         Scissors         ",bg="yellow",command=scissors , height=1,width=12,font=('arial',15,'bold'))
button3.grid(column=15,row=3) 

"""
button4=tk.Button(text="   Play Again : Yes   ",bg="green",command=yes, height=1, width=12,font=('arial',8,'bold'))
button4.grid(column=15,row=5) 
    
 
button5=tk.Button(text="Play Again : No",bg="red", command = no, height=1, width=12,font=('arial',8,'bold'))
button5.grid(column=15,row=6) 
"""

window.mainloop()