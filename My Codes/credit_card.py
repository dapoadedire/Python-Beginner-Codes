card_no = input("Input your credit card number")
if (len(card_no) == 16) and (card_no.isdigit()):
  print(f"************{card_no[12:16]}")
else:
  print("Error")