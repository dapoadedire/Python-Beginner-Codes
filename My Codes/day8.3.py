import time
import sys

def slow(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def myfunc(sentence):
          sList = list(sentence.split())
          l = len(sList) 
          a,b = sList[-1], sList[0:l-1]
          b = " ".join(b)   
          result= f"{a} {b}"
          slow(f"\n{result}")
          time.sleep(0.2)
          if result != s:
              myfunc(result)    
s = "You do not matter as much as you think you do anyway"
myfunc(s)