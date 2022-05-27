def sqr(a,b):
   this_dict = {}
   for j in range(a,b+1): this_dict[j] = j**2  
   print(*list(this_dict.keys()), sep = ", ")  
sqr(1,20)