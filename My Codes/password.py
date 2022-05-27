import string 
import random

print("Hello, this is a random password generator")

length = int(input("Length of password: \n")) 

password = "".join(random.sample(string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation , length))

print(password)
