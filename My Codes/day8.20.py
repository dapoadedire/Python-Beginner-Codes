import time
def crazyloop(sentence):
     l = len(list(sentence.split())) 
     for i in range(l):
          sentence = list(sentence.split())
          l = len(sentence) 
          lastword, others = sentence[-1], sentence[0:l-1]
          others = " ".join(others)   
          sentence= f"{lastword} {others}"
          print(f"\n{sentence}")
          time.sleep(1)        
sentence=input("Input a sentence : \n")
crazyloop(sentence)