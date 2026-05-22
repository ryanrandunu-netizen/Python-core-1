#for loop
height=int(input("Enter the height of the rectangular :"))
width=int(input("Enter the width of the rectangular :"))
for i in range(1,(height+1)):
    print('*'*width,end='')
    print()