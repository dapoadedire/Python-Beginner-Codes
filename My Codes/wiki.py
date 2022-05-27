import wikipedia

search = input("What do you want to search ? \n")

''' sentences = 2 refers to numbers of line the number may vary it is according to you '''
result = wikipedia.summary(search, sentences = 2)

print(result)