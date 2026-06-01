row=int(input("Enter the number of rows you want to enter:"))

for i in range(1,row+1):
    if i%2==1:
        for j in range(1,row+1):
            if j%2==1:
              print('\u2B1c',end='')
            else:
              print("\u2b1B",end='')
    else:
        for k in range(1,row+1):
            if k%2==1:
              print("\u2b1B",end='')
            else:
              print('\u2B1c',end='')
    print()    
