class Dog:
      def __init__(self, name, color):
           self.name = name
           self.color = color
           
      def bark(self):
           print("Woof woof ")
jack = Dog("Jack", "Black")
print(jack.name)
print(jack.color)
jack.bark()

#Inheritance 
class Animal:
      def __init__(self, name, color):
           self.name = name
           self.color = color
           
class Dog(Animal):          
      def bark(self):
           print("Woof woof ") 
class Cat(Animal):
      def meow(self):
           print("Meeoww")
class Man(Animal):
      def shout(self):
           print("Ewoooo Eweeee")   
           
              
tesla =  Man("Tesla", "Black")
print(tesla.name)
tesla.shout()
Man.shout(tesla)


class A:
    def __init__(self, name, color):
          pass 
     
    def spam(self):
          print(1)
         
class B(A):
    def spam(self):
          print(2)
          super().spam()
         
A.spam()
B.spam()