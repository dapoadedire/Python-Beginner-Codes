def myfunc(text):
      text= text.lower().split()
      result = dict((i, text.count(i)) for i in text) 
      print("Result\n")
      for i in result:
            print(i, "=", result[i])
myfunc(input("Input a sentence : \n"))