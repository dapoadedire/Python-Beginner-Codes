try:
    a = "45 BC"
    b = 100 
    c = a/b
    print(c)
except ValueError as e:
    print('Reason:', e)