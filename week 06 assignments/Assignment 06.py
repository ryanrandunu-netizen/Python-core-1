num=int(input('Enter a number(greater than 0):'))
avg=0
count=1
sum=num
while(num!=0):
    num=int(input('Enter a number(greater than 0):'))
    if(num>0):
        sum=sum+num
        count+=1
        avg=sum/count
print(f'Average of the positive numbers is {avg}')
    
