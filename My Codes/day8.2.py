import time
def myfunc(sentence):
          sList = list(sentence.split())
          l = len(sList) 
          a,b = sList[-1], sList[0:l-1]
          b = " ".join(b)   
          result= f"{a} {b}"
          print(f"\n{result}")
          time.sleep(0.2)
          if result != s:
              myfunc(result)    
s = "You do not matter as much as you think you do anyway"
myfunc(s)