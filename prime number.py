num=int(input('Enter a number:'))
y=[]
for i in range(1,num+1):
    if(num%i==0):
     y.append(i)
if(len(y)==2):
    print("prime number")
else:
    print("not prime")    

