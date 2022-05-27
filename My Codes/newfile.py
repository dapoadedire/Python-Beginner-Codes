def myfunc():
   # t = int(input("t = "))
    if t < 0:
       y = -3*t**2 + 3*t - 5
    elif t >0:
       y = 3*t**2 - 3*t - 5
    else:
       y = 3*t**2 - 3*t + 5
   
    print("y =", y)
    
for t in range(-9,91,3):
   myfunc()
