x=list(map(int,input("Enter numbers that you want to insert into the list(use commas within numbers):").split(",")))

prev=0
new=0

#checking the numbers in the list in the sorted order

for i in x:
    new=i
    if(new>=prev):
        is_sorted=True
    else:
        is_sorted=False
        break
    prev=new

print(is_sorted)        
