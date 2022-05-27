import random 

def quote():
    quote_list = ["T0","T1","T2","T3","T4","T5","T6"]
    length = len(quote_list)- 1
    rand = random.randint(0, length)
    print(quote_list[rand])
  
show = True
while show == True: 
  quote()
  
  again = input("\nDo you want more quote?\n[Yes or No] ")
  if "y" not in again:
    show = False
    print("\nBye")
  else:
    show = True
       