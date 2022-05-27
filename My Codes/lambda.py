x = lambda a : a + 5
print(x(5))

def myfunc(b):
    return lambda a : a**b
root2 = myfunc(2)
root3 = myfunc(3)
print(root2(20))
print(root3(20))
    
   
