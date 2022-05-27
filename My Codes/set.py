"""
this_set = {"apple", "pineapple", "orange", "coconut", "watermelon", "yam", "rice", "beans", "fish", "potato"}

this_set.remove("apple")
this_set.discard("watermelon") 
this_set.pop()
this_set.clear()
print(this_set)


that_set = {"Tesla", "Apple", "Facebook", "Twitter", "Amazon", "IBM" } 
this_set.add("semolina")
print(this_set)

this_set.update(that_set)
print(this_set)
"""


odd = {1,3,5,7,9,11,13,15,17,19}
prime = {2,3,5,7,11,13,17,19}

x = odd.union(prime)
print(x)

y = odd.intersection(prime)
print(y)

z = odd.symmetric_difference(prime)
print(z)

a = odd.difference(prime)
print(a)

b = prime.difference(odd)
print(b)