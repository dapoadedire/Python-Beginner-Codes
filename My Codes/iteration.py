i = 0
while i < 6:
  i += 1
  if i%2 == 0 :
    continue 
  print(i)
 

for x in "bananas":
      if x == "a":
          continue
#     if x == "n":
#          break
      print(x)
else:
      print("Done")
      
      
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
      