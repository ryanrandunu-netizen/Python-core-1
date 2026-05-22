num=int(input('Enter a number(greater than -1):'))
min=num
while(num!=0):
    num=int(input('Enter a number(greater than -1):'))
    if(min>num):
        min=num
print(f'Min number is {min}') 
