"""
class Shape: 

    def __init__(self, w, h):

        self.width = w

        self.height = h



    def area(self):

        print(self.width*self.height)



class Rectangle(Shape):

    #your code goes here

    def perimeter(self):
        print(2*(self.width+self.height))



w = int(input())

h = int(input())



r = Rectangle(w, h)

r.area()

r.perimeter()


class Player:

    def __init__(self, name, level):

        self.name = name

        self.level = level



    def intro(self):

        print(self.name + " (Level " + self.level + ")")



#your code goes here

name = input()
level = input()
player = Player(name,level)
player.intro()
#Player.intro(player)


"""

class Vector2D:
      def __init__(self, x, y):
          self.x = x
          self.y = y
      def __add__(self, other):
          return Vector2D(self.x + other.x, self.y + other.y)
         
first = Vector2D(5,7)
second = Vector2D(3,9)
third = Vector2D(6,5)
result = first + second + third
print(result.x)
print(result.y)
           
          
         
"""
More magic methods for common operators:

__sub__ for -

__mul__ for *

__truediv__ for /

__floordiv__ for //

__mod__ for %

__pow__ for **

__and__ for &

__xor__ for ^

__or__ for |



The expression x + y is translated into x.__add__(y). 

However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 

There are equivalent r methods for all magic methods just mentioned. 


Python also provides magic methods for comparisons.

__lt__ for <

__le__ for <=

__eq__ for ==

__ne__ for !=

__gt__ for >

__ge__ for >=



 If __ne__ is not implemented, it returns the opposite of __eq__. 

There are no other relationships between the other operators. 

There are several magic methods for making classes act like containers.

__len__ for len()

__getitem__ for indexing

__setitem__ for assigning to indexed values

__delitem__ for deleting indexed values

__iter__ for iteration over objects (e.g., in for loops)

__contains__ for in



There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types
"""

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        #your code goes here
        self._lives -=1
        while self._lives == 0:
             print("Game Over")
             break
             

p = Player("Cyberpunk77", 3)
#for i in range(3):
p.hit()
p.hit()
p.hit()