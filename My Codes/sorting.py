
def sorting(list):
   sort = input("\nAsc/Dcs")
   if sort == "asc":
      list.sort()
   else: 
      list.sort(reverse = True)
   print(list)
  
list = [2,8,9,0,4,6,8,9,2,4,0,6,8]
sorting(list)