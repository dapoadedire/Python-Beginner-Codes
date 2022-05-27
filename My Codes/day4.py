import random 
def even():
     x = random.randint(100, 300)
     [print(x) if x%2 ==0 else even()]
[even() for i in range(10)]