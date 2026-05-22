num1=int(input('Enter a number:'))
num2=int(input('Enter another number:'))
num3=int(input('Enter another number:'))
if(num1>num2):
    if(num1>num3):
        print(f'{num1} is the MAX number')
        if(num2>num3):
             print(f'{num3} is the MIN number')
        else:
            print(f'{num2} is the MIN number')
    else:
        print(f'{num3} is the MAX nuumber')
else:
    if(num2>num3):
         print(f'{num2} is the MAX number')
         if(num1>num3):
            print(f'{num2} is the MIN number')
         else:
            print(f'{num3} is the MIN number')
    else:
         print(f'{num3} is the MAX number')
              


    
