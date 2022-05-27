quote = input("Input a quote")
f = open("quote.txt","a")
f.write("\n"+quote)

f.close()

f = open("quote.txt", "r")
print(f.read())

f.close