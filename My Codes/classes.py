class myClass:
      x = 5
p1 = myClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
          self.name = name
          self.age = age
    def myfunc(self):
          print("My name is " + self.name)
         
p1 = Person("Tesla", 18)
p1.age = 59
print(p1.name)
print(p1.age)

p1.myfunc()