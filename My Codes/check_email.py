import re
valid_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
  if(re.fullmatch(valid_regex, email)):
    print("This is a valid email")
  else:
    print("This is an invalid email")

check(input("Input an email"))