#python 3.7.1

while True:
  
    name = input("Whats your name?: ")
    age = input("How old are you?: ")
    if age.isdigit() and int(age) > 15:
        print ("Congradulations you can drive!") 
    elif age.isdigit() and int(age) < 16:
        print ("Sorry you can not drive yet") 
    else:
        print ("Enter a valid number") 
    print ("it's been very nice getting to know you " + name)
    print ("")
    
    run_again = input("Run again? ")
    if run_again.lower() == 'no':
        break
    