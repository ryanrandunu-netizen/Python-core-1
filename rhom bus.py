#for loop
row=int(input("How many rows do you need? :"))
for i in range((row-1),-1,-1):
    print(' '*i,'*'*row,end='')
    print()