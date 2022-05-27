import random 
import string 

lower = string.ascii_lowercase
upper = string.ascii_uppercase 
number = string.digits
symbol =string.punctuation

all = lower + upper + number + symbol
#length = int(input("Enter the length of the password \n"))
length = 12
pwd = "".join(random.sample(all, length))

print("Your password is: ",pwd)

choice = input("\nDo you want to store password in txt file ? y/n ")

if choice == "y" : 
 f = open("pwd.txt","a")
 f.write("\n"+pwd)
 #We are using \n so that if we store multiple passwords then we must be able to identify the different passwords
 print("Your password is successfully stored in the file pwd.txt")
 f.close()
else :
  pass