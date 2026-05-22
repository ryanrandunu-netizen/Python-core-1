j=int(input("Enter how many rows you need?:"))
for i in range(1,j+1):
    print(' '*(j-i),'*'*i,end='')
    print()