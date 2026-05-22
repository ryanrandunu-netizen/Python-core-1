num=int(input('Enter a number(greater than -1):'))
prev=num
while(num!=-1):
    num=int(input('Enter a number(greater than -1):'))
    if(num>prev):
        print('Inceasing')
    else:
        print('Decreasing')
    prev=num    
