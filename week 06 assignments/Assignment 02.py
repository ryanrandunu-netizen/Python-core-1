num=int(input('Enter a number(greater than -1):'))
count=0
while(num!=-1):
    if(num>0):
        count+=1
        num=int(input('Enter a number(greater than -1):'))
print(f'{count} positive numbers')                
        
