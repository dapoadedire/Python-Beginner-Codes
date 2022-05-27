file_one = open("file_one.txt","w")
file_one.write("I do not care about optimism or pessimism; fuck that, we are gonna get it done. — Elon Musk")
file_one.close()

file_two = open("file_two.txt","w")
file_two.write("2022 is already on the move. You are getting distracted again. You have dreams to chase, not people to impress. Wake up!")
file_two.close()



words= open('file_one.txt').read().split()
set_one= set(words)

words= open('file_two.txt').read().split()
set_two= set(words)


print("\nUnique words ")
y = set_one.intersection(set_two)
print(y)


print("Union")
x = set_one.union(set_two)
print(x)


print("\nSymmetric Diff")
z = set_one.symmetric_difference(set_two)

print(z)
print("\nDifference 1")
a = set_one.difference(set_two)
print(a)
print("\nDifference 2")
b = set_two.difference(set_one)
print(b)



