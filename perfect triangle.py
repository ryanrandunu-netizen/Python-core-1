#for loop
row=int(input("Enter the number of rows that you want :"))
j=0
for i in range(1,(row+1)):
    print(' '*(row-j),'*'*(2*i-1),' '*(row-j),end='')
    j+=1
    print()
