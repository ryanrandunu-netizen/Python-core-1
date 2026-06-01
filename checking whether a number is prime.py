num=int(input("Enter a number:"))

is_prime=True

for i in range(2,num):
    if num%i==0:
        is_prime=False

print(f'Is {num} a prime number?={is_prime}')        