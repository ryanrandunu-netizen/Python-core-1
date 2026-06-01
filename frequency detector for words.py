list1=list(input('Enter some words that you want to input(split words by commas):').split(','))
length_prev=0
length_new=0
dict_={}
for i in range(0,len(list1)):
    list2=[]
    length_new=len(list1[i])
    if length_new!=length_prev:
        for j in range(0,len(list1)):
            if len(list1[j])==len(list1[i]):
                list2.append(list1[j])
                dict_[len(list1[i])]=list2
    length_prev=length_new

for key,value in dict_.items():
     print(f'{key}:{value}')







