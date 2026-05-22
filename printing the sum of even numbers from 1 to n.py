#while loop
n=int(input('Enter a integer:'))
i=2
sum=0
while(i<=n):
    sum=sum+i
    i+=2
print(sum)   

#for loop
n=int(input('Enter a integer:'))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print(sum)

