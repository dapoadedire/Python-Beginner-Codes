
import sys
import time


def slow_write(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


welcome ="┏━━┓┏━━┓┏━━┓┏━━┓\n┗━┓┃┃┏┓┃┗━┓┃┗━┓┃\n┏━┛┃┃┃┃┃┏━┛┃┏━┛┃\n┃┏━┛┃┃┃┃┃┏━┛┃┏━┛\n┃┗━┓┃┗┛┃┃┗━┓┃┗━┓\n┗━━┛┗━━┛┗━━┛┗━━┛  "

two = "\n┏━━┓\n┗━┓┃\n┏━┛┃\n┃┏━┛\n┃┗━┓\n┗━━┛"
zero = "\n┏━━┓\n┃┏┓┃\n┃┃┃┃\n┃┃┃┃\n┃┗┛┃\n┗━━┛"
#slow_write(welcome)
slow_write(two + zero + two + two)
"""  
slow_write("Hello, how're you doing?")
print("")
slow_write("This function slowly writes anything you input. \nI am sure you will find it useful in any of your projects")

print("Bye")  
    

"""