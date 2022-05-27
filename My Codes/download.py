import random 
import time 
level = 0
print("Download begins\n")
while level < 100:
      print(f"{level} percent! \n") 
      level +=random.randint(2,19)
      time.sleep(0.5) 
while level >= 100:   
      print("100 percent! \n")
      print("Download complete.")
      break