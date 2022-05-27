
car = {
  "brand": "For",
  "model": "Mustang",
  "year": 1964
}

#x = car.setdefault("color", "white")

y = car.setdefault("brand", "Tesla")
print(y)
#print(x) 

"""
car = {
 "car1":{
  "name":"Tesla", 
  "year": 2020
  }, 
 "car2":{
  "name":"Ford", 
  "year": 2021
  } 
 } 
 
print(car)

bike1 = {
   "name" : "Bajaj", 
   "year" : "2019"
   } 
bike2 = {
   "name" : "Jicheng", 
   "year" : "2021"
   } 
bikes ={
   "bike1" : bike1, 
   "bike2" : bike2
} 

print(bikes)

x = ('key1', 'key2', 'key3')
y = 0

this_dict = dict.fromkeys(x, y)

print(this_dict)

z = ('key1', 'key2', 'key3')

this_dict = dict.fromkeys(z)

print(this_dict)

this_dict = {
      "name" : "Adedire Adedapo Farouq ", 
      "level": "200L", 
      "year" : 2021, 
      "classmates": ["santos", "oluwatise", "adeayo", "lateefah", "enioluwa", "olaoti", "paragon"]
}

that_dict = this_dict.copy()
that_dict = dict(this_dict)
print(that_dict)



for x, y in this_dict.items():
      print(x, y)


for x in this_dict:
  print(x)
  
for x in this_dict:
  print(this_dict[x]) 
print("\n\n")
for x in this_dict.values():
  print(x) 
for x in this_dict.keys():
  print(x)

this_dict.clear()
this_dict.update({"year" : 2022})
this_dict.update({"color" : "yellow"})
this_dict.pop("classmates")

print(this_dict)

print(this_dict.items())
print(this_dict["year"])
print(this_dict["classmates"])
"""