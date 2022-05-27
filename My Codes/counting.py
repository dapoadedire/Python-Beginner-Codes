count_x= 0
count_o= 0
text = "xoxodhdzhjjdsz"
for i in text:
    if i == "x":
      count_x +=1
for j in text:
    if j == "o":
      count_o +=1
if count_o == count_x:
    print("True")
print(count_x)
print(count_o)