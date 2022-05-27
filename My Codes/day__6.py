def word_func(word_list):
     length_list= []
     for i in word_list:
         length_list.append(len(i))
         length_list.sort()
     print("\nLongest word(s) \n")
     for j in word_list:
         if len(j) == length_list[-1]:
            print(f"{j} = {len(j)} letter(s)")
     print("\nShortest word(s) \n")        
     for k in word_list:
         if len(k) ==length_list[0]:
            print(f"{k} = {len(k)} letter(s)")
       
#word_list= ["okay","list", "function", "number", "the", "task", "recursion", "sleep", "program", "find", "orange", "large"]
word_list = ["boy", "cat", "dog"]       
word_func(word_list)