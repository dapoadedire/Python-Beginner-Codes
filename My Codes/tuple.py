"""
Tuples are unchangeable 


this_tuple = ("apple", "pineapple", "orange", "coconut", "watermelon", "yam", "rice", "beans", "fish", "potato")
#del this_tuple 
this_tuple = list(this_tuple)
this_tuple.append("shawarma")

print(this_tuple)

"""

info = ("Adedire Adedapo Farouq", "200L","Electronics/Electrical Engineering Department", "19 years", "Osun State", "Santos", "Oluwatise", "Electron", "Paragon", "Adeayo", "Lateefah", "Feranmi")

(name, level, dept, age, pob, *classmates ) = info

print(f"Name : {name}") 
print(*classmates)