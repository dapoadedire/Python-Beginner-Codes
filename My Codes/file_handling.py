"""
You can specify the mode used to open a file by applying a second argument to the open function.

Sending "r" means open in read mode, which is the default. 

Sending "w" means write mode, for rewriting the contents of a file.

Sending "a" means append mode, for adding new content to the end of the file.



Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files). 
"""

# write mode

open("filename.txt", "w")



# read mode

open("filename.txt", "r")

open("filename.txt")



# binary write mode

file = open("filename.txt", "wb")

#close
file.close()

cont = file.read()
print(cont)

print(file.read(5))

#Each character is 1 byte

for line in file.readlines():
      print(line, end = "")
     
for line in file:
      print(line)
     
file = open("newfile.txt","w")

file = open("newfile.txt","a")#append


file.write("My name is Farouq")
file.close()

msg = "Hi, I am learning Javascript and I am very interested in the position"
file = open("newfile.txt", "w")
amount = file.write(msg)
print(amount)
file.close()


try:
    f = open("newfile.txt")
    cont = f.read()
    print(cont)
     
finally:
    f.close()
   
 
with open("newfile.txt") 
as f:
      print(f.read())