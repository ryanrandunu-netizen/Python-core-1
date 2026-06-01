x=input("Enetr your input(use space to seperate):").split(',')

y=list(map(int,x))

num=int(input('Enter the number that you want to find in the list:'))

#checking whether the num is in the list
for i in y:
    if(i==num):
        is_in=True
        break
    else:
        is_in=False
print(is_in)        

