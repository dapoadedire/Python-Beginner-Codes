with open('book.txt','r') as f:
    for line in f.readlines():
        print(line[0]+str(len(line)))
