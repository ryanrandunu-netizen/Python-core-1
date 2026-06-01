list1=list(map(int,input("Enter the list of numbers that you want to input(split them using commas)").split(',')))
prev=0
new=0
dict_={}
for i in range(0,len(list1)-1):
    count=0
    new=list1[i]
    if new!=prev:
        for j in range(0,len(list1)-1):
            if new==list1[j]:
                count+=1
        dict_[new]=count
    prev=new

for key,value in dict_.items():
    print(f'{key}:{value}')                
