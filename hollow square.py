row=int(input("Enter the number of rows that you want to input in the grid:"))

#nested loop for printing hollow grid

for i in range(1,row+1):
    if(i==1 or i==row):
        for j in range(1,row+1):
            print("*",end=' ')
        print()    
    else:
        print("*"," "*(row),"*",end=' ')
        print()    
   