num=int(input('Enter a number(greater than 0):'))
count=0
while(num!=0):
    if(num%2==0 and num%3==0):
        count+=1
    num=int(input('Enter a number(greater than 0):'))
print(f'{count} numbers can be devidede by 2 and 3')    

        
